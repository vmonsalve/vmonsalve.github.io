---
layout: default
title: Notas de un dev
permalink: /notas/
---

{% for post in site.categories.notas %}
  <article>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <hr>
  </article>
{% endfor %}