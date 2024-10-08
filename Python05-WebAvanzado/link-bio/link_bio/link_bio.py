"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses




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



