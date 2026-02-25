# BleuNova Public Brain (Sanitized Demo Edition)

This document describes the **public, sanitized BleuNova brain** included with the open-source repository. It mirrors the structural concepts of the private sovereign BleuNova system **without exposing any sensitive, proprietary, or regulated IP**.

The goal of this public brain is to:
- Give developers a real, functioning “agent brain” to experiment with  
- Demonstrate multi-agent design patterns  
- Provide safe, local tools for output  
- Allow extension and customization  
- Avoid hallucinations by restricting unsafe operations  

---

## 🔵 What This Public Brain *Is*

- A simple, extensible multi-agent configuration  
- Inspired by modern agent frameworks (OpenClaw-style brain design)  
- Safe to run locally  
- Fully filesystem-sandboxed (no real external APIs)  
- A teaching and experimentation platform  

This brain is designed for **developers**, **students**, and **builders** to understand how a brain is structured.

---

## 🔴 What This Public Brain *Is NOT*

- It is **not** the sovereign BleuNova Prime brain  
- It is **not** equipped with VeriAbyss (only a basic veracity mode is included)  
- It is **not** tied to real social media or email accounts  
- It is **not** permitted to generate regulated content  
- It contains **none** of the proprietary BLEULearn curriculum  
- It contains **none** of the Retreat Bleu, Breakroom, Nexus Kids, or BleuConsult universes  

All sensitive universes and IP are completely removed.

---

## 🧩 Universes Available in the Public Brain

The public brain ships with three safe “demo universes”:

### **1. `demo_general`**
A generic utility universe for basic tasks, scheduling demos, and content generation.

### **2. `demo_edtech`**
A *non-proprietary* educational demo universe that can:
- Explain simple topics  
- Create practice prompts  
- Provide reading or math tips  

It **does NOT** use BLEULearn, Ms. Ava Bloom, Nexus Kids, or any sovereign IP.

### **3. `demo_consulting`**
A simple business-logic universe intended for:
- Workflow suggestions  
- Productivity tips  
- High-level ops strategy  

It cannot produce regulated content.

---

## 👥 Agents Included in the Public Brain

These demo agents are safe and extendable:

### **SchedulerDemoAgent**
- Default router  
- Schedules fake tasks  
- Writes plans to `data/public_outbox/`

### **SocialDemoAgent**
- Drafts social posts  
- Creates simulated posting jobs  
- Does NOT interact with real platforms  
- All jobs written to disk

### **TeacherDemoAgent**
- Offers simple, generic educational explanations  
- Does NOT use or reference BLEULearn  
- No proprietary personas or codes  
- No student data

### **ConsultDemoAgent**
- Provides general operations advice  
- Avoids clinical, legal, or financial domains  
- Safe for all users  

---

## 🛠 Tools Available

All tools are **local** and **non-networked**:

- `file_outbox_demo` → writes text/JSON to `data/public_outbox/`
- `social_stub_demo` → simulates social posting
- `email_stub_demo` → simulates sending emails

These tools show how tool integrations work **without** touching external APIs.

---

## 🔀 Routing

The public router is intentionally simple:

- Default → `SchedulerDemoAgent`
- `demo_edtech` → `TeacherDemoAgent`
- `demo_consulting` → `ConsultDemoAgent`

This layout is easy to modify for custom builds.

---

## 🚀 How to Extend the Public Brain

To add your own brain:

1. Copy:  
   `config/bleunova_public_brain.yaml` → `config/my_custom_brain.yaml`

2. Add:
   - New universes  
   - New agents  
   - New prompts  
   - New tools (local only until advanced)

3. Update your runner to load the new brain.

This allows safe experimentation without touching the sovereign architecture.

---

## 🧠 Veracity Mode (Basic)

The public brain uses:
