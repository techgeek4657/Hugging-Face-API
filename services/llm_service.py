from huggingface_hub import InferenceClient
from config.settings import HF_TOKEN

class LLMService:
    def __init__(self):
        self.client = InferenceClient(
            token=HF_TOKEN
        )
    
    def ask(self, prompt: str) -> str:

        response = self.client.chat_completion(
            model='meta-llama/Llama-3.1-8B-Instruct',
            messages=[
                {
                    "role": 'user',
                    'content': prompt
                }
            ],
            max_tokens=300 #Why only 300??? Why not more?
        )

        return response.choices[0].message.content