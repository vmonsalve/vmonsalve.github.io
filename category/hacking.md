---
layout: default
title: Hacking
permalink: /hacking/
---

{% for post in site.categories.hacking %}
  <article>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <p>{{ post.excerpt }}</p>
    <hr>
  </article>
{% endfor %}