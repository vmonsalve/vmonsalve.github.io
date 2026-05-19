---
layout: post
title: Creando y optimizando un contenedor para este blog
date: 2026-05-03
categories: notas
---

# Creando y optimizando un contenedor para este blog

Hace años, que tenía ganas de hacer un blog técnico, ocupé múltiples plataformas, blogger, wordpress, tumblr, pero ninguna se adaptaba a lo que queria, hasta que un dia descubrí que podia crear un blog con github pages y jekyll.

Este blog ha pasado por varias fases, la primera directo en el host teniendo que instalar ruby y todo el ecosistema. Que pasaba con esto? que cada vez que cambiaba de sistema operativo, tenia problemas con la versión de ruby y sus dependencias. Solución? Dockerizar y aquí estamos con el entorno de mi blog totalmente dockerizado.

## Primera versión.

La primera versión de mi `Dockefile` y mi `docker-compose.yml`

```Dockerfile
FROM ruby:3.0

RUN apt-get update -qq && apt-get install -y build-essential

RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g yarn

WORKDIR /site

COPY Gemfile* /site/

RUN gem update --system 3.2.22 && gem install bundler

RUN bundle install

COPY . /site

EXPOSE 4000

CMD ["jekyll", "serve", "--host", "0.0.0.0"]
```
---

```yml
version: '3.8'
services:
  jekyll:
    image: bretfisher/jekyll-serve
    volumes:
      - .:/site
    ports:
      - "4000:4000"
    working_dir: /site
```

Problema que tiene esta configuración.


```text
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
blog-jekyll   latest    3e993ceca837   19 minutes ago   1.48GB
```

La cantidad de espacio brutal que ocupa.

## Arreglando el problema.

Para solucionar este problema lo primero que hice fue tocar el `Dockerfile`

```Dockerfile
FROM ruby:3.1-alpine

RUN apk add --no-cache \
    build-base \
    curl \
    nodejs \
    npm \
    linux-headers \
    libffi-dev

RUN npm install -g yarn

WORKDIR /site

COPY Gemfile Gemfile.lock ./

RUN bundle install

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
```

## Que cambios hicimos?