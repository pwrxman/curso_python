import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    width = styles.Size.LARGE.value,
                    height = styles.Size.LARGE.value,
                    margin = styles.Size.MEDIUM.value,
                    alt = title    # Texto alternativo
                ),
                rx.vstack(
                    rx.text(title, style = styles.button_title_style),
                    rx.text(body, style = styles.button_body_style),
                    align_items = "start",
                    spacing = Size.SMALL.value,
                    padding_y = Size.SMALL.value,
                    padding_right = Size.SMALL.value
                ),
                width="100%"
            )
        ),
        href = url, 
        is_external = is_external,   # el valor asignado es el del parametro recibido como parametro de la funcion
        width = "100%"

    ) 
