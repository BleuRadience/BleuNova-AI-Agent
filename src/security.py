# Created by @BleuRadience - Unauthorized use prohibited.

import os
import time
import docker
from docker.errors import NotFound, APIError


class SecurityManager:
    def __init__(self):
        try:
            self.client = docker.from_env()
        except Exception:
            self.client = None

        self.timeout = int(os.getenv("SANDBOX_TIMEOUT", "5"))
        self.mem_limit = os.getenv("SANDBOX_MEM_LIMIT", "128m")          # e.g. 128m
        self.nano_cpus = int(os.getenv("SANDBOX_NANO_CPUS", "500000000")) # 0.5 CPU
        self.pids_limit = int(os.getenv("SANDBOX_PIDS_LIMIT", "64"))
        self.max_log_lines = int(os.getenv("SANDBOX_LOG_TAIL", "200"))

        # You can pin this to 3.11 to match your runtime if you want consistency
        self.image = os.getenv("SANDBOX_IMAGE", "python:3.12-slim")

    def check(self, task: str) -> None:
        """
        Gate method for the agent. Raise an Exception to block.
        Keep it conservative; expand rules as needed.
        """
        # Example: block obvious attempts to run shell commands via prompts
        # (This is not a full policy engine—just a minimal guard.)
        dangerous = ["rm -rf", "mkfs", ":(){:|:&};:", "curl ", "wget "]
        lower = (task or "").lower()
        if any(x in lower for x in dangerous):
            raise ValueError("Potentially dangerous task content blocked by security policy.")

    def sandbox_execute(self, code: str) -> str:
        """
        Execute Python code inside a locked-down container with strict limits.
        Returns stdout/stderr (tailed) or a security timeout/error message.
        """
        if not self.client:
            return "Docker not available for sandboxed execution."

        code = code or ""

        try:
            # Run python reading code from stdin to avoid quoting/injection issues.
            container = self.client.containers.run(
                image=self.image,
                command=["python", "-"],
                stdin_open=True,
                detach=True,
                remove=True,
                network_mode="none",
                read_only=True,
                security_opt=["no-new-privileges:true"],
                cap_drop=["ALL"],
                mem_limit=self.mem_limit,
                nano_cpus=self.nano_cpus,
                pids_limit=self.pids_limit,
            )

            # Send code to stdin and close input
            try:
                sock = container.attach_socket(params={"stdin": 1, "stream": 1})
                sock._sock.sendall(code.encode("utf-8"))
                sock._sock.shutdown(1)  # close stdin
            except Exception:
                # If attach fails, still attempt to wait/log
                pass

            # Wait up to timeout seconds
            try:
                container.wait(timeout=self.timeout)
            except Exception:
                # Timeout or wait failure => kill as a security measure
                try:
                    container.kill()
                except (NotFound, APIError):
                    pass
                return "Execution timed out for security."

            # Grab tailed logs to prevent huge output
            try:
                out = container.logs(tail=self.max_log_lines).decode("utf-8", errors="replace")
            except (NotFound, APIError):
                out = ""

            return out.strip() if out.strip() else "(no output)"

        except Exception as e:
            return f"Sandbox execution failed: {e}"
