import json

from utils.file_utils import (
    ensure_chat_folder,
    chat_path
)


def create_chat(title: str):
    """
    Creates a brand new chat.
    """

    ensure_chat_folder()

    data = {
        "title": title,
        "messages": []
    }

    with open(chat_path(title), "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_chat(title: str) -> dict:
    """
    Loads a chat from disk.
    """

    ensure_chat_folder()

    with open(chat_path(title), "r", encoding="utf-8") as file:

        return json.load(file)


def save_chat(title: str, messages: list):
    """
    Saves messages to a chat.
    """

    ensure_chat_folder()

    data = {
        "title": title,
        "messages": messages
    }

    with open(chat_path(title), "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def rename_chat(old_title: str, new_title: str):
    """
    Renames a chat.
    """

    old_file = chat_path(old_title)
    new_file = chat_path(new_title)

    old_file.rename(new_file)

    chat = load_chat(new_title)

    chat["title"] = new_title

    with open(new_file, "w", encoding="utf-8") as file:

        json.dump(
            chat,
            file,
            indent=4,
            ensure_ascii=False
        )


def delete_chat(title: str):
    """
    Deletes a chat.
    """

    file = chat_path(title)

    if file.exists():

        file.unlink()