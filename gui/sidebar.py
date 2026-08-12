import tkinter as tk

from gui.theme import Theme


class Sidebar:

    def __init__(
        self,
        parent,
        fonts,
        new_chat_callback,
        rename_callback,
        delete_callback,
        help_callback,
        theme_callback
    ):

        self.parent = parent
        self.fonts = fonts

        self.new_chat_callback = new_chat_callback
        self.rename_callback = rename_callback
        self.delete_callback = delete_callback
        self.help_callback = help_callback
        self.theme_callback = theme_callback

        self.dark_mode = False

        self.frame = tk.Frame(
            parent,
            width=250
        )

        self.frame.pack_propagate(False)

        self.create_widgets()

        self.apply_theme()


    def create_widgets(self):

        self.title = tk.Label(
            self.frame,
            text="Chats",
            font=self.fonts["title"]
        )

        self.title.pack(
            anchor="w",
            padx=20,
            pady=(20, 12)
        )


        self.chat_separator = tk.Frame(
            self.frame,
            height=1
        )

        self.chat_separator.pack(
            fill="x",
            padx=15
        )


        self.chat_list = tk.Frame(
            self.frame
        )

        self.chat_list.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )


        self.action_separator = tk.Frame(
            self.frame,
            height=1
        )

        self.action_separator.pack(
            fill="x",
            padx=15,
            pady=(0, 10)
        )


        self.new_button = self.create_button(
            "New Chat",
            self.new_chat_callback
        )


        self.rename_button = self.create_button(
            "Rename",
            self.rename_callback
        )


        self.delete_button = self.create_button(
            "Delete",
            self.delete_callback
        )


        self.settings_separator = tk.Frame(
            self.frame,
            height=1
        )

        self.settings_separator.pack(
            fill="x",
            padx=15,
            pady=10
        )


        self.theme_button = self.create_button(
            "Dark Mode",
            self.theme_callback
        )


        self.help_button = self.create_button(
            "Help",
            self.help_callback
        )


        self.create_button(
            "Quit",
            self.parent.winfo_toplevel().destroy
        )


    def create_button(self, text, command):

        button = tk.Button(
            self.frame,
            text=text,
            font=self.fonts["normal"],
            relief="flat",
            bd=0,
            anchor="w",
            padx=15,
            pady=9,
            cursor="hand2",
            command=command
        )

        button.pack(
            fill="x",
            padx=15,
            pady=2
        )

        return button


    def set_chats(self, chats, open_callback):

        for widget in self.chat_list.winfo_children():

            widget.destroy()


        for title in chats:

            button = tk.Button(
                self.chat_list,
                text=title,
                font=self.fonts["normal"],
                relief="flat",
                bd=0,
                anchor="w",
                padx=10,
                pady=8,
                cursor="hand2",
                command=lambda t=title: open_callback(t)
            )

            button.pack(
                fill="x",
                pady=2
            )

            colors = Theme.get(
                self.dark_mode
            )

            button.configure(
                bg=colors["sidebar"],
                fg=colors["text"],
                activebackground=colors["button_hover"],
                activeforeground=colors["text"]
            )


    def set_dark_mode(self, dark_mode):

        self.dark_mode = dark_mode

        self.apply_theme()


    def apply_theme(self):

        colors = Theme.get(
            self.dark_mode
        )


        self.frame.configure(
            bg=colors["sidebar"]
        )

        self.title.configure(
            bg=colors["sidebar"],
            fg=colors["text"]
        )


        for separator in (
            self.chat_separator,
            self.action_separator,
            self.settings_separator
        ):

            separator.configure(
                bg=colors["border"]
            )


        for button in (
            self.new_button,
            self.rename_button,
            self.delete_button,
            self.theme_button,
            self.help_button
        ):

            button.configure(
                bg=colors["sidebar"],
                fg=colors["text"],
                activebackground=colors["button_hover"],
                activeforeground=colors["text"]
            )


        for widget in self.chat_list.winfo_children():

            widget.configure(
                bg=colors["sidebar"],
                fg=colors["text"],
                activebackground=colors["button_hover"],
                activeforeground=colors["text"]
            )