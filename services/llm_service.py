from huggingface_hub import InferenceClient
from config.settings import HF_TOKEN

class LLMService:
    def __init__(self):
        self.client = InferenceClient(
            token=HF_TOKEN
        )
    
    def ask(self, messages: list) -> str:

        response = self.client.chat_completion(
            model='meta-llama/Llama-3.1-8B-Instruct',
            messages=messages,
            max_tokens=300
        )

        return response.choices[0].message.content