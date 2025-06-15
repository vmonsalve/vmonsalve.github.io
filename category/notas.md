---
layout: default
title: Notas del Desarrollador
permalink: /notas/
---

# 💻 Notas del Desarrollador

*Donde el pensamiento se convierte en código, y el código revela lo que pensamos.*

---

{% for post in site.categories.notas %}
  <article>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <p>{{ post.excerpt }}</p>
    <hr>
  </article>
{% endfor %}