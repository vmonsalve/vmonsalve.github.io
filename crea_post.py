import datetime
import os

def create_and_move_jekyll_post():
    title = input("Ingresa el título del post: ")

    date = datetime.datetime.now().date()
    title_slug = title.lower().replace(' ', '-')
    filename = f"{date}-{title_slug}.md"

    content = f"""---
layout: post
title: {title}
---

# {title}

Contenido del post...
"""

    with open(filename, 'w') as file:
        file.write(content)

    if not os.path.exists('_posts'):
        os.makedirs('_posts')

    os.rename(filename, os.path.join('_posts', filename))

    print(f"Archivo '{filename}' movido con éxito al directorio '_posts'.")

# Llamar a la función
if __name__ == "__main__":
    create_and_move_jekyll_post()
