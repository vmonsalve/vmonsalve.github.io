---
layout: post
title: Direcciones explicitas
date: 2026-02-17
categories: vicente
---

# Direcciones explicitas

**Objetivo:** Entender donde vive cada cosa en memoria.

# Código

```c
#include <stdio.h>

int main() {
    char a[] = "Hola, memoria";
    char *p = "Hola, memoria";

    printf("&a = %p\n", &a);
    printf("&p = %p\n", &p);
    printf("p  = %p\n", p);

    return 0;
}
```

# Procedimiento

## Creación y compilación.

Creamos nuestro archivo con touch, en mi caso lo cree con el nombre ejercicio01.c

```bash
touch ejercicio01.c
```

Luego con nvim abrimos el archivo

```bash
nvim ejercicio01.c
```

Copiamos el código de arriba, presionamos la tecla "esc" luego " shift + ." en la parte inferior izquierda nos aparecerán dos puntitos que es el modo comando, presionamos la tecla "w" luego "enter" y podremos guardar nuestro archivo.

Para compilar nuestro archivo sin salir de nvim podemos hacerlo de siguiente forma: nos aseguramos de no estar en ningún modo presionando "esc", luego las teclas  "shift + . ", para entrar en modo comando y escribimos la siguiente linea

```bash
!gcc -g ejercicio01.c -o ejercicio01
```

Con esto compilamos el programa e incluimos la información necesaria para poder depurarlo con GDB.

## Depurando el código con gdb.

Para comenzar a depurar con gdb debemos hacerlo la siguiente manera

```bash
gdb ./ejercicio01
```

con esto entraamos a la teminal interactiva de gdb deberiamos ver algo asi

```text
Reading symbols from ./ejercicio01...
```

Ahora debemos poner un breakpoint en el main

```text
break main
```
 Al ejecutar la sentencia nos devolvera el siguiente mensaje indicado que el punto ruptura que fue seleccionado
 
 ```text
 Breakpoint 1, main () at /home/student/workspace/chapter01/ejercicios/ejercicio01/ejercicio01.c:4

4 char a[] = "Hola, memoria";
 ```

Para avanzar debemos continuar con la ejecucion del programa 

```text
run
```

Del cual obtendremos la siguente salida

```text
Starting program: /home/student/workspace/chapter01/ejercicios/ejercicio01/ejercicio01

warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
```

En este punto ya podemos ver como se comportan las variables dentro del stack. Nuestro siguiente ejercicio sera ver que contienen con print

```text
print &a
print &p
print p
```

La salida que nos devuelve cada uno de los print son las siguientes, tambien iremos revisando que significa cada una.

```text
$1 = (char (*)[14]) 0x7ffc195fbae2}
$2 = (char **) 0x7ffc195fbad8
$3 = 0x7824e6a2b5c0 <dl_main> "Uf\017\357\300H\211\345AWI\211\377AVAUATSH\201\354x\002"
```

De acuerdo al código fuente expuesto podemos darnos cuenta que tenemos dos tipos de variable.

| Variable                    | Descripcion                              |
| --------------------------- | ---------------------------------------- |
| char a[] = "Hola, memoria"; | arreglo en el stack                      |
| char *p = "Hola, memoria";  | puntero en el stack que apunta a .rodata |
|                             |                                          |

Con esto en mente podemos explicar los diferentes comandos print

| Comando  | Que imprime                       |
| -------- | --------------------------------- |
| print &a | Dirección del arreglo en el stack |
| print &p | Dirección del puntero en el stack |
| print p  | Dirección a la que apunta p       |

Con respecto a la salida de print p

```text
$3 = 0x7824e6a2b5c0 <dl_main> "Uf\017\357\300H\211\345AWI\211\377AVAUATSH\201\354x\002"
```

Debemos mencionar que GDB intenta asociar direcciones con símbolos conocidos del binario o librerías cargadas. Cuando la dirección cae dentro de un segmento compartido con otros símbolos, GDB muestra el símbolo más cercano.

Si quieres probar esto en un entorno controlado aqui tienes este lab completo

[The Art of exploitation](https://github.com/vmonsalve/the-art-of-exploitation-lab-es)

