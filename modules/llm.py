# LLM inference wrapper
from llama_cpp import Llama

class LLM:
    def __init__(self, model_path, device="cuda"):
        self.model = Llama(model_path=model_path, n_gpu_layers=32, n_ctx=2048)

    def generate(self, prompt):
        return self.model(prompt)["choices"][0]["text"]
