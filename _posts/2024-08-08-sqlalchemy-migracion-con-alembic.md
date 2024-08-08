---
layout: post
title: [Python] Migraciones con Alembic.
---

# Crear migraciones con Alembic.

Estoy desarrollando un proyecto personal con python, sqlalchemy y flask. Me vi en la necesidad de hacer la migracion de la base de datos, buscando la forma de hacer esto encontre una herramienta llamada Alambic.

Los pasos para hacer una migracion son los siguientes.

## Instalacion.

```
pip install alembic
```

## Inicializar alembic dentro del proyecto.

```
alembic init migrations

```

Esto nos va a gener un archivo alembic.ini, aqui configuraremos el conections string de nuesta base de datos, para ello debemos buscar y modificar la siguiente variable "sqlalchemy.url".

```
sqlalchemy.url = mysql+pymysql://user:password@host:port/dba_name
```

Colocando los datos que corresponden a tu base de datos, ya estamos listo para continuar.

## Crando una migración

Esto lo hacemos de la siguiente manera.

```
alembic revision --autogenerate -m "Initial migration"
```
En el texto que colocamos entre comillas podemos colocar de que trata nuestra migracion.

## Aplicando la migración

Para que nuestra migracion se vea reflejada en en nuestro motor de base de datos, usamos el siguiente comando.
```
alembic upgrade head
```

## Resumen

Esta herramienda es perfecta para no hacer cambios a mano en la base de datos. Corriendo algun riesgo.
