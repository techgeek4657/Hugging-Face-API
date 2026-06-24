from services.llm_service import LLMService

llm = LLMService()

answer = llm.ask('Define what a 3D printer is and how it works.')

print('\nAi response:\n')
print(answer)