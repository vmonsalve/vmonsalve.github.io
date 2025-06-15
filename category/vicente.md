---
layout: default
title: Textos de Vicente
permalink: /vicente/
---

# ✒️ Textos de Vicente

*Reflexiones, anécdotas y pensamientos de un alma que observa, vive y cuestiona.*

---

{% for post in site.categories.vicente %}
  <article>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <p>{{ post.excerpt }}</p>
    <hr>
  </article>
{% endfor %}