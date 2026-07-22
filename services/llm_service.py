from huggingface_hub import InferenceClient
from config.settings import HF_TOKEN


class LLMService:

    def __init__(self):

        self.client = InferenceClient(
            token=HF_TOKEN
        )

    def ask(self, messages: list) -> str:

        response = self.client.chat_completion(

            model="meta-llama/Llama-3.1-8B-Instruct",

            messages=messages,

            max_tokens=300

        )

        return response.choices[0].message.content.strip()


    def generate_title(self, messages: list) -> str:

        prompt = [
            {
                "role": "system",
                "content":
                (
                    "Generate a short chat title.\n"
                    "Maximum four words.\n"
                    "No quotation marks.\n"
                    "No punctuation.\n"
                    "Return ONLY the title."
                )
            }
        ]

        prompt.extend(messages)

        response = self.client.chat_completion(

            model="meta-llama/Llama-3.1-8B-Instruct",

            messages=prompt,

            max_tokens=15

        )

        title = response.choices[0].message.content.strip()

        title = title.replace('"', "")
        title = title.replace("'", "")
        title = title.replace("/", "-")
        title = title.replace("\\", "-")
        title = title.replace(":", "-")

        return title