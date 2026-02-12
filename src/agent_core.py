# Created by @BleuRadience - Unauthorized use prohibited.

import os
from dotenv import load_dotenv
from ethics_blueprint import EthicsBlueprint
from security import SecurityManager
from openai import OpenAI  # For Grok API
from anthropic import Anthropic  # For Claude API
import dspy

load_dotenv()

class BleuNovaAgent:
    def __init__(self):
        self.ethics = EthicsBlueprint()
        self.security = SecurityManager()
        self.witty_mode = os.getenv('WITTY_MODE', 'false').lower() == 'true'
        
        # Initialize Grok client
        self.grok_client = None
        if os.getenv('GROK_API_KEY'):
            self.grok_client = OpenAI(
                api_key=os.getenv('GROK_API_KEY'),
                base_url="https://api.x.ai/v1"
            )
            print("xAI Grok API enabled—wit and efficiency incoming!")
        
        # Initialize Claude client
        self.claude_client = None
        if os.getenv('ANTHROPIC_API_KEY'):
            self.claude_client = Anthropic(
                api_key=os.getenv('ANTHROPIC_API_KEY')
            )
            print("Claude API enabled—precision thinking activated!")

    def _get_response(self, prompt, use_grok=False, use_claude=False):
        if use_claude and self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
            except:
                pass
        
        if use_grok and self.grok_client:
            try:
                response = self.grok_client.chat.completions.create(
                    model="grok-beta",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content
            except:
                pass
        
        # Fallback to basic response
        return f"Processing: {prompt}"

    # ... rest of your methods
