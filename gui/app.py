import tkinter as tk

from gui.fonts import create_fonts
from gui.sidebar import Sidebar
from gui.chat_view import ChatView
from gui.dialogs import Dialogs


class ChatApp:

    def __init__(self, root):

        self.root = root

        self.root.title("AI Chatbot")
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)


        self.fonts = create_fonts()

        self.dialogs = Dialogs(
            root,
            self.fonts
        )


        self.current_chat = None


        self.create_layout()

        self.load_test_chats()


    def create_layout(self):

        self.sidebar = Sidebar(
            self.root,
            self.fonts,
            self.new_chat,
            self.rename_chat,
            self.delete_chat,
            self.show_help
        )

        self.sidebar.frame.pack(
            side="left",
            fill="y"
        )


        self.chat_view = ChatView(
            self.root,
            self.fonts,
            self.send_message
        )

        self.chat_view.frame.pack(
            side="right",
            fill="both",
            expand=True
        )


    def load_test_chats(self):

        chats = [
            "Python Learning",
            "Arduino Project",
            "Game Ideas"
        ]

        self.sidebar.set_chats(
            chats,
            self.open_chat
        )


    def open_chat(self, title):

        self.current_chat = title

        self.chat_view.set_title(
            title
        )

        self.chat_view.display_messages(
            []
        )


    def new_chat(self):

        title = self.dialogs.text_input(
            "New Chat",
            "Enter a chat name:"
        )

        if title:

            self.dialogs.message(
                f'Created "{title}"'
            )


    def rename_chat(self):

        if self.current_chat is None:

            self.dialogs.message(
                "Select a chat first."
            )

            return


        new_title = self.dialogs.text_input(
            "Rename Chat",
            "Enter the new name:"
        )

        if new_title:

            self.current_chat = new_title

            self.chat_view.set_title(
                new_title
            )


    def delete_chat(self):

        if self.current_chat is None:

            self.dialogs.message(
                "Select a chat first."
            )

            return


        confirmed = self.dialogs.confirm_delete(
            self.current_chat
        )

        if confirmed:

            self.current_chat = None

            self.chat_view.set_title(
                "Select a chat"
            )

            self.chat_view.display_messages(
                []
            )


    def send_message(self, message):

        if self.current_chat is None:

            return


        test_messages = [
            {
                "role": "user",
                "content": message
            },
            {
                "role": "assistant",
                "content": "The chat interface is working!"
            }
        ]

        self.chat_view.display_messages(
            test_messages
        )


    def show_help(self):

        self.dialogs.message(
            "Click a chat to open it.\n\n"
            "New Chat: Create a chat\n"
            "R Rename: Rename the selected chat\n"
            "Delete: Delete the selected chat\n"
            "Help: Show this message"
        )