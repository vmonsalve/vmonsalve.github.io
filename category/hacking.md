---
layout: default
title: Hacking
permalink: /hacking/
---

{% for post in site.categories.hacking %}
  <article>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <p><small>{{ post.date | date: "%d %B %Y" }}</small></p>
    <hr>
  </article>
{% endfor %}