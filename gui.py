import tkinter as tk


class ChatApp:

    def __init__(self, root):

        self.root = root

        self.root.title("AI Chatbot")

        self.root.geometry("1000x650")

        self.root.minsize(800, 500)


        self.create_layout()


    def create_layout(self):

        self.sidebar = tk.Frame(
            self.root,
            width=250
        )

        self.sidebar.pack(
            side="left",
            fill="y"
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
            font=("Arial", 18)
        )

        self.chat_title.pack(
            pady=15
        )


        self.messages = tk.Text(
            self.chat_area,
            state="disabled",
            wrap="word"
        )

        self.messages.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


        self.input_box = tk.Entry(
            self.chat_area
        )

        self.input_box.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 5),
            pady=15
        )


        self.send_button = tk.Button(
            self.chat_area,
            text="Send"
        )

        self.send_button.pack(
            side="right",
            padx=(5, 15),
            pady=15
        )


root = tk.Tk()

app = ChatApp(root)

root.mainloop()