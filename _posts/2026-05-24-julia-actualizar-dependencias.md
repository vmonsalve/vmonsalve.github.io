---
layout: post
title: Julia Actualizar dependencias
date: 2026-05-25
categories: notas
---

Estaba desarrollando un `Toroide` con `Plot`, pero visualmente no me gusto como quedo, le pregunte a Ada, si habían otras opciones para hacerlo y me hablo de `GLMakie`.  Intente instalarlo pero desde el `Pkg`de `Julia` con:

```text
add GLMakie
```

y me salto el siguiente error:

```text
Resolving package versions...
ERROR: version 6.10.2+1 of package Qt6Base_jll is not available. Available versions: 6.0.3+0, 6.0.3+1, 6.3.0+0, 6.3.0+1, 6.4.1+0, 6.4.1+1, 6.4.2+0, 6.4.2+1, 6.4.2+2, 6.4.2+3, 6.5.2+0, 6.5.2+1, 6.5.2+2, 6.5.3+0, 6.5.3+1, 6.7.0+0, 6.7.0+1, 6.7.1+0, 6.7.1+1, 6.8.1+0, 6.8.2+0, 6.8.2+1, 6.8.2+2, 6.10.2+2
```

## Como actualizarlo.

Para actualizar Julia y nuestro sistema de paquetes para resolver ese error debemos seguir el siguiente procedimiento:

**Paso uno:**

```text
julia> using pkg
```

**Paso dos:**

```text
Pkg.Registry.update()
```

## Limpiamos dependencias viejas.

**Paso uno:**

```text
]
```

**Paso dos:**

```text
resolve
```

**Paso tres:**

```text
up
```

## Instalamos nuevamente `GLMakie`

```text
add GLMakie
```

## Verificamos la instalación.

```text
st
```

y deberíamos ver algo como esto

```text
Status `~/.julia/environments/v1.12/Project.toml`
  [e9467ef8] GLMakie v0.13.10
  [91a5bcdd] Plots v1.41.6
  [295af30f] Revise v3.14.3
```

Que nos indica que `GLMakie` fue instalado correctamente.