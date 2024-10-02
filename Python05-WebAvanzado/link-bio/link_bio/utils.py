
import reflex as rx


# COMUN
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://moure.dev/preview.jpg"

_meta=[
    {"name": "og:type",        "content": "website"},
    {"name": "og:image",       "content": preview},
    {"name": "twitter:card",   "content": "summary_large_image"},
    {"name": "twitter:site",   "content": "@mouredev"}

]


# INDEX

index_title = "MoureDev | Te enseño programación y desarrollo de software"
index_description = "Hola, Mi nombre es Brais Moure. Soy Ingeniero de software, desarrollador freelance ..."
index_meta=[
    {"name": "og:title",       "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)


# CURSOS
courses_title = "MoureDev | Cursos Gratis"
courses_description = "Este es un listado de cursos gratis para aprender programacion. Python, SQL, Git..."
courses_meta=[
    {"name": "og:title",       "content": courses_title},
    {"name": "og:description", "content": courses_description}
]
courses_meta.extend(_meta)
