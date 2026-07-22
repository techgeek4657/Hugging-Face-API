from pathlib import Path

CHAT_FOLDER = Path("chats")

def ensure_chat_folder():
    """
    Creates the chats folder if it does not exist.
    """

    CHAT_FOLDER.mkdir(exist_ok=True)

def chat_path(title: str) -> Path:
    """
    Returns the full path to a chat file.
    """

    return CHAT_FOLDER / f"{title}.json"

def chat_exists(title: str) -> bool:
    """
    Checks whether a chat file already exists.
    """

    return chat_path(title).exists()

def generate_new_chat_name() -> str:
    """
    Generates:
    New Chat 1
    New Chat 2
    New Chat 3
    ...
    """

    number = 1

    while True:

        title = f"New Chat {number}"

        if not chat_exists(title):
            return title

        number += 1