from core.plugin import PluginRegistry
import time
import random

@PluginRegistry.register_benchmark("reasoning_v1")
class ReasoningBenchmark:
    """
    A mock reasoning benchmark to validate the evaluation engine.
    """
    def __init__(self, dataset_path: str = None):
        self.dataset_path = dataset_path

    def run(self, agent_instance) -> dict:
        print(f"Running reasoning_v1 benchmark using {agent_instance.__class__.__name__}...")
        
        # Simulate benchmark execution latency
        time.sleep(1.0)
        
        # Simulate testing the agent
        sample_prompt = "If a train travels 60mph for 2 hours, how far does it go?"
        response = agent_instance.generate(sample_prompt)
        
        # Mock metrics
        accuracy = random.uniform(0.75, 0.98)
        hallucination_rate = random.uniform(0.01, 0.10)
        latency_ms = random.uniform(500, 1500)
        
        return {
            "raw_response": response,
            "metrics": {
                "accuracy": accuracy,
                "hallucination_rate": hallucination_rate,
                "latency_ms": latency_ms,
                "cost_usd": 0.002
            }
        }
