"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.links import links
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
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),   # GTAG es el tag asociado a Google Analytics
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)

title = "MoureDev | Te enseño programación y desarrollo de software"
description = "Hola, Mi nombre es Brais Moure. Soy Ingeniero de software, desarrollador freelance ..."
preview = "https://moure.dev/preview.jpg"


app.add_page(
    index,
    title=title,
    description=description,
    image = preview,
    meta=[
        {"name": "og:type",        "content": "website"},
        {"name": "og:title",       "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image",       "content": preview},
        {"name": "twitter:card",   "content": "summary_large_image"},
        {"name": "twitter:site",   "content": "@mouredev"}

    ]
)







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

