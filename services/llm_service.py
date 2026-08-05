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

                max_tokens=800

            )

            return response.choices[0].message.content.strip()


        except Exception as e:

            return f"AI Error: {e}"