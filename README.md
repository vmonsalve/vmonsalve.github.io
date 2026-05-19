# vmonsalve blog

Blog con artículos de programación y sistemas que voy aprendiendo [https://vmonsalve.github.io/](https://vmonsalve.github.io/).

## Stack

- Jekyll

## Requisitos

- Docker
- Docker Compose

## Levantar entorno

```bash
docker compose -f Docker/docker-compose.yml up -d --build
```

Esto levanta el entorno de desarrollo del blog (Jekyll dentro de Docker).

## Ver blog en local

http://localhost:4000/

## Comandos útiles

### Limpiar build

```bash
docker exec -it blog bundle exec jekyll clean
```

### Construir sitio

```bash
docker exec -it blog bundle exec jekyll build
```

### Detener entorno

```bash
docker compose -f Docker/docker-compose.yml down
```

### Ver logs

```bash
docker compose logs -f
```

## Crear nueva entrada

Requiere Python instalado:

```bash
python crea_post.py
```

Se creará un archivo en `_posts` con el formato:

```
YYYY-MM-DD-titulo-del-post.md
```

## Filosofía

Este blog busca documentar aprendizaje real, debugging y construcción de sistemas, reduciendo fricción en el proceso.

