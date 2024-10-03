
# Este módulo se incorporó para mostrar la utilizacion de componentes react de la libreria https://ant.design

import reflex as rx
from link_bio.styles.colors import Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    #icon = rx.image("/icons/donate.svg")
    #href = "https://"
    icon: rx.Var[rx.el.Img]
    href: rx.Var[str]
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}

float_button = FloatButton.create



