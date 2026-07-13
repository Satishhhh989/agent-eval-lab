from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class AgentConfig(Base):
    __tablename__ = "agent_configs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    provider = Column(String, index=True)
    model_identifier = Column(String)
    hyperparameters = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

class Benchmark(Base):
    __tablename__ = "benchmarks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    category = Column(String)

class Dataset(Base):
    __tablename__ = "datasets"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    benchmark_id = Column(Integer, ForeignKey("benchmarks.id"))
    version = Column(String)
    data_path = Column(String)
    
    benchmark = relationship("Benchmark")

class Experiment(Base):
    __tablename__ = "experiments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    problem_statement = Column(String)
    hypothesis = Column(String)
    status = Column(String, default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)

class ExperimentRun(Base):
    __tablename__ = "experiment_runs"
    
    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    agent_config_id = Column(Integer, ForeignKey("agent_configs.id"))
    benchmark_id = Column(Integer, ForeignKey("benchmarks.id"))
    dataset_id = Column(Integer, ForeignKey("datasets.id"))
    raw_outputs = Column(JSON)
    metrics_summary = Column(JSON)
    
    experiment = relationship("Experiment")
    agent_config = relationship("AgentConfig")
    benchmark = relationship("Benchmark")
    dataset = relationship("Dataset")

class Metric(Base):
    __tablename__ = "metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("experiment_runs.id"))
    metric_name = Column(String, index=True)
    value = Column(Float)
    
    run = relationship("ExperimentRun")
