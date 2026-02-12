
# BleuNova AI Agent

**BleuNova AI Agent: Your Ethical, Hacker-Proof Personal AI Companion**  
Self-hosted, autonomous AI agent for everyday tasks: messaging, file management, web browsing, video generation, IoT control, continual learning, and more — all with strong ethics and security built-in.

## Features
- Immutable ethical blueprint (no fabrication, harm prevention, consent gates)
- Hacker-proof design (zero-trust sandboxing, anomaly detection)
- Multi-agent orchestration with role-based collaboration
- Multi-modal capabilities (video gen via open-source models, voice, vision)
- xAI Grok API integration (optional — adds wit & humor)
- Visual dashboard + drag-and-drop workflow builder
- Docker assistance sub-agent (ask for setup help)
- Free/local-first (Ollama fallback), offline resilience, drift detection

## Installation by Operating System

BleuNova runs in Docker containers — the same repo works on macOS, Windows, and Linux. You just need Docker installed first.

### 1. macOS (Apple Silicon or Intel)
1. **Install Docker Desktop** (free for personal use)  
   - Download: https://www.docker.com/products/docker-desktop/  
   - Choose Apple Silicon (arm64) or Intel version  
   - Open the .dmg → drag to Applications → launch Docker Desktop  
   - Sign in (optional) → grant permissions when asked
2. **Clone the repo**  
   ```bash
   git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
   cd BleuNova-AI-Agent

Set up environment
Copy .env.example to .env and add any API keys (e.g., GROK_API_KEY for humor).
RunBashdocker-compose up --build→ Dashboard at http://localhost:8501
→ API at http://localhost:8000

2. Windows 10/11 (Home, Pro, Enterprise)

Install Docker Desktop (free for personal use)
Download: https://www.docker.com/products/docker-desktop/
Run the .exe installer
It will enable WSL 2 automatically (reboot if asked)
Launch Docker Desktop → sign in (optional) → allow firewall changes

Clone the repo (use PowerShell, Git Bash, or Command Prompt)Bashgit clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
Set up environment — same as macOS
Run — same command as macOSBashdocker-compose up --build

3. Linux (Ubuntu, Fedora, etc.)

Install Docker Engine (fastest & lightest — no VM layer)Bashsudo apt update && sudo apt install docker.io docker-compose -y   # Ubuntu example
sudo systemctl start docker
sudo usermod -aG docker $USER   # Log out/in to apply(See https://docs.docker.com/engine/install/ for your distro)
Clone, .env, and run — identical to the other platforms

After First Run: Get Help with Docker
Once BleuNova is running (even if installation was tricky), ask the built-in Docker assistance sub-agent for help anytime:

In the dashboard: type "Help me fix Docker on macOS" or "How do I restart containers?"
Via API: POST to /docker-assist with {"query": "Troubleshoot docker-compose up error"}

It will guide you step-by-step (and ask for explicit consent before suggesting any system changes).
Quick Start (after Docker is running)

Dashboard: http://localhost:8501
API example: curl -X POST http://localhost:8000/process-task -H "Content-Type: application/json" -d '{"task": "Summarize today's news"}'

Optional Enhancements

Enable witty/humorous responses: Set WITTY_MODE=true in .env (requires GROK_API_KEY)
Explore xAI Grok integration: https://docs.x.ai

Created by @BleuRadience — Unauthorized use prohibited.
text### What to Do Next
1. Replace the current README.md in your repo with this version.
2. Commit and push:
   ```bash
   git add README.md
   git commit -m "Update README with platform-specific Docker installation instructions"
   git push
