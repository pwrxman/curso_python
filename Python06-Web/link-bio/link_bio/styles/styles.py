

import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

MAX_WIDTH = "560px"

# Sizes

class Size (Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "size": "5",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family = Font.LOGO.value,   # Es la fuente de la pàgina de MoureDev
    font_size = Size.LARGE.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    font_family = Font.TITLE.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value
)



