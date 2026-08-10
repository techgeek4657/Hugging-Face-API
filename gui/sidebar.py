import tkinter as tk


class Sidebar:

    def __init__(
        self,
        parent,
        fonts,
        new_chat_callback,
        rename_callback,
        delete_callback,
        help_callback
    ):

        self.parent = parent
        self.fonts = fonts

        self.new_chat_callback = new_chat_callback
        self.rename_callback = rename_callback
        self.delete_callback = delete_callback
        self.help_callback = help_callback

        self.frame = tk.Frame(
            parent,
            width=250
        )

        self.frame.pack_propagate(False)

        self.create_widgets()


    def create_widgets(self):

        self.title = tk.Label(
            self.frame,
            text="Chats",
            font=self.fonts["title"]
        )

        self.title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )


        self.chat_list = tk.Frame(
            self.frame
        )

        self.chat_list.pack(
            fill="both",
            expand=True,
            padx=10
        )


        self.new_button = tk.Button(
            self.frame,
            text="+  New Chat",
            font=self.fonts["normal"],
            command=self.new_chat_callback
        )

        self.new_button.pack(
            fill="x",
            padx=15,
            pady=5
        )


        self.rename_button = tk.Button(
            self.frame,
            text="R  Rename",
            font=self.fonts["normal"],
            command=self.rename_callback
        )

        self.rename_button.pack(
            fill="x",
            padx=15,
            pady=5
        )


        self.delete_button = tk.Button(
            self.frame,
            text="−  Delete",
            font=self.fonts["normal"],
            command=self.delete_callback
        )

        self.delete_button.pack(
            fill="x",
            padx=15,
            pady=5
        )


        self.help_button = tk.Button(
            self.frame,
            text="?  Help",
            font=self.fonts["normal"],
            command=self.help_callback
        )

        self.help_button.pack(
            fill="x",
            padx=15,
            pady=(5, 15)
        )


    def set_chats(self, chats, open_callback):

        for widget in self.chat_list.winfo_children():

            widget.destroy()


        for title in chats:

            button = tk.Button(
                self.chat_list,
                text=title,
                font=self.fonts["normal"],
                anchor="w",
                command=lambda t=title: open_callback(t)
            )

            button.pack(
                fill="x",
                pady=2
            )