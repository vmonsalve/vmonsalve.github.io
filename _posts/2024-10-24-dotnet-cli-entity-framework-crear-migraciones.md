---
layout: post
title: Dotnet-cli entity framework crear migraciones
---

# Dotnet-cli entity framework crear migraciones

Cuando creo modelos de bases de datos, suelo usar el metodo first to code.

## Paso uno instalar dependencias.

Para usar entity framework core debemos instalar los siguientes packetes a travez de la herramienta nuget.

```Bash
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
```

## Paso dos generar un modelo.

En este paso generaré un modelo para un blog, asi se puede ver la relacion entre las entidades.

### Entidad Post.

archivo Post.cs

```csharp
using System;
using System.Collections.Generic;

namespace BlogData.Models
{
    public class Post
    {
        public int PostId { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }
        public DateTime PublishDate { get; set; }
        public List<Comment> Comments { get; set; }
    }
}
```

### Entidad Comentarios.

archivo Comment.cs

```csharp
using System;

namespace BlogData.Models
{
    public class Comment
    {
        public int CommentId { get; set; }
        public string AuthorName { get; set; }
        public string Content { get; set; }
        public int PostId { get; set; }
        public Post Post { get; set; }
    }
}
```

## Paso tres Creación del contexto de la base de datos.

El contexto es un puente entre mis entidades y la base de datos.

```csharp
using Microsoft.EntityFrameworkCore;
using BlogData.Models;

public class BlogContext : DbContext
{
    public DbSet<Post> Posts { get; set; }
    public DbSet<Comment> Comments { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer(@"Server=(localdb)\mssqllocaldb;Database=BlogDB;Trusted_Connection=True;");
    }
}
```

En este caso creamos una clase llamada BlogContext que hereda de DbContext.
Definimos las propiedades, que corresponderan a las tablas en la base de datos con DbSet.

### Que nos permite hacer dbset.

1. Nos permite generar operaciones CRUD.
2. Nos permite trabajar con LINQ, permitiendonos escribir consultas complejas de manera eficiente y clara.
3. Nos permite hacer un seguimiento de cambios realizados en las entidades.
4. Nos permite hacer Lazy loading.

## Paso cuatro migraciones.

### Instalando la herramienta cli ef core.

```Bash
dotnet tool install --global dotnet-ef
```

### Generar migración.

```Bash
dotnet ef migrations add InitialCreate
```

### Aplicando migración.

```Bash
dotnet ef database update
```

En resumen, esta la forma de trabajar con first to code para trabajar con nuestra base de datos.