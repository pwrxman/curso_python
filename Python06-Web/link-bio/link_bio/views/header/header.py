

import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="And Medina", size="7",
                      fallback="AM", color_scheme="tomato"),
            rx.vstack(
                rx.heading("Hi 👋  My Name is Andrei"),
                rx.text(
                    "@amedina", 
                    size = "4", 
                    margin_top = Size.ZERO.value,
                    color = TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(const.GITHUB_URL),
                    link_icon(const.TWITTER_X_URL),
                    link_icon(const.INSTAGRAM_URL),
                    link_icon(const.TIKTOK_URL),
                    link_icon(const.SPOTIFY_URL),
                    link_icon(const.LINKEDIN_URL)
                ),
                align_items = "start",
                spacing = Size.DEFAULT.value
            )     
        ),
        rx.flex(
            info_text("13+", "Años de Experiencia"),
            rx.spacer(),
            info_text("100+", "Aplicaciones Creadas"),
            rx.spacer(),
            info_text("1M+", "Seguidores"),
            width = "100%"
        ),
        
        rx.text(
          f"""
          Soy ingeniero de software y actualmente trabajo como freelance
          full-stack developer iOS y Android.
          Además, creo contenido formativo sobre programación en redes.
          Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
          """,
          color = TextColor.BODY.value
          ),
          spacing = Size.BIG.value,
          align_items = "start"
    )

