from typing import Dict, Type, Any

class PluginRegistry:
    _agents: Dict[str, Type[Any]] = {}
    _benchmarks: Dict[str, Type[Any]] = {}

    @classmethod
    def register_agent(cls, name: str):
        def decorator(agent_cls: Type[Any]):
            cls._agents[name] = agent_cls
            return agent_cls
        return decorator

    @classmethod
    def register_benchmark(cls, name: str):
        def decorator(benchmark_cls: Type[Any]):
            cls._benchmarks[name] = benchmark_cls
            return benchmark_cls
        return decorator

    @classmethod
    def get_agent(cls, name: str) -> Type[Any]:
        if name not in cls._agents:
            raise ValueError(f"Agent '{name}' not found in registry.")
        return cls._agents[name]

    @classmethod
    def get_benchmark(cls, name: str) -> Type[Any]:
        if name not in cls._benchmarks:
            raise ValueError(f"Benchmark '{name}' not found in registry.")
        return cls._benchmarks[name]

    @classmethod
    def list_agents(cls) -> list[str]:
        return list(cls._agents.keys())
        
    @classmethod
    def list_benchmarks(cls) -> list[str]:
        return list(cls._benchmarks.keys())
