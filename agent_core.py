from anthropic import Anthropic

class BleuNovaAgent:
    def __init__(self):
        # ... existing code ...
        self.claude_client = None
        if os.getenv('ANTHROPIC_API_KEY'):
            self.claude_client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
