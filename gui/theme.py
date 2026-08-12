class Theme:

    LIGHT = {
        "background": "#F7F7F8",
        "sidebar": "#EEEEF0",
        "surface": "#FFFFFF",
        "text": "#202123",
        "muted": "#6B6B6B",
        "border": "#D9D9DE",
        "user_bubble": "#E2E2E7",
        "user_text": "#202123",
        "button": "#E5E5EA",
        "button_hover": "#D6D6DC",
        "input": "#FFFFFF"
    }


    DARK = {
        "background": "#202123",
        "sidebar": "#17181A",
        "surface": "#202123",
        "text": "#F2F2F2",
        "muted": "#A0A0A5",
        "border": "#3A3B40",
        "user_bubble": "#3A3B40",
        "user_text": "#F2F2F2",
        "button": "#2D2F33",
        "button_hover": "#3A3C42",
        "input": "#2A2B2F"
    }


    @staticmethod
    def get(dark_mode):

        if dark_mode:
            return Theme.DARK

        return Theme.LIGHT