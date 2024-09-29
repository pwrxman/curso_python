import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png", 
            height = Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt="Logotipo de MoureDev. Una \"eme\" entre llaves."
        ),
        rx.link(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.text(
                    "MoureDev by Brais Moure",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v4.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        align = "center",
        margin_bottom = Size.BIG.value,
        padding_bottom = Size.VERY_BIG.value,
        padding_x = Size.BIG.value,
        spacing=Size.ZERO.value,
        color = TextColor.FOOTER.value
        
    )