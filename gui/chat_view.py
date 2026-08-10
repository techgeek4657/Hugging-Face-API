import tkinter as tk


class ChatView:

    def __init__(self, parent, fonts, send_callback):

        self.parent = parent
        self.fonts = fonts
        self.send_callback = send_callback

        self.frame = tk.Frame(parent)

        self.create_widgets()


    def create_widgets(self):

        self.chat_title = tk.Label(
            self.frame,
            text="Select a chat",
            font=self.fonts["title"]
        )

        self.chat_title.pack(
            anchor="w",
            padx=20,
            pady=20
        )


        self.messages_box = tk.Text(
            self.frame,
            state="disabled",
            wrap="word",
            font=self.fonts["normal"]
        )

        self.messages_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 10)
        )


        self.input_frame = tk.Frame(
            self.frame
        )

        self.input_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )


        self.input_box = tk.Entry(
            self.input_frame,
            font=self.fonts["normal"]
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
            font=self.fonts["normal"],
            command=self.send_message
        )

        self.send_button.pack(
            side="right",
            padx=(10, 0)
        )


    def send_message(self, event=None):

        prompt = self.input_box.get().strip()

        if not prompt:
            return

        self.input_box.delete(
            0,
            tk.END
        )

        self.send_callback(prompt)


    def set_title(self, title):

        self.chat_title.config(
            text=title
        )


    def display_messages(self, messages):

        self.messages_box.config(
            state="normal"
        )

        self.messages_box.delete(
            "1.0",
            tk.END
        )


        for message in messages:

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