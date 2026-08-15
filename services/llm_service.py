from groq import Groq
from config.settings import GROQ_API_KEY


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )


    def ask(self, messages: list) -> str:

        try:

            response = self.client.chat.completions.create(

                model="llama-3.1-8b-instant",

                messages=messages,

                max_completion_tokens=2048

            )

            return response.choices[0].message.content.strip()


        except Exception as e:

            return f"AI Error: {e}"


    def stream(self, messages: list):

        response = self.client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=messages,

            max_completion_tokens=2048,

            stream=True

        )


        for chunk in response:

            content = chunk.choices[0].delta.content

            if content:

                yield content