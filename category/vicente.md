---
layout: default
title: Textos de Vicente
permalink: /Vicente/
---

# ✒️ Textos de Vicente
Diario de un dev.
---

{% for post in site.categories.vicente %}
  <article>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <hr>
  </article>
{% endfor %}