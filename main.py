from services.llm_service import LLMService

llm = LLMService()

print("=== AI Chatbot ===")
print("Type 'quit' to exit.\n")

while True:

    prompt = input("You: ")

    if prompt.lower() == "quit":
        print("\nGoodbye!")
        break

    answer = llm.ask(prompt)

    print("\nAI:")
    print(answer)
    print()