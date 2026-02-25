# BleuNova AI Agent  
### Your Ethical, Hacker-Proof, Personal AI Companion (Public Demo Edition)

BleuNova is a **self-hosted, autonomous AI agent** designed for everyday tasks:

- Messaging (Telegram, WhatsApp)
- File & document management
- Smart web browsing
- Video generation (local models)
- IoT / smart home control
- Continual learning & memory
- Multi-agent collaboration

This public edition is a **safe, open-source demo** with a fully sanitized agent brain, ideal for developers, students, and experimenters.

---

# 🔐 Core Principles  

### ✔ **Immutable ethical blueprint**  
Truthfulness, consent gates, no-harm logic, transparent audit trails.

### ✔ **Hacker-proof design**  
MicroVM-style sandboxing, anomaly detection, and drift alerts.

### ✔ **Multi-agent orchestration**  
Role-based agent teams inspired by CrewAI patterns.

### ✔ **Multi-modal capabilities**  
Local-first support for video, voice (STT/TTS), and vision.

### ✔ **xAI Grok integration (optional)**  
Adds humor, fast tool-calling, and large context windows.

### ✔ **Visual dashboard**  
Drag-and-drop workflow builder (LangFlow-inspired).

### ✔ **Built-in Docker assistance**  
A consent-gated setup & troubleshooting helper.

### ✔ **Free / Local-first**  
Ollama fallback, offline queuing, and failure resilience.

### ✔ **Continual learning**  
Replay-based optimization + DSPy-style self-improvement.

### ✔ **Curated skills marketplace**  
Expandable via community plugins.

### ✔ **Watermarked outputs & provenance**  
Every generation is attributed to **@BleuRadience**.

---

# 🧠 Public Brain (Sanitized Demo)

The public version includes a safe, extendable multi-agent brain:

This brain includes:

### Demo Universes
- `demo_general`
- `demo_edtech`
- `demo_consulting`

### Demo Agents
- `SchedulerDemoAgent`
- `SocialDemoAgent`
- `TeacherDemoAgent`
- `ConsultDemoAgent`

### Local-Only Tools
- File outbox (writes to `data/public_outbox`)
- Social stub (simulated posting)
- Email stub (writes emails to disk)

### Basic Veracity Layer
A simplified guardrail system to avoid:
- hallucinations  
- unsafe operations  
- regulated content  

Full documentation:

---

# 📦 Installation by Operating System

BleuNova runs inside Docker containers — the same repo works everywhere.

---

# 🍎 macOS (Intel + Apple Silicon M1/M2/M3/M4)

### Requirements
- macOS Ventura (13) or later  
- 4–8 GB RAM  

### Steps
1. Install Docker Desktop  
   https://www.docker.com/products/docker-desktop/

2. Clone & run:

```bash
git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
cp .env.example .env
docker-compose up --build

---

# 📦 Installation by Operating System

BleuNova runs inside Docker containers — the same repo works everywhere.

---

# 🍎 macOS (Intel + Apple Silicon M1/M2/M3/M4)

### Requirements
- macOS Ventura (13) or later  
- 4–8 GB RAM  

### Steps
1. Install Docker Desktop  
   https://www.docker.com/products/docker-desktop/

2. Clone & run:

```bash
git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
cp .env.example .env
docker-compose up --build

🪟 Windows 10/11
Requirements
Windows 10/11 (64-bit)
Virtualization enabled (VT-x / AMD-V)
Steps
Install Docker Desktop
https://www.docker.com/products/docker-desktop/
Clone & run:
git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
copy .env.example .env
docker-compose up --build

🐧 Linux (Ubuntu, Debian, Fedora, etc.)
Requirements
Modern Linux distribution
4–8 GB RAM
Steps
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo usermod -aG docker $USER
# log out/in
Clone & run:
git clone https://github.com/BleuRadience/BleuNova-AI-Agent.git
cd BleuNova-AI-Agent
cp .env.example .env
docker-compose up --build

🚀 Quick Start (Once Running)
Dashboard
Visual UI:
http://localhost:8501
Example API Call
curl -X POST http://localhost:8000/process-task \
  -H "Content-Type: application/json" \
  -d '{"task": "Summarize latest AI news"}'

🧰 Built-In Docker Assistance
If you’re stuck, BleuNova includes a Docker helper agent.
Inside the dashboard, type:

“Help install Docker on macOS”
“Fix docker-compose error on Windows”
“Restart my agent container”
“Why won’t Docker start?”
Or through API:
POST /docker-assist
{ "query": "Troubleshoot docker up" }
The helper will:
Provide tailored steps
Suggest safe commands
Ask consent before anything system-changing

🎭 Optional Features
💬 Humor / Personality
Set in .env:
WITTY_MODE=true
Requires:
GROK_API_KEY=...

🤖 Local Models (Ollama)
Fully offline:
Install Ollama → https://ollama.com
Set in .env:
OLLAMA_MODEL=llama3
🔗 xAI Grok Integration
https://docs.x.ai

🗺 Roadmap (2026 Targets)
v0.2 — Public skills marketplace (bleuhub.ai)
v0.3 — Native voice input/output
v0.4 — Mobile companion (iOS/Android)
v0.5 — Enterprise suite (RBAC, audit exports, SSO)

🌐 Community & Support
X: @BleuRadience
GitHub Discussions: available in this repo

⭐ Acknowledgments
Inspired by:
OpenClaw
CrewAI
AutoGen
LlamaIndex
DSPy
LangGraph
xAI Grok
Grateful to the open-source AI community.
⚖ License & Attribution

MIT License (commercial use allowed).
Copyright ©
Created by @BleuRadience.
Unauthorized use prohibited.

