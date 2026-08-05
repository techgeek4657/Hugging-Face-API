from groq import Groq
from config.settings import GROQ_API_KEY

import re


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


    def generate_title(self, messages: list):

        for attempt in range(2):

            try:

                title_messages = [

                    {
                        "role": "system",
                        "content":
                        (
                            "You are an AI that creates short chat titles.\n\n"

                            "Rules:\n"

                            "- The title should naturally describe the conversation.\n"
                            "- Keep it between 2 and 6 words whenever possible.\n"
                            "- No quotation marks.\n"
                            "- No emojis.\n"
                            "- No punctuation unless absolutely necessary.\n"
                            "- Do not say 'Title:' or explain anything.\n"
                            "- Respond ONLY with the title."
                        )
                    }

                ]

                title_messages.extend(messages)

                response = self.client.chat.completions.create(

                    model="llama-3.1-8b-instant",

                    messages=title_messages,

                    max_tokens=30

                )

                title = response.choices[0].message.content.strip()

                # Remove quotes
                title = title.replace('"', "")
                title = title.replace("'", "")

                # Remove illegal Windows filename characters
                title = re.sub(r'[\\/:*?"<>|]', "", title)

                # Collapse multiple spaces
                title = " ".join(title.split())

                # Reject empty titles
                if not title:

                    continue

                # If it is still too long, let the AI try again
                if len(title) > 35:

                    continue

                return title

            except Exception as e:

                print(f"Title generation error: {e}")

                break

        return None