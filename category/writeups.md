---
layout: default
title: Write up maquinas y crackmes
permalink: /writeups/
---

{% for post in site.categories.notas %}
  <article>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <hr>
  </article>
{% endfor %}