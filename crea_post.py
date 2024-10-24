import datetime
import os

def create_and_move_jekyll_post():
    # Solicitar el título del post al usuario
    title = input("Ingresa el título del post: ")

    # Crear el nombre del archivo con la fecha actual y el título formateado
    date = datetime.datetime.now().date()
    title_slug = title.lower().replace(' ', '-')
    filename = f"{date}-{title_slug}.md"

    # Definir el contenido del archivo utilizando el título proporcionado
    content = f"""---
layout: post
title: {title}
---

# {title}

Contenido del post...
"""

    # Crear el archivo en el directorio actual
    with open(filename, 'w') as file:
        file.write(content)

    # Verificar si el directorio _posts existe, si no, crearlo
    if not os.path.exists('_posts'):
        os.makedirs('_posts')

    # Mover el archivo al directorio _posts
    os.rename(filename, os.path.join('_posts', filename))

    print(f"Archivo '{filename}' movido con éxito al directorio '_posts'.")

# Llamar a la función
if __name__ == "__main__":
    create_and_move_jekyll_post()
