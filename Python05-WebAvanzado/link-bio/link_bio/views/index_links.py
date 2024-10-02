import reflex as rx
from link_bio.routes import Route
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def index_links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Cursos Gratis",
            "Consulta mis tutoriales para aprender programación",
            "/icons/challenges.png",
            Route.COURSES.value,
            is_external=False
        ),
        link_button(
            "Twitch", 
            "Transmision sobre programación de Lunes a Viernes", 
            "/icons/twitch.svg", 
            const.TWITCH_URL
        ),
        link_button(
            "Discord", 
            "El Chat y los grupos de estudio de la Comunidad",
            "/icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "YouTube", 
            "Tutoriales sobre desarrollo de software Semanales",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "YouTube [Canal Secundario]", 
            "Emisiones en Directo Destacados", 
            "/icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        
        width = "100%",
        spacing = Size.MEDIUM.value
    ), rx.vstack(
        title("Recursos y Más"),
        link_button(
            "Git y GitHub desde Cero", 
            "Aquí Puedes Comprar Mi Libro en Formato Físico y Ebook", 
            "/icons/git.svg",
            const.BOOK_URL
        ),
        link_button(
            "Libros Recomendados",
            "Mi Listado de Libros Sobre Programación, Ciencia y Tecnología",
            "/icons/book.svg",
            const.BOOKS_URL
        ),
        link_button(
            "Mi Set Up",
            "Listado con todos los elementos que uso en mi trabajo",
            "/cons/setup.svg",
            const.SETUP_URL
        ),
        link_button(
            "MoureDev",
            "Mi Sitio Web",
            "/icons/logo.png",
            const.MOUREDEV_URL
        ),
        link_button(
            "Invítame a un Café", 
            "¿Quieres Ayudarme a que siga creando contenido?",
            "/icons/coffee.svg",
            const.COFFEE_URL
        ),
        title("Contacto"),
        link_button(
            "My Public Inbox",
            "Respuesta Rápida y con Preferencia",
            "/icons/twitch.svg",
            const.MYPUBLICINBOX_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width = "100%",
        spacing = Size.MEDIUM.value
    )
    

    

