import tkinter as tk

from gui.theme import Theme


class ChatView:

    def __init__(self, parent, fonts, send_callback):

        self.parent = parent
        self.fonts = fonts
        self.send_callback = send_callback

        self.dark_mode = False

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
            padx=24,
            pady=(20, 14)
        )


        self.title_separator = tk.Frame(
            self.frame,
            height=1
        )

        self.title_separator.pack(
            fill="x",
            padx=20
        )


        self.messages_container = tk.Frame(
            self.frame
        )

        self.messages_container.pack(
            fill="both",
            expand=True
        )


        self.messages_canvas = tk.Canvas(
            self.messages_container,
            highlightthickness=0
        )

        self.scrollbar = tk.Scrollbar(
            self.messages_container,
            orient="vertical",
            command=self.messages_canvas.yview
        )

        self.messages_canvas.configure(
            yscrollcommand=self.scrollbar.set
        )


        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.messages_canvas.pack(
            side="left",
            fill="both",
            expand=True
        )


        self.messages_frame = tk.Frame(
            self.messages_canvas
        )


        self.canvas_window = self.messages_canvas.create_window(
            (0, 0),
            window=self.messages_frame,
            anchor="nw"
        )


        self.messages_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        self.messages_canvas.bind(
            "<Configure>",
            self.resize_message_frame
        )


        self.input_separator = tk.Frame(
            self.frame,
            height=1
        )

        self.input_separator.pack(
            fill="x",
            padx=20
        )


        self.input_frame = tk.Frame(
            self.frame
        )

        self.input_frame.pack(
            fill="x",
            padx=20,
            pady=16
        )


        self.input_box = tk.Entry(
            self.input_frame,
            font=self.fonts["normal"],
            relief="flat",
            bd=0
        )

        self.input_box.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=8,
            padx=(0, 10)
        )

        self.input_box.bind(
            "<Return>",
            self.send_message
        )


        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            font=self.fonts["normal"],
            relief="flat",
            bd=0,
            padx=18,
            pady=8,
            cursor="hand2",
            command=self.send_message
        )

        self.send_button.pack(
            side="right"
        )


    def update_scroll_region(self, event=None):

        self.messages_canvas.configure(
            scrollregion=self.messages_canvas.bbox("all")
        )


    def resize_message_frame(self, event):

        self.messages_canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )


        self.update_message_wraps(
            event.width
        )


    def update_message_wraps(self, width):

        wrap_width = max(
            250,
            int(width * 0.72)
        )


        for widget in self.messages_frame.winfo_children():

            if hasattr(widget, "message_label"):

                widget.message_label.configure(
                    wraplength=wrap_width
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

        for widget in self.messages_frame.winfo_children():

            widget.destroy()


        for message in messages:

            self.add_message(
                message["role"],
                message["content"]
            )


        self.messages_frame.update_idletasks()

        self.messages_canvas.yview_moveto(
            1
        )


    def add_message(self, role, content):

        outer_frame = tk.Frame(
            self.messages_frame
        )

        outer_frame.pack(
            fill="x",
            padx=24,
            pady=7
        )


        wrap_width = max(
            250,
            int(
                self.messages_canvas.winfo_width() * 0.72
            )
        )


        if role == "user":

            bubble = tk.Label(
                outer_frame,
                text=content,
                font=self.fonts["normal"],
                justify="left",
                anchor="w",
                wraplength=wrap_width,
                padx=14,
                pady=9,
                relief="flat",
                bd=0
            )

            bubble.pack(
                side="right",
                anchor="e"
            )


            outer_frame.message_label = bubble


        else:

            message = tk.Label(
                outer_frame,
                text=content,
                font=self.fonts["normal"],
                justify="left",
                anchor="w",
                wraplength=wrap_width,
                padx=2,
                pady=5
            )

            message.pack(
                side="left",
                anchor="w"
            )


            outer_frame.message_label = message


        self.apply_message_theme(
            outer_frame,
            role
        )


    def apply_message_theme(self, outer_frame, role):

        colors = Theme.get(
            self.dark_mode
        )


        outer_frame.configure(
            bg=colors["background"]
        )


        bubble = outer_frame.message_label


        if role == "user":

            bubble.configure(
                bg=colors["user_bubble"],
                fg=colors["user_text"]
            )

        else:

            bubble.configure(
                bg=colors["background"],
                fg=colors["text"]
            )


    def set_dark_mode(self, dark_mode):

        self.dark_mode = dark_mode

        colors = Theme.get(
            dark_mode
        )


        self.frame.configure(
            bg=colors["background"]
        )

        self.chat_title.configure(
            bg=colors["background"],
            fg=colors["text"]
        )

        self.title_separator.configure(
            bg=colors["border"]
        )

        self.messages_container.configure(
            bg=colors["background"]
        )

        self.messages_canvas.configure(
            bg=colors["background"]
        )

        self.messages_frame.configure(
            bg=colors["background"]
        )

        self.input_separator.configure(
            bg=colors["border"]
        )

        self.input_frame.configure(
            bg=colors["background"]
        )

        self.input_box.configure(
            bg=colors["input"],
            fg=colors["text"],
            insertbackground=colors["text"]
        )

        self.send_button.configure(
            bg=colors["button"],
            fg=colors["text"],
            activebackground=colors["button_hover"],
            activeforeground=colors["text"]
        )


        for widget in self.messages_frame.winfo_children():

            if hasattr(widget, "message_label"):

                role = (
                    "user"
                    if widget.message_label.cget("bg")
                    in (
                        Theme.LIGHT["user_bubble"],
                        Theme.DARK["user_bubble"]
                    )
                    else "assistant"
                )

                self.apply_message_theme(
                    widget,
                    role
                )
    def start_streaming_message(self):

        self.streaming_frame = tk.Frame(
            self.messages_frame
        )

        self.streaming_frame.pack(
            fill="x",
            padx=24,
            pady=7
        )


        wrap_width = max(
            250,
            int(
                self.messages_canvas.winfo_width() * 0.72
            )
        )


        self.streaming_label = tk.Label(
            self.streaming_frame,
            text="",
            font=self.fonts["normal"],
            justify="left",
            anchor="w",
            wraplength=wrap_width,
            padx=2,
            pady=5
        )


        self.streaming_label.pack(
            side="left",
            anchor="w"
        )


        self.streaming_frame.message_label = (
            self.streaming_label
        )


        self.apply_message_theme(
            self.streaming_frame,
            "assistant"
        )


        self.messages_frame.update_idletasks()

        self.messages_canvas.yview_moveto(
            1
        )


    def append_streaming_text(self, text):

        if not hasattr(
            self,
            "streaming_label"
        ):

            return


        current = self.streaming_label.cget(
            "text"
        )


        self.streaming_label.config(
            text=current + text
        )


        self.messages_frame.update_idletasks()

        self.messages_canvas.configure(
            scrollregion=self.messages_canvas.bbox("all")
        )

        self.messages_canvas.yview_moveto(
            1
        )


    def finish_streaming_message(self):

        if hasattr(
            self,
            "streaming_label"
        ):

            del self.streaming_label


        if hasattr(
            self,
            "streaming_frame"
        ):

            del self.streaming_frame