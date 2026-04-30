# vmonsalve blog.

Blog con articulos de programacion y sistemas que valla aprendiendo.

## Stack

- Jekyll

## Requisitos

- Docker
- Docker Compose

```bash
docker compose up -d
```
Esto levanta el entorno de desarrollo del blog (Jekyll dentro de Docker).

## Visualizar el blog en local.

Para visualizar nuestro blog en local debemos ir a la siguiente url: 

```text
http://localhost:4000/
```

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
docker compose down
```

### Ver logs

```bash
docker compose logs -f
```
