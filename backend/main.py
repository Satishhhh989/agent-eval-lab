from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.plugin import PluginRegistry
import agents.mock_agent  # Import to trigger registration
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Agent Evaluation Laboratory API",
    description="API for benchmarking autonomous AI agents",
    version="0.1.0"
)

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Agent Evaluation Laboratory API"}

@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/agents")
def list_agents():
    return {"agents": PluginRegistry.list_agents()}

@app.get("/api/v1/benchmarks")
def list_benchmarks():
    return {"benchmarks": PluginRegistry.list_benchmarks()}
