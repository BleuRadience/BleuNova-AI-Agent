# Created by @BleuRadience - Unauthorized use prohibited.

from agent_core import BleuNovaAgent

class DockerHelper:
    def __init__(self, parent_agent):
        self.parent = parent_agent

    def assist(self, user_query):
        # Consent via ethics
        action = {"type": "docker_assist", "query": user_query, "consent": True}  # Assume consent from endpoint call; in prod, add prompt
        if not self.parent.ethics.check_action(action):
            return "Consent required: Do you agree to Docker assistance? (Reply 'yes' to proceed)."
        
        # Delegate to sub-agent
        task = f"Provide Docker help for: {user_query}. Be witty if enabled."
        sub_agent = BleuNovaAgent()
        result = sub_agent.process_task(task, use_grok=True)  # Prefer Grok for humor
        
        # Sandbox if execution needed
        if "run" in user_query.lower() or "command" in user_query.lower():
            result = self.parent.security.sandbox_execute(result)
        
        return result
