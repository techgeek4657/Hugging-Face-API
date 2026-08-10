import tkinter as tk


class Dialogs:

    def __init__(self, root, fonts):

        self.root = root
        self.fonts = fonts


    def text_input(self, title, prompt):

        window = tk.Toplevel(
            self.root
        )

        window.title(title)
        window.geometry("400x150")

        window.transient(
            self.root
        )

        window.grab_set()


        label = tk.Label(
            window,
            text=prompt,
            font=self.fonts["normal"]
        )

        label.pack(
            pady=(20, 5)
        )


        entry = tk.Entry(
            window,
            font=self.fonts["normal"]
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
            font=self.fonts["normal"],
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


    def message(self, message):

        window = tk.Toplevel(
            self.root
        )

        window.title("AI Chatbot")
        window.geometry("350x130")

        window.transient(
            self.root
        )


        label = tk.Label(
            window,
            text=message,
            font=self.fonts["normal"]
        )

        label.pack(
            pady=25
        )


        button = tk.Button(
            window,
            text="OK",
            font=self.fonts["normal"],
            command=window.destroy
        )

        button.pack()


    def confirm_delete(self, title):

        window = tk.Toplevel(
            self.root
        )

        window.title("Delete Chat")
        window.geometry("400x150")

        window.transient(
            self.root
        )

        window.grab_set()


        label = tk.Label(
            window,
            text=f'Delete "{title}"?',
            font=self.fonts["normal"]
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
            font=self.fonts["normal"],
            command=confirm
        ).pack(
            side="left",
            padx=10
        )


        tk.Button(
            button_frame,
            text="Cancel",
            font=self.fonts["normal"],
            command=cancel
        ).pack(
            side="left",
            padx=10
        )


        self.root.wait_window(
            window
        )


        return result[0] if result else False