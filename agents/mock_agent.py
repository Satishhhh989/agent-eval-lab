from core.plugin import PluginRegistry

@PluginRegistry.register_agent("mock_agent")
class MockAgent:
    def __init__(self, model_identifier: str, hyperparameters: dict = None):
        self.model_identifier = model_identifier
        self.hyperparameters = hyperparameters or {}

    def generate(self, prompt: str) -> str:
        return f"Mock response for prompt: {prompt}"
