import json
from colorama import Fore

MEMORY_FILE = "memory.json"


def handle_command(prompt, messages, long_term_memory):

    command = prompt.lower()

    # HELP
    if command == "/help":
        print(Fore.YELLOW + """
Available Commands

/help      Show this help menu
/history   Show conversation history
/reset     Clear chat memory
/exit      Exit chatbot
""")
        return True

    # HISTORY
    elif command == "/history":
        print(Fore.MAGENTA + "\nConversation History\n")

        for msg in messages[1:]:
            print(f"{msg['role']}: {msg['content']}\n")

        return True

    # RESET
    elif command == "/reset":
        system = messages[0]
        messages.clear()
        messages.append(system)

        print(Fore.YELLOW + "\nConversation reset.\n")
        return True

    # EXIT
    elif command == "/exit":
        print(Fore.YELLOW + "\nGoodbye!\n")
        return True

    return False