from services.llm_service import LLMService
from utils.chat_storage import load_chat, save_chat

llm = LLMService()

messages=load_chat()

print("=== AI Chatbot ===")
print("Type 'quit' to exit.\n")

if messages:
    print(f'Loaded {len(messages)} previous messages.\n')

while True:

    prompt = input("You: ")

    if prompt.lower() == "quit":
        save_chat(messages)
        print('\nConversation saved.')
        print("\nGoodbye!")
        break

    messages.append(
        {
            "role": 'user',
            'content': prompt
        }
    )

    answer = llm.ask(messages)
    
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    save_chat(messages)
    print("\nAI:")
    print(answer)
    print()