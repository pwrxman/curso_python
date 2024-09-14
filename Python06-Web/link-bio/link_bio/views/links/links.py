import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", "Transmision sobre programación de Lunes a Viernes", const.TWITCH_URL),
        link_button("YouTube", "Tutoriales sobre desarrollo de software Semanales", const.YOUTUBE_URL),
        link_button("YouTube (Canal Secundario)", "Emisiones en Directo Destacados", const.YOUTUBE_SECONDARY_URL),
        link_button("Discord", "El Chat y los grupos de estudio de la Comunidad", const.DISCORD_URL),
        link_button("Retos de Programación", "Ejercicios Semanales para Practicar Lógica de Programación", const.CODE_CHALLENGES_URL),
        width = "100%",
        spacing = Size.MEDIUM.value
    ), rx.vstack(
        title("Recursos y Más"),
        link_button("Git y GitHub desde Cero", "Aquí Puedes Comprar Mi Libro en Formato Físico y Ebook", const.BOOK_URL),
        link_button("Libros Recomendados", "Mi Listado de Libros Sobre Programación, Ciencia y Tecnología", const.BOOKS_URL),
        link_button("Mi Set Up", "Listado con todos los elementos que uso en mi trabajo", const.SETUP_URL),
        link_button("MoureDev", "Mi Sitio Web", const.MOUREDEV_URL),
        link_button("Invítame a un Café", "¿Quieres Ayudarme a que siga creando contenido?", const.COFFEE_URL),
        title("Contacto"),
        link_button("My Public Inbox", "Respuesta Rápida y con Preferencia", const.MYPUBLICINBOX_URL),
        link_button("Email", const.EMAIL, f"mailto:{const.EMAIL}"),
        width = "100%",
        spacing = Size.MEDIUM.value
    )
    

    

