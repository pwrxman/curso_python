

import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.constants as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src ="avatar.jpg",
                size="6",
                color = TextColor.BODY.value,
                bg = Color.CONTENT.value,
                padding = "2px",
                border = "8px",
                border_color = Color.PRIMARY.value
                # color_scheme="tomato"
            ),
            rx.vstack(
                rx.heading("Hi 👋  My Name is Andrei"),
                rx.text(
                    "@amedina", 
                    size = "4", 
                    margin_top = Size.ZERO.value,
                    color = TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("icons/github_gris.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "Linkedin"
                    )
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
          font_size = Size.MEDIUM.value,
          color = TextColor.BODY.value
          ),
          spacing = Size.BIG.value,
          align_items = "start"
    )

