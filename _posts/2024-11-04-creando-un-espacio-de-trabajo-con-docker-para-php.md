---
layout: post
title: Creando un espacio de trabajo con docker para php
---

# Creando un espacio de trabajo con docker para php

Muchas veces me ah tocado trabajar con distintas version de php y symfony y la mejor de forma de trabajar sin ensuciar tanto nuestro sistema conversiones de php es usando un enterno docker.

## Creando el archivo Dockerfile.

```dockerfile
FROM php:8.1-apache

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    libicu-dev \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libzip-dev \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/* # Limpia la caché de apt

# Configurar y instalar extensiones de PHP
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) pdo pdo_mysql mysqli intl gd zip \
    && docker-php-ext-enable pdo_mysql

# Habilitar el módulo de Apache rewrite
RUN a2enmod rewrite

# Instalar Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Instalar Symfony CLI
ADD https://get.symfony.com/cli/installer /usr/local/bin/symfony-installer
RUN bash /usr/local/bin/symfony-installer \
    && mv /root/.symfony5/bin/symfony /usr/local/bin/symfony

# Configurar el directorio de trabajo
WORKDIR /var/www/html

# Exponer el puerto 80
EXPOSE 80
```

Una vez creado nuestro dockerfile debemos crear nuestro docker-compose.yml que se encargara de crear la imagen con el archivo que hicimos anteriormente y ademas le indicaremos la base de datos que vamos a usar y la red que veamos a crear.

## Archivo docker-compose.yml

```yml
version: '3.8'

services:
  symfony_app:
    build: .
    ports:
      - "80:80"
    volumes:
      - .:/var/www/html
    depends_on:
      - mysql
    networks:
      - symfony_network

  mysql:
    image: mysql:8.0
    platform: linux/arm64/v8
    environment:
      MYSQL_DATABASE: tu_nombre_de_la_base_de_datos
      MYSQL_USER: tu_user
      MYSQL_PASSWORD: tu_password
      MYSQL_ROOT_PASSWORD: tu_password_root
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"
    networks:
      - symfony_network

networks:
  symfony_network:
    name: symfonyapps
    driver: bridge

volumes:
  mysql_data:

```

Como podemos ver el primer contenedor que se crea es el de php, luego el de mysql y por ultimo la red.

Para saber que direccion ip se le asigno a nuestro contenedor debemos ejecutar el siguiente comando

```terminal
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nombre_contenedor
```

Esto nos devolvera lo siguiente, en mi caso esta ip.

```terminal
172.24.0.2
```

Espero que esto les sea de utilidad.