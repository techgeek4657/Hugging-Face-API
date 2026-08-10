from tkinter import font


def create_fonts():

    return {
        "title": font.Font(
            family="Segoe UI",
            size=18,
            weight="bold"
        ),

        "heading": font.Font(
            family="Segoe UI",
            size=11,
            weight="bold"
        ),

        "normal": font.Font(
            family="Segoe UI",
            size=11
        ),

        "small": font.Font(
            family="Segoe UI",
            size=10
        )
    }