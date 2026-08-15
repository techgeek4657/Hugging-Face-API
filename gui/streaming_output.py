import threading


class StreamingOutput:

    def __init__(self, root, llm):

        self.root = root
        self.llm = llm

        self.running = False


    def start(
        self,
        messages,
        on_start,
        on_chunk,
        on_complete,
        on_error
    ):

        if self.running:
            return


        self.running = True


        thread = threading.Thread(
            target=self._run,
            args=(
                messages,
                on_start,
                on_chunk,
                on_complete,
                on_error
            ),
            daemon=True
        )


        thread.start()


    def _run(
        self,
        messages,
        on_start,
        on_chunk,
        on_complete,
        on_error
    ):

        try:

            self.root.after(
                0,
                on_start
            )


            full_response = ""


            for chunk in self.llm.stream(
                messages
            ):

                if chunk:

                    full_response += chunk


                    self.root.after(
                        0,
                        on_chunk,
                        chunk
                    )


            self.root.after(
                0,
                on_complete,
                full_response
            )


        except Exception as e:

            self.root.after(
                0,
                on_error,
                str(e)
            )


        finally:

            self.running = False