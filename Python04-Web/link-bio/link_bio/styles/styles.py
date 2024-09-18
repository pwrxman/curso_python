

import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

MAX_WIDTH = "560px"

# Para cargar las fuentes desde Google y puedan ser leidas por cualquier explorador
# y son jaladas desde el arranque de la app con el parametro stylesheets
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",   # css2 es para que se use la nueva version de google fonts
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
]

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
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "size": "5",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        # "display": "block",  # Se elimina para el diseño responsivo
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",            # Se añade para el diseño responsivo
        "text_align": "start",
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
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value
)

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    font_family = Font.TITLE.value,
    font_weight = FontWeight.MEDIUM.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    font_weight = FontWeight.LIGHT.value,
    color = TextColor.BODY.value
)



