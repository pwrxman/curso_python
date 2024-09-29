

import reflex as rx
import link_bio.constants as const 
from link_bio.styles.styles import Size

from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor

def sponsors() -> rx.Component:
    return rx.vstack(
        title ("Colaboran"),
        rx.flex(              # Se cambia hstack por el diseño responsivo
            link_sponsor(
                "elgato.png",
                const.ELGATO_URL,
                "Logotipo de Elgato"        
            ),
            link_sponsor(
                "mvp.png",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"          
            ), 
            link_sponsor(
                "githubstar.png",
                const.GITHUB_STAR_URL,
                "Logotipo de GitHub Star"          
            ), 
            spacing = Size.BIG.value,
            #columns=[1, 3]
            flex_direction = ["column", "row"]      # ver la documentacion de reflex, seccion layouts para entebnder el significado
        ),
        width = "100%",
        align_items = "start"
    )
