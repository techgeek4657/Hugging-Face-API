from services.llm_service import LLMService
from utils.chat_manager import ChatManager


llm = LLMService()
chat_manager = ChatManager()


def chat_interface(chat_title, chat_data):

    messages = chat_data["messages"]

    print("\n=========================")
    print(f" CHAT: {chat_title}")
    print("=========================")
    print("Type 'quit' to return to menu.\n")


    while True:

        prompt = input("You: ")


        if prompt.lower() == "quit":

            chat_manager.save_chat(
                chat_title,
                messages
            )

            print("\nReturning to chat menu...\n")
            break


        messages.append(
            {
                "role": "user",
                "content": prompt
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


        chat_manager.save_chat(
            chat_title,
            messages
        )


def show_menu():

    print("=========================")
    print("      CHAT MANAGER")
    print("=========================")


    chats = chat_manager.list_chats()


    if len(chats) == 0:

        print("No chats found in system history.")
        print("Press + to make a new chat.\n")

    else:

        for index, chat in enumerate(chats, start=1):

            print(
                f"{chat}: Press {index}"
            )

        print()


    print("+  Create new chat")
    print("-  Delete chat")
    print("R  Rename chat")
    print("0  Exit")
    print()



def create_new_chat():

    title = input(
        "Type a title for your chat:\n> "
    )


    if not title.strip():

        print(
            "\nChat creation cancelled.\n"
        )

        return


    chat_manager.create_chat(
        title.strip()
    )


    chat_data = chat_manager.open_chat(
        title.strip()
    )


    chat_interface(
        title.strip(),
        chat_data
    )



def delete_chat():

    chats = chat_manager.list_chats()


    if not chats:

        print(
            "\nNo chats to delete.\n"
        )

        return


    print("\nSelect chat to delete:\n")


    for index, chat in enumerate(chats, start=1):

        print(
            f"{chat}: Press {index}"
        )


    choice = input("\nDelete number: ")


    if choice.isdigit():

        index = int(choice) - 1


        if 0 <= index < len(chats):

            title = chats[index]


            confirm = input(
                f'Delete "{title}"? (y/n): '
            )


            if confirm.lower() == "y":

                chat_manager.delete_chat(
                    title
                )

                print(
                    "\nChat deleted.\n"
                )



def rename_chat():

    chats = chat_manager.list_chats()


    if not chats:

        print(
            "\nNo chats available.\n"
        )

        return


    print("\nSelect chat to rename:\n")


    for index, chat in enumerate(chats, start=1):

        print(
            f"{chat}: Press {index}"
        )


    choice = input("\nRename number: ")


    if not choice.isdigit():

        return


    index = int(choice) - 1


    if index < 0 or index >= len(chats):

        return


    old_title = chats[index]


    new_title = input(
        "\nNew title: "
    )


    if new_title.strip():

        chat_manager.rename_chat(
            old_title,
            new_title.strip()
        )

        print(
            "\nChat renamed.\n"
        )



while True:

    show_menu()


    choice = input("> ")


    if choice == "0":

        print("\nGoodbye!")
        break


    elif choice == "+":

        create_new_chat()


    elif choice == "-":

        delete_chat()


    elif choice.lower() == "r":

        rename_chat()


    elif choice.isdigit():

        chats = chat_manager.list_chats()


        index = int(choice) - 1


        if 0 <= index < len(chats):

            title = chats[index]

            chat_data = chat_manager.open_chat(
                title
            )

            chat_interface(
                title,
                chat_data
            )

        else:

            print(
                "\nInvalid chat number.\n"
            )


    else:

        print(
            "\nInvalid option.\n"
        )