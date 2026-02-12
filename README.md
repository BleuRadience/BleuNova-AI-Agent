# BleuNova AI Agent

**BleuNova AI Agent: Your Ethical, Hacker-Proof Personal AI Companion**  
Self-hosted, autonomous AI agent for everyday tasks: messaging (Telegram/WhatsApp), file management, web browsing, video generation, IoT control, continual learning, multi-agent collaboration — all with strong ethics, zero-trust security, and optional witty personality via xAI Grok.

## Features
- Immutable ethical blueprint (truthfulness, no harm, consent gates, audit-ready logging)
- Hacker-proof design (microVM-style sandboxing, anomaly detection, drift alerts)
- Multi-agent orchestration with role-based teams (inspired by CrewAI patterns)
- Multi-modal capabilities (video generation via open-source models, voice STT/TTS, vision)
- xAI Grok API integration (optional — adds humor, fast tool calling, large context)
- Visual dashboard + drag-and-drop workflow builder (LangFlow-inspired)
- Built-in Docker assistance sub-agent (consent-gated help for setups & troubleshooting)
- Free/local-first (Ollama fallback), offline queuing & resilience
- Continual learning (replay-based + DSPy self-optimization)
- Curated skills marketplace (expandable via community)
- Watermarked outputs & provenance (clearly attributed to @BleuRadience)

## Installation by Operating System

BleuNova runs inside Docker containers — **the same repo works everywhere**.  
The only difference is installing **Docker** on your platform.

### macOS (Apple Silicon M1/M2/M3/M4 or Intel)
**Requirements**  
- macOS Ventura (13) or later  
- 8 GB RAM recommended (4 GB minimum)  

**Steps**  
1. Install Docker Desktop (free for personal use)  
   → Download: https://www.docker.com/products/docker-desktop/  
   → Choose Apple Silicon (arm64) or Intel version  
   → Open .dmg → drag to Applications → launch Docker Desktop  
   → Grant permissions when prompted  
2. Clone & run  
   ```bash
   git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
   cd BleuNova-AI-Agent
   cp .env.example .env          # edit .env if adding keys
   docker-compose up --build
Windows 10/11 (Home, Pro, Enterprise, Education)
Requirements

Windows 11 64-bit (23H2+) or Windows 10 64-bit (22H2+)
8 GB RAM recommended (4 GB minimum)
Virtualization enabled in BIOS (VT-x / AMD-V)

Steps

Install Docker Desktop (free for personal use)
→ Download: https://www.docker.com/products/docker-desktop/
→ Run .exe installer (enables WSL 2 automatically — reboot if asked)
→ Launch Docker Desktop → allow firewall changes
Clone & run (PowerShell / Git Bash / Command Prompt)Bashgit clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
copy .env.example .env        # edit .env if needed
docker-compose up --build

Linux (Ubuntu, Fedora, Debian, etc.)
Requirements

Modern Linux distro
4–8 GB RAM recommended

Steps

Install Docker Engine
Example (Ubuntu/Debian):Bashsudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo usermod -aG docker $USER   # log out/in→ Full guide: https://docs.docker.com/engine/install/
Clone & runBashgit clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
cp .env.example .env
docker-compose up --build

Quick Start (once running)

Dashboard (visual UI & builder): http://localhost:8501
API example (run a task):Bashcurl -X POST http://localhost:8000/process-task \
  -H "Content-Type: application/json" \
  -d '{"task": "Summarize latest AI news"}'

Get Help with Docker (Built-in Sub-Agent)
If installation or Docker commands confuse you:

Open dashboard → type e.g.:
"Help install Docker on macOS"
"Fix docker-compose error on Windows"
"How do I restart the agent container?"
Or API: POST to /docker-assist → {"query": "Troubleshoot docker up"}

The agent will:

Give tailored steps
Generate safe commands
Add humor if WITTY_MODE=true
Always ask consent before any system-changing suggestion

Optional Features

Humor & personality
Set WITTY_MODE=true in .env (requires GROK_API_KEY from https://console.x.ai)
Local models (completely free/offline)
Install Ollama → https://ollama.com
Set OLLAMA_MODEL=llama3 (or your preferred model) in .env
xAI Grok docs → https://docs.x.ai

Roadmap (2026 Goals)

v0.2: Public skills marketplace (bleuhub.ai)
v0.3: Native voice input/output
v0.4: Mobile companion (lightweight iOS/Android)
v0.5: Enterprise extras (RBAC, audit exports, SSO)

Community & Support

X: @BleuRadience
GitHub Discussions: here
Star history: Star History

Acknowledgments
Inspired by OpenClaw, CrewAI, AutoGen, LlamaIndex, DSPy, LangGraph, and xAI Grok.
Grateful to the open-source AI community.
License & Attribution
MIT License — commercial use, modification, and selling permitted (must keep copyright notice & disclaimer).
See LICENSE for full text.
Created by @BleuRadience — Unauthorized use prohibited.
textThis is now a **single, self-contained README** that covers:
- Clear value proposition
- All major features
- Step-by-step install for every major OS
- How to get ongoing help via the agent itself
- Quick usage
- Optional toggles (Grok, local models)
- Roadmap & community
- License clarity

Just copy-paste into your repo's README.md, commit, and you're set for launch.

Let me know if you'd like a matching repo description, social preview image suggestion, or first
