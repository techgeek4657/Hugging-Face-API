import tkinter as tk
from services.llm_service import LLMService
from gui.fonts import create_fonts
from gui.sidebar import Sidebar
from gui.chat_view import ChatView
from gui.dialogs import Dialogs
from gui.streaming_output import StreamingOutput
from utils.chat_manager import ChatManager


class ChatApp:

    def __init__(self, root):

        self.root = root

        self.root.title("AI Chatbot")
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)

        self.fonts = create_fonts()

        self.chat_manager = ChatManager()

        self.llm = LLMService()
        self.streaming = StreamingOutput(
            self.root,
            self.llm
        )
        self.dialogs = Dialogs(
            root,
            self.fonts
        )

        self.current_chat = None
        self.messages = []

        self.dark_mode = False
        
        self.create_layout()

        self.refresh_chats()


    def create_layout(self):

        self.sidebar = Sidebar(
            self.root,
            self.fonts,
            self.new_chat,
            self.rename_chat,
            self.delete_chat,
            self.show_help,
            self.toggle_dark_mode
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

    def toggle_dark_mode(self):

        self.dark_mode = not getattr(
            self,
            "dark_mode",
            False
        )


        self.sidebar.set_dark_mode(
            self.dark_mode
        )

        self.chat_view.set_dark_mode(
            self.dark_mode
        )

    def refresh_chats(self):

        chats = self.chat_manager.list_chats()

        self.sidebar.set_chats(
            chats,
            self.open_chat
        )


    def open_chat(self, title):

        try:

            chat_data = self.chat_manager.open_chat(
                title
            )

        except FileNotFoundError:

            self.refresh_chats()

            self.dialogs.message(
                "That chat no longer exists."
            )

            return


        self.current_chat = title

        self.messages = chat_data["messages"]

        self.chat_view.set_title(
            title
        )

        self.chat_view.display_messages(
            self.messages
        )


    def new_chat(self):

        title = self.dialogs.text_input(
            "New Chat",
            "Enter a chat name:"
        )

        if not title:

            return


        title = title.strip()

        if not title:

            return


        if self.chat_manager.exists(title):

            self.dialogs.message(
                "A chat with that name already exists."
            )

            return


        self.chat_manager.create_chat(
            title
        )

        self.refresh_chats()

        self.open_chat(
            title
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

        if not new_title:

            return


        new_title = new_title.strip()

        if not new_title:

            return


        if new_title == self.current_chat:

            return


        if self.chat_manager.exists(new_title):

            self.dialogs.message(
                "A chat with that name already exists."
            )

            return


        old_title = self.current_chat


        self.chat_manager.rename_chat(
            old_title,
            new_title
        )


        self.current_chat = new_title

        self.refresh_chats()

        self.chat_view.set_title(
            new_title
        )


    def delete_chat(self):

        if self.current_chat is None:

            self.dialogs.message(
                "Select a chat first."
            )

            return


        title = self.current_chat


        confirmed = self.dialogs.confirm_delete(
            title
        )


        if not confirmed:

            return


        self.chat_manager.delete_chat(
            title
        )


        self.current_chat = None

        self.messages = []


        self.chat_view.set_title(
            "Select a chat"
        )

        self.chat_view.display_messages(
            [] 
        )


        self.refresh_chats()


    def send_message(self, message):

        if self.current_chat is None:

            return


        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )


        self.chat_view.display_messages(
            self.messages
        )


        self.chat_view.input_box.config(
            state="disabled"
        )


        self.chat_view.send_button.config(
            state="disabled"
        )


        self.streaming.start(

            self.messages,

            self.streaming_started,

            self.streaming_chunk,

            self.streaming_finished,

            self.streaming_error

        )
    def show_help(self):

        self.dialogs.message(
            "Click a chat to open it.\n\n"
            "New Chat: Create a chat\n"
            "R Rename: Rename the selected chat\n"
            "Delete: Delete the selected chat\n"
            "Help: Show this message"
        )

    def streaming_started(self):

        self.chat_view.start_streaming_message()

    


    def streaming_chunk(self, chunk):

            self.chat_view.append_streaming_text(
                chunk
            )


    def streaming_finished(self, answer):

            self.chat_view.finish_streaming_message()


            self.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )


            self.chat_view.display_messages(
                self.messages
            )


            self.chat_manager.save_chat(
                self.current_chat,
                self.messages
            )


            self.chat_view.input_box.config(
                state="normal"
            )


            self.chat_view.send_button.config(
                state="normal"
            )


            self.chat_view.input_box.focus()


    def streaming_error(self, error):

            self.chat_view.finish_streaming_message()


            self.messages.append(
                {
                    "role": "assistant",
                    "content": f"AI Error: {error}"
                }
            )


            self.chat_view.display_messages(
                self.messages
            )


            self.chat_view.input_box.config(
                state="normal"
            )


            self.chat_view.send_button.config(
                state="normal"
            )


            self.chat_view.input_box.focus()