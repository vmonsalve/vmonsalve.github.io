---
layout: post
title: Capitulo 01 - Memoria en C y Observación
categories: vicente
---

## Comenzando.

Para comenzar con el libro The Art of Exploitation, construimos el siguiente programa en C:

```c
#include <stdio.h>

int main() {
    char a[] = "Hola, memoria";
    char *p = "Hola, memoria";

    printf("a: %s\n", a);
    printf("p: %s\n", p);

    return 0;
}
```

Lo guardamos como compare.c.

## Compilando

Al compilar el archivo .c a binario debemos hacerlo con el flag -g para que **le diga al compilador que incluya información de depuración** en el binario:

> **mapas entre el código fuente y el binario final**

Es decir que incluya:

- nombres de funciones (main, etc.)
- nombres de variables (a, p)
- tipos (char[], char * *)
- líneas de código ↔ direcciones de memoria
- estructura de stack frames
- información de scopes (dónde existe cada variable)

comando

```bash
gcc -g compare.c -o compare
```

Al hacerlo de esta forma podremos debuguear de mejor manera nuestro binario.

## Depurando

Para comenzar a entender como depurar algoritmos en c lo haremos con la herramienta gdb.

```bash
gdb ./comprare
```

Al compilar con el flag -g deberíamos ver el siguiente mensaje dentro del texto de inicio de gdb

```text
Reading symbols from./compare...
```
Con lo cual podremos hacer cosas como esta:

```text
break compare.c:7
```
Que hace esto?
Le indicamos a gdb que ponga un punto de interrupción del flujo del algoritmo en la linea 7. 

Al hacer 

```text
run
```
la ejecución se parará en la linea 7 y nos mostrara este mensaje en pantalla

```text
Starting program: /home/student/workspace/chapter01/compare
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, main () at compare.c:7
7	    printf("a: %s\n", a);
```

Siguiente misión decirle a gdb que nos muestre el frame actual del stack

### info frame

```text
info frame
```

Nos devuelve el siguente mensaje

```text
tack level 0, frame at 0x7ffc8a3390c0:
 rip = 0x570f3c46d168 in main (compare.c:7); saved rip = 0x7009151c5ca8
 source language c.
 Arglist at 0x7ffc8a3390b0, args:
 Locals at 0x7ffc8a3390b0, Previous frame's sp is 0x7ffc8a3390c0
 Saved registers:
  rbp at 0x7ffc8a3390b0, rip at 0x7ffc8a3390b8
```
Este mensaje nos muestra no solo las variables locales, sino también la información necesaria para que el programa continúe ejecutándose correctamente al finalizar la función.

De esta forma, info frame nos permite observar no solo los datos, sino también el estado de ejecución del programa, lo que resulta clave para comprender cómo el flujo continúa correctamente entre funciones.

### Info local

```text
info locals
```

 Este comando nos muestra el contenido de las variables locales que existen en el **stack frame actual** …mientras la función está activa.

 En nuestro caso estamos en el _stack level 0_, correspondiente a la función main, y la salida es la siguiente:

```text
a = "Hola, memoria"
p = 0x570f3c46e004 "Hola, memoria"
```

La variable a es un arreglo de caracteres, por lo que **contiene directamente la cadena en memoria**.

En cambio, p es un puntero, y lo que almacena es **una dirección de memoria**, que apunta al lugar donde se encuentra la cadena "Hola, memoria".

Esta diferencia es fundamental para comprender cómo se organizan los datos en memoria y por qué ciertas operaciones pueden afectar regiones distintas del programa.

<img src="{{ site.baseurl }}/images/the_art_of_exploition.jpg" alt="the art of exploition" style="width: auto;"/>