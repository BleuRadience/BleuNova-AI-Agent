# Created by @BleuRadience - Unauthorized use prohibited.

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from threading import Thread
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_core import BleuNovaAgent
from dashboard import run_dashboard
from integrations.docker_helper import DockerHelper

load_dotenv()

app = FastAPI(title="BleuNova AI Agent")

# Initialize agent
agent = BleuNovaAgent()
docker_helper = DockerHelper(agent)

class TaskRequest(BaseModel):
    task: str

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "BleuNova AI Agent running. Access dashboard at port 8501."}

@app.post("/process-task")
def process_task(request: TaskRequest):
    try:
        result = agent.process_task(request.task)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/docker-assist")
def docker_assist(request: QueryRequest):
    try:
        result = docker_helper.assist(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run dashboard in thread
    dashboard_thread = Thread(target=run_dashboard, daemon=True)
    dashboard_thread.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
