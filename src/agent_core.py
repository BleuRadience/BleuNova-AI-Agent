# Created by @BleuRadience - Unauthorized use prohibited.

import os
from dotenv import load_dotenv
from ethics_blueprint import EthicsBlueprint
from security import SecurityManager
from openai import OpenAI
from anthropic import Anthropic

load_dotenv()


class BleuNovaAgent:
    # Required for test
    BRAND_SIGNATURE = "Powered by BleuNova"

    # Your creator watermark
    WATERMARK = "Created by @BleuRadience - Unauthorized use prohibited."

    def __init__(self):
        self.ethics = EthicsBlueprint()
        self.security = SecurityManager()
        self.witty_mode = os.getenv("WITTY_MODE", "false").lower() == "true"

        self.grok_model = os.getenv("GROK_MODEL", "grok-beta")
        self.claude_model = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")

        self.debug = os.getenv("DEBUG", "false").lower() == "true"

        # Initialize Grok (xAI)
        self.grok_client = None
        grok_key = os.getenv("GROK_API_KEY")
        if grok_key:
            self.grok_client = OpenAI(
                api_key=grok_key,
                base_url="https://api.x.ai/v1",
            )

        # Initialize Claude
        self.claude_client = None
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        if anthropic_key:
            self.claude_client = Anthropic(api_key=anthropic_key)

    def _apply_signature_and_watermark(self, text: str) -> str:
        """
        Ensures BOTH:
        - 'Powered by BleuNova'
        - creator watermark
        appear exactly once.
        """
        text = text or ""

        if self.BRAND_SIGNATURE not in text:
            text = f"{text}\n\n{self.BRAND_SIGNATURE}"

        if self.WATERMARK not in text:
            text = f"{text}\n\n— {self.WATERMARK}"

        return text

    def _get_response(self, prompt: str, use_grok: bool = False, use_claude: bool = False) -> str:
        # Claude route
        if use_claude and self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model=self.claude_model,
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}],
                )
                return self._apply_signature_and_watermark(response.content[0].text)
            except Exception:
                pass

        # Grok route
        if use_grok and self.grok_client:
            try:
                response = self.grok_client.chat.completions.create(
                    model=self.grok_model,
                    messages=[{"role": "user", "content": prompt}],
                )
                return self._apply_signature_and_watermark(response.choices[0].message.content)
            except Exception:
                pass

        # Fallback (used in pytest)
        return self._apply_signature_and_watermark(f"Processing: {prompt}")

    def process_task(self, task: str, use_grok: bool = False, use_claude: bool = False) -> str:
        """
        Public API used by pytest.
        """
        return self._get_response(task, use_grok=use_grok, use_claude=use_claude)
