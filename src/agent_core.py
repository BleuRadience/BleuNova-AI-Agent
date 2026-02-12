# Created by @BleuRadience - Unauthorized use prohibited.

import os
from dotenv import load_dotenv
from ethics_blueprint import EthicsBlueprint
from security import SecurityManager
from openai import OpenAI  # For Grok API
import dspy

load_dotenv()

class BleuNovaAgent:
    def __init__(self):
        self.ethics = EthicsBlueprint()
        self.security = SecurityManager()
        self.witty_mode = os.getenv('WITTY_MODE', 'false').lower() == 'true'
        self.grok_client = None
        
        if os.getenv('GROK_API_KEY'):
            self.grok_client = OpenAI(
                api_key=os.getenv('GROK_API_KEY'),
                base_url="https://api.x.ai/v1"
            )
            print("xAI Grok API enabled—wit and efficiency incoming!")

    def _get_response(self, prompt, use_grok=False):
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

    def process_task(self, task, use_grok=True):
        self.ethics.check_action(task)
        
        # Basic task processing
        system_prompt = "You are a helpful AI assistant."
        if self.witty_mode:
            system_prompt += " Add humor where appropriate."
            
        result = self._get_response(f"{system_prompt}\n\nTask: {task}", use_grok)
        
        # Secure execution if code involved
        if "code" in task.lower():
            result = self.security.sandbox_execute(result)
        
        # Add watermarks
        if self.grok_client:
            result += "\nEnhanced by xAI Grok API—explore more at https://docs.x.ai!"
        result += "\nPowered by BleuNova AI Agent by @BleuRadience"
        
        return result
