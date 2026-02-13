# Created by @BleuRadience - Unauthorized use prohibited.

import os
from dotenv import load_dotenv
from ethics_blueprint import EthicsBlueprint
from security import SecurityManager
from openai import OpenAI  # OpenAI SDK configured for xAI via base_url
from anthropic import Anthropic  # Claude API
# import dspy  # Remove if unused

load_dotenv()


class BleuNovaAgent:
    # Runtime output watermark (appended to returned strings)
    WATERMARK = "Created by @BleuRadience - Unauthorized use prohibited."

    def __init__(self):
        self.ethics = EthicsBlueprint()
        self.security = SecurityManager()
        self.witty_mode = os.getenv("WITTY_MODE", "false").lower() == "true"

        # Configurable model names
        self.grok_model = os.getenv("GROK_MODEL", "grok-beta")
        self.claude_model = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")

        # Debug logging toggle
        self.debug = os.getenv("DEBUG", "false").lower() == "true"

        # Initialize Grok client (xAI)
        self.grok_client = None
        grok_key = os.getenv("GROK_API_KEY")
        if grok_key:
            self.grok_client = OpenAI(
                api_key=grok_key,
                base_url="https://api.x.ai/v1",
            )
            if self.debug:
                print("xAI Grok API enabled.")

        # Initialize Claude client
        self.claude_client = None
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        if anthropic_key:
            self.claude_client = Anthropic(api_key=anthropic_key)
            if self.debug:
                print("Claude API enabled.")

    def _apply_watermark(self, text: str) -> str:
        """Ensure watermark appears exactly once in the returned output."""
        text = text or ""
        if self.WATERMARK in text:
            return text
        return f"{text}\n\n— {self.WATERMARK}"

    def _log_debug(self, msg: str) -> None:
        if self.debug:
            print(msg)

    def _get_response(self, prompt: str, use_grok: bool = False, use_claude: bool = False) -> str:
        # Claude route
        if use_claude and self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model=self.claude_model,
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}],
                )
                return self._apply_watermark(response.content[0].text)
            except Exception as e:
                self._log_debug(f"Claude call failed: {e!r}")

        # Grok route
        if use_grok and self.grok_client:
            try:
                response = self.grok_client.chat.completions.create(
                    model=self.grok_model,
                    messages=[{"role": "user", "content": prompt}],
                )
                return self._apply_watermark(response.choices[0].message.content)
            except Exception as e:
                self._log_debug(f"Grok call failed: {e!r}")

        # Fallback
        return self._apply_watermark(f"Processing: {prompt}")

    def process_task(self, task: str, use_grok: bool = False, use_claude: bool = False) -> str:
        """
        Public API expected by tests.
        Runs security + ethics gates (non-crashing) then returns model response.
        Always returns a watermarked string.
        """
        # Security gate (best-effort)
        try:
            if hasattr(self.security, "scan"):
                self.security.scan(task)
            elif hasattr(self.security, "validate"):
                self.security.validate(task)
            elif hasattr(self.security, "check"):
                self.security.check(task)
        except Exception as e:
            return self._apply_watermark(f"Security blocked task: {e}")

        # Ethics gate (best-effort)
        try:
            if hasattr(self.ethics, "approve"):
                approved = self.ethics.approve(task)
                if approved is False:
                    return self._apply_watermark("Ethics blocked task.")
            elif hasattr(self.ethics, "validate"):
                ok = self.ethics.validate(task)
                if ok is False:
                    return self._apply_watermark("Ethics blocked task.")
            elif hasattr(self.ethics, "check"):
                ok = self.ethics.check(task)
                if ok is False:
                    return self._apply_watermark("Ethics blocked task.")
        except Exception as e:
            self._log_debug(f"Ethics module error (non-fatal): {e!r}")

        return self._get_response(task, use_grok=use_grok, use_claude=use_claude)

    # ... rest of your methods
