---
layout: post
title: Activar logs en gdb
categories: Vicente
---

Gdb trae su propio sistema de logs y lo podemos activar de la siguiente manera:

```text
set logging on
```

Esto crea un archivo llamado gdb.txt en el directorio donde lanzamos gdb, estoy guarda todo lo que se imprime en pantalla.

## Cambiar el nombre del archivo.

Para cambiar el nombre del archivo se hace de la siguiente manera

```text
set logging file compare.log
```

Para que nuestro gdb comience a guardar logs

```text
set logging on
```

Y para que deje de hacerlo

```text
set logging off
```

## Modo Append

Esto sirve para sesiones largas

```gdb
set logging overwrite off
```

Hace que nuestro archivo de logs no se sobre escriba.

## Flujo real 

```text
set logging file compare.log
set logging overwrite off
set logging on

break main
run
info registers
x/16x $rsp

bt

set logging off
```

## Ejemplo real de un log

```text
Breakpoint 1 at 0x1168: file compare.c, line 7.
Starting program: /home/student/workspace/chapter01/compare 
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, main () at compare.c:7
7           printf("a: %s\n", a);
Stack level 0, frame at 0x7ffc8a3390c0:
 rip = 0x570f3c46d168 in main (compare.c:7); saved rip = 0x7009151c5ca8
 source language c.
 Arglist at 0x7ffc8a3390b0, args: 
 Locals at 0x7ffc8a3390b0, Previous frame's sp is 0x7ffc8a3390c0
 Saved registers:
  rbp at 0x7ffc8a3390b0, rip at 0x7ffc8a3390b8
8           printf("p: %s\n", p);
10          return 0;
a = "Hola, memoria"
p = 0x570f3c46e004 "Hola, memoria"
```

## Truco avanzado

Se puede activar y desactivar los logs en caliente

```text
set logging on
x/32gx $rsp
set logging off
```

