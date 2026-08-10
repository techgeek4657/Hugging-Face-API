import tkinter as tk
from tkinter import font

from services.llm_service import LLMService
from utils.chat_manager import ChatManager


class ChatApp:

    def __init__(self, root):

        self.root = root

        self.root.title("AI Chatbot")
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)

        self.llm = LLMService()
        self.chat_manager = ChatManager()

        self.current_chat = None
        self.messages = []

        self.setup_fonts()
        self.create_layout()
        self.refresh_chat_list()

        self.root.bind(
            "<Control-n>",
            lambda event: self.create_new_chat()
        )

        self.root.bind(
            "<Control-r>",
            lambda event: self.rename_current_chat()
        )

        self.root.bind(
            "<Delete>",
            lambda event: self.delete_current_chat()
        )

        self.root.bind(
            "<Control-h>",
            lambda event: self.show_help()
        )


    def setup_fonts(self):

        self.title_font = font.Font(
            family="Segoe UI",
            size=18,
            weight="bold"
        )

        self.heading_font = font.Font(
            family="Segoe UI",
            size=11,
            weight="bold"
        )

        self.normal_font = font.Font(
            family="Segoe UI",
            size=11
        )

        self.small_font = font.Font(
            family="Segoe UI",
            size=10
        )


    def create_layout(self):

        self.sidebar = tk.Frame(
            self.root,
            width=250
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)


        self.sidebar_title = tk.Label(
            self.sidebar,
            text="Chats",
            font=self.title_font
        )

        self.sidebar_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )


        self.chat_list = tk.Frame(
            self.sidebar
        )

        self.chat_list.pack(
            fill="both",
            expand=True,
            padx=10
        )


        self.new_chat_button = tk.Button(
            self.sidebar,
            text="+  New Chat",
            font=self.normal_font,
            command=self.create_new_chat
        )

        self.new_chat_button.pack(
            fill="x",
            padx=15,
            pady=(5, 5)
        )


        self.rename_button = tk.Button(
            self.sidebar,
            text="R  Rename",
            font=self.normal_font,
            command=self.rename_current_chat
        )

        self.rename_button.pack(
            fill="x",
            padx=15,
            pady=5
        )


        self.delete_button = tk.Button(
            self.sidebar,
            text="−  Delete",
            font=self.normal_font,
            command=self.delete_current_chat
        )

        self.delete_button.pack(
            fill="x",
            padx=15,
            pady=5
        )


        self.help_button = tk.Button(
            self.sidebar,
            text="?  Help",
            font=self.normal_font,
            command=self.show_help
        )

        self.help_button.pack(
            fill="x",
            padx=15,
            pady=(5, 15)
        )


        self.chat_area = tk.Frame(
            self.root
        )

        self.chat_area.pack(
            side="right",
            fill="both",
            expand=True
        )


        self.chat_title = tk.Label(
            self.chat_area,
            text="Select a chat",
            font=self.title_font
        )

        self.chat_title.pack(
            anchor="w",
            padx=20,
            pady=20
        )


        self.messages_box = tk.Text(
            self.chat_area,
            state="disabled",
            wrap="word",
            font=self.normal_font
        )

        self.messages_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 10)
        )


        self.input_frame = tk.Frame(
            self.chat_area
        )

        self.input_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )


        self.input_box = tk.Entry(
            self.input_frame,
            font=self.normal_font
        )

        self.input_box.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.input_box.bind(
            "<Return>",
            self.send_message
        )


        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            font=self.normal_font,
            command=self.send_message
        )

        self.send_button.pack(
            side="right",
            padx=(10, 0)
        )


    def refresh_chat_list(self):

        for widget in self.chat_list.winfo_children():

            widget.destroy()


        chats = self.chat_manager.list_chats()


        for title in chats:

            button = tk.Button(
                self.chat_list,
                text=title,
                font=self.normal_font,
                anchor="w",
                command=lambda t=title: self.open_chat(t)
            )

            button.pack(
                fill="x",
                pady=2
            )


    def open_chat(self, title):

        chat_data = self.chat_manager.open_chat(
            title
        )

        self.current_chat = title

        self.messages = chat_data["messages"]

        self.chat_title.config(
            text=title
        )

        self.display_messages()


    def display_messages(self):

        self.messages_box.config(
            state="normal"
        )

        self.messages_box.delete(
            "1.0",
            tk.END
        )


        for message in self.messages:

            role = message["role"]
            content = message["content"]


            if role == "user":

                self.messages_box.insert(
                    tk.END,
                    f"You:\n{content}\n\n"
                )

            elif role == "assistant":

                self.messages_box.insert(
                    tk.END,
                    f"AI:\n{content}\n\n"
                )


        self.messages_box.config(
            state="disabled"
        )

        self.messages_box.see(
            tk.END
        )


    def send_message(self, event=None):

        if self.current_chat is None:

            return


        prompt = self.input_box.get().strip()


        if not prompt:

            return


        if prompt.lower() == "/help":

            self.input_box.delete(
                0,
                tk.END
            )

            self.show_help()

            return


        self.input_box.delete(
            0,
            tk.END
        )


        self.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )


        self.display_messages()

        self.root.update()


        answer = self.llm.ask(
            self.messages
        )


        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        self.display_messages()


        self.chat_manager.save_chat(
            self.current_chat,
            self.messages
        )


    def create_new_chat(self):

        title = self.get_text_input(
            "New Chat",
            "Enter a name for the new chat:"
        )


        if not title:

            return


        title = title.strip()


        if not title:

            return


        if self.chat_manager.exists(title):

            self.show_message(
                "Chat already exists."
            )

            return


        self.chat_manager.create_chat(
            title
        )

        self.refresh_chat_list()

        self.open_chat(
            title
        )


    def rename_current_chat(self):

        if self.current_chat is None:

            self.show_message(
                "Select a chat first."
            )

            return


        old_title = self.current_chat


        new_title = self.get_text_input(
            "Rename Chat",
            "Enter the new chat name:"
        )


        if not new_title:

            return


        new_title = new_title.strip()


        if not new_title:

            return


        if self.chat_manager.exists(new_title):

            self.show_message(
                "A chat with that name already exists."
            )

            return


        self.chat_manager.rename_chat(
            old_title,
            new_title
        )


        self.current_chat = new_title

        self.chat_title.config(
            text=new_title
        )

        self.refresh_chat_list()


    def delete_current_chat(self):

        if self.current_chat is None:

            self.show_message(
                "Select a chat first."
            )

            return


        title = self.current_chat


        confirmed = self.confirm_delete(
            title
        )


        if not confirmed:

            return


        self.chat_manager.delete_chat(
            title
        )


        self.current_chat = None

        self.messages = []

        self.chat_title.config(
            text="Select a chat"
        )

        self.messages_box.config(
            state="normal"
        )

        self.messages_box.delete(
            "1.0",
            tk.END
        )

        self.messages_box.config(
            state="disabled"
        )

        self.refresh_chat_list()


    def show_help(self):

        help_window = tk.Toplevel(
            self.root
        )

        help_window.title(
            "Help"
        )

        help_window.geometry(
            "500x400"
        )

        help_window.transient(
            self.root
        )


        title = tk.Label(
            help_window,
            text="AI Chatbot Help",
            font=self.title_font
        )

        title.pack(
            pady=(20, 10)
        )


        help_text = tk.Label(
            help_window,
            text=(
                "Navigation\n\n"
                "Click a chat to open it.\n\n"
                "Ctrl + N    New chat\n"
                "Ctrl + R    Rename chat\n"
                "Delete     Delete selected chat\n"
                "Ctrl + H    Open help\n"
                "Enter      Send message\n\n"
                "You can also type /help in the chat."
            ),
            font=self.normal_font,
            justify="left"
        )

        help_text.pack(
            anchor="w",
            padx=40,
            pady=20
        )


        close_button = tk.Button(
            help_window,
            text="Close",
            font=self.normal_font,
            command=help_window.destroy
        )

        close_button.pack(
            pady=10
        )


    def get_text_input(self, title, prompt):

        window = tk.Toplevel(
            self.root
        )

        window.title(title)

        window.geometry(
            "400x150"
        )

        window.transient(
            self.root
        )

        window.grab_set()


        label = tk.Label(
            window,
            text=prompt,
            font=self.normal_font
        )

        label.pack(
            pady=(20, 5)
        )


        entry = tk.Entry(
            window,
            font=self.normal_font
        )

        entry.pack(
            fill="x",
            padx=30
        )

        entry.focus()


        result = []


        def submit():

            result.append(
                entry.get()
            )

            window.destroy()


        button = tk.Button(
            window,
            text="OK",
            font=self.normal_font,
            command=submit
        )

        button.pack(
            pady=15
        )


        window.bind(
            "<Return>",
            lambda event: submit()
        )


        self.root.wait_window(
            window
        )


        if result:

            return result[0]

        return None


    def show_message(self, message):

        window = tk.Toplevel(
            self.root
        )

        window.title("AI Chatbot")

        window.geometry(
            "350x130"
        )

        window.transient(
            self.root
        )


        label = tk.Label(
            window,
            text=message,
            font=self.normal_font
        )

        label.pack(
            pady=25
        )


        button = tk.Button(
            window,
            text="OK",
            font=self.normal_font,
            command=window.destroy
        )

        button.pack()


    def confirm_delete(self, title):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Delete Chat"
        )

        window.geometry(
            "400x150"
        )

        window.transient(
            self.root
        )

        window.grab_set()


        label = tk.Label(
            window,
            text=f'Delete "{title}"?',
            font=self.normal_font
        )

        label.pack(
            pady=20
        )


        result = []


        button_frame = tk.Frame(
            window
        )

        button_frame.pack()


        def confirm():

            result.append(True)

            window.destroy()


        def cancel():

            result.append(False)

            window.destroy()


        tk.Button(
            button_frame,
            text="Delete",
            font=self.normal_font,
            command=confirm
        ).pack(
            side="left",
            padx=10
        )


        tk.Button(
            button_frame,
            text="Cancel",
            font=self.normal_font,
            command=cancel
        ).pack(
            side="left",
            padx=10
        )


        self.root.wait_window(
            window
        )


        return result[0] if result else False


root = tk.Tk()

app = ChatApp(root)

root.mainloop()