from pathlib import Path

from utils.file_utils import (
    CHAT_FOLDER,
    generate_new_chat_name
)

from utils.chat_storage import (
    create_chat,
    load_chat,
    save_chat,
    rename_chat,
    delete_chat
)


class ChatManager:
    """
    Handles creating, opening,
    deleting and listing chats.
    """

    def __init__(self):

        CHAT_FOLDER.mkdir(exist_ok=True)

    def list_chats(self):

        chats = []

        for file in CHAT_FOLDER.glob("*.json"):

            chats.append(file.stem)

        chats.sort()

        return chats
    
    def create_chat(self, title=None):

        if title is None:

            title = generate_new_chat_name()

        create_chat(title)

        return title

    def open_chat(self, title):

        return load_chat(title)

    def save_chat(self, title, messages):

        save_chat(title, messages)

    def rename_chat(self, old_title, new_title):

        rename_chat(old_title, new_title)

    def delete_chat(self, title):

        delete_chat(title)

    def exists(self, title):

        return title in self.list_chats()