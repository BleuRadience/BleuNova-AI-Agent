# Created by @BleuRadience - Unauthorized use prohibited.

import docker
import time

class SecurityManager:
    def __init__(self):
        self.client = docker.from_env()
        self.timeout = int(os.getenv('SANDBOX_TIMEOUT', 5))

    def sandbox_execute(self, code):
        container = self.client.containers.run(
            "python:3.12-slim",
            command=f"python -c '{code}'",
            detach=True,
            remove=True,
            network_mode="none"
        )
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            container.reload()
            if container.status == 'exited':
                return container.logs().decode()
            time.sleep(0.5)
        container.kill()
        return "Execution timed out for security."
