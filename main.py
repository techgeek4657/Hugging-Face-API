from services.llm_service import LLMService

llm = LLMService()

messages=[]

print("=== AI Chatbot ===")
print("Type 'quit' to exit.\n")

while True:

    prompt = input("You: ")

    if prompt.lower() == "quit":
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

    print("\nAI:")
    print(answer)
    print()