# BleuNova AI Agent

### Public Demo Edition

**Current Version:** 1.0.0-public  
**Status:** Educational Demo / Proof of Concept

---

## 🎯 What This Actually Is

This is a **simple, educational demonstration** of a basic AI agent structure. It shows how an agent can connect to LLM APIs (Claude, Grok) and process text tasks.

**This is NOT a production-ready autonomous agent.**

---

## ✅ What Works Right Now

| Feature | Status | Notes |
|---------|--------|-------|
| Claude API integration | ✅ Working | Anthropic Claude models |
| Grok (xAI) integration | ✅ Working | Requires API key |
| Basic text processing | ✅ Working | Simple Q&A |
| Environment config | ✅ Working | .env file support |
| Docker container | ✅ Working | Runs the demo |

---

## ❌ What Is NOT Included (Public vs Enterprise)

This public demo is **intentionally limited**. The following features are **NOT** in this repository:

| Feature | Public Demo | Enterprise |
|---------|-------------|------------|
| Multi-agent orchestration | ❌ | ✅ |
| Memory & continual learning | ❌ | ✅ |
| Tool calling / execution | ❌ | ✅ |
| Task planning & decomposition | ❌ | ✅ |
| IoT / smart home control | ❌ | ✅ |
| Video / image generation | ❌ | ✅ |
| Web browsing | ❌ | ✅ |
| File management | ❌ | ✅ |
| Docker assistance agent | ❌ | ✅ |
| Drag-and-drop workflow | ❌ | ✅ |
| Multi-modal capabilities | ❌ | ✅ |
| Self-improvement / learning | ❌ | ✅ |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker (optional)
- API keys for Claude or Grok (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the demo
python agent.py
