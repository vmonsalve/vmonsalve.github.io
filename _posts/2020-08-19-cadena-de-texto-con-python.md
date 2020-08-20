---
layout: post
comments: true
title: "Cadenas de texto con python"
date: 2020-08-19 21:46
---

Revisaremos algunos metodos para trabajar con cadenas.

### Ejemplo:

cadena = "Hola Mundo"

### Método Lower.
Lower nos devuelve la cadena en minúsculas

```Python
cadena.lower()
```
Salida:

```
'hola mundo'
```

### Método upper.
Upper nos devuelve la cadena en mayúsculas.

```Python
cadena.upper()
```

salida:
```
'HOLA MUNDO'
```

### Método capitalize.
Capitalize devuelve la misma cadena, con el primer caracter
en mayuscula
```
cadena.capitalize()
```

Salida:
```
'Hola mundo'
```
### Métodp startswith.
Startswith devuelve True si la cadena enviada por parametro se encuentra al principio de la misma, de contrario devuelve False.

```
cadena.startswith("Hola")
```
Salida:
```
True
```

### Método endswith
Endswith busca la palabra al final de la cadena, si la palabra se encuentra
devuelve True, si no esta al final devuelve False.
```
cadena.endswith("Mundo")
```
Salida:
```
True
```

La lista se ira ampliando mientras aparezcan mas metodos.

{% include disqus.html %}