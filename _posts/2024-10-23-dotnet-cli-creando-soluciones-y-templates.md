---
layout: post
title: Dotnet-cli creando soluciones y templates
---

# Dotnet-cli creando soluciones y templates

Llevo un tiempo trabajando con .net en macos, al principio partí con visual studio. Manteniendo unos proyectos del trabajo, pero ahora definitivamente me cambien a visual studio code y la herramienta dotnet-cli.

Gracias a un curso que estoy siguiendo en la plataforma udemy e aprendido a crear soluciones de forma correcta.

En este caso vamos a crear una solucion, para una api.

## Creando una solución.

Para crear una solución simple con dotnet-cli debemos ejecutar el siguiente comando.

```Text
dotnet new sln
```

Este comando nos creara una archivo sln en el directorio donde estes posicionado.

## Creando una solución tipo webapi.

Para crear una solucion tipo webapi usamos el siguiente comando.

```Text
dotnet new webapi -controllers -n [NombreSolucion]
```

Desglosemos el comando para entender que es lo que hace.

1. dotnet new webapi

   
    1. dotnet new es el comando base para crear un nuevo proyecto. Permite especificar un template que define el tipo de proyecto a iniciar.

    2. webapi especifica que el template a utilizar es el de una API web. Este template configura automáticamente el proyecto con las dependencias y configuraciones necesarias para desarrollar un servicio RESTful usando ASP.NET Core.

2. -controllers
   
   1. Esta opción modifica cómo se generan los controladores dentro del proyecto. En versiones actuales de .NET (como .NET 5 y superiores), el uso de -controllers especifica que el proyecto no debe generar ningún controlador de ejemplo por defecto. Esto es útil si prefieres comenzar tu proyecto desde cero o tienes especificaciones particulares para tus controladores.
   
3. -n [NombreSolucion]
   
    1. -n o --name se utiliza para especificar el nombre que tendrá el proyecto y la solución (si se crea una nueva solución). Debes reemplazar [NombreSolucion] con el nombre deseado para tu proyecto.

## En resumen.

Con los comandos mencionados anteriormente podemos comenzar a crear soluciones y templates para nuestros proyectos.

