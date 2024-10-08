import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as constants
from link_bio.routes import Route
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text(
                    "Andrei ",
                    as_ = "span",
                    font_weight = "bold",
                    color = Color.PRIMARY.value
                ),
                rx.text(
                    "M",
                    as_ = "span",
                    font_weight = "bold",
                    color = Color.SECONDARY.value
                ),
                style = styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        float_button(
            icon = rx.image(src="/icons/donate.svg"),
            href = constants.COFFEE_URL
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index="999",
        top = "0"
    )