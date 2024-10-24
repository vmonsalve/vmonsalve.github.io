---
layout: post
title: Docker crear un contenedor sqlserver
---

# Docker crear un contenedor sqlserver

Vamos a crear un contenedor sqlserver compatible macbook pro m1 pro.

```bash
    docker run --platform linux/amd64 \ 
        -e "ACCEPT_EULA=Y" \ 
        -e "MSSQL_SA_PASSWORD=[TuContrasena]" \ 
        -p 1433:1433 \ 
        --name [NombreDelContenedor] \ 
        -d mcr.microsoft.com/mssql/server:2022-latest
```
Una vez ejecutado el comando, revisamos que se haya creado correctamente.

```bash
    docker container ls
```
Ejecutado el comando nos mostrara algo similar a esto.

```bash
    b10abea098b7 mcr.microsoft.com/mssql/server:2022-latest "/opt/mssql/bin/perm…" 3 weeks ago    Up 3 days     0.0.0.0:1433->1433/tcp   [NombreDelContenedor]
```

En resumen con esto hemos levantado nuesto sqlserver en un contenedor.