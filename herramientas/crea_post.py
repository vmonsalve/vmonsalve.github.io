import datetime
import os
import unicodedata
import re

def slugify(title):
    # Elimina acentos/tildes
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('utf-8')
    # Reemplaza cualquier caracter no alfanumérico por guion
    title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    # Reemplaza espacios y múltiple guiones por uno solo
    return re.sub(r'[-\s]+', '-', title)

def create_and_move_jekyll_post():
    title = input("Ingresa el título del post: ").strip()

    date = datetime.datetime.now().date()
    title_slug = slugify(title)
    filename = f"{date}-{title_slug}.md"

    content = f"""---
layout: post
title: {title}
---

# {title}

Contenido del post...
"""

    if not os.path.exists('_posts'):
        os.makedirs('_posts')

    post_path = os.path.join('_posts', filename)
    with open(post_path, 'w') as file:
        file.write(content)

    print(f"Archivo '{post_path}' creado con éxito en el directorio '_posts'.")

# Llamar a la función
if __name__ == "__main__":
    create_and_move_jekyll_post()