# Created by @BleuRadience - Unauthorized use prohibited.

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from agent_core import BleuNovaAgent

@pytest.fixture
def agent():
    return BleuNovaAgent()

def test_process_task(agent):
    result = agent.process_task("Test task", use_grok=False)
    assert "Powered by BleuNova" in result

def test_grok_integration(agent):
    if agent.grok_client:
        result = agent.process_task("Witty test", use_grok=True)
        assert "Enhanced by xAI" in result
    else:
        pytest.skip("No Grok API key configured")
