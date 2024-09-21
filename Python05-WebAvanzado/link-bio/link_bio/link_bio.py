"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors import sponsors
import link_bio.styles.styles as styles


# class State(rx.State):    # En la 1a version, como la página es estática, esta sección no se necesita
 #     pass                           # Se ocupará en la 2a parte de este curso de python web


# Esta es la funcion principal
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG.value,
                padding = styles.Size.BIG.value
            )
        ),
        rx.center(footer())
    )
        



app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLE
)
app.add_page(
    index,
    title = "MoureDev | Te enseño programación y desarrollo de software",
    description = "Hola, Mi nombre es Brais Moure. Soy Ingeniero de software, desarrollador freelance ...",
    image = "./logo.png"
)
app._compile()






"""

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Hello Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
"""

