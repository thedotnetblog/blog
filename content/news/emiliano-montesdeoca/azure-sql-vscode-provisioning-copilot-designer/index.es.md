---
title: "La extensión MSSQL para VS Code se está convirtiendo silenciosamente en una plataforma mucho más grande"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "La última actualización de la extensión MSSQL añade aprovisionamiento de Azure SQL, diseño de esquemas asistido por Copilot, Data API builder y notebooks. Lo interesante es cuánta parte del trabajo de bases de datos puede quedarse ahora dentro de VS Code."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Este artículo se tradujo automáticamente. Para ver la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

La extensión MSSQL para VS Code lleva creciendo desde hace tiempo, pero esta última actualización deja la dirección mucho más clara.

Ya no es solo «conéctate y ejecuta unas consultas».

Con el **aprovisionamiento de Azure SQL**, el **Schema Designer con Copilot**, los **SQL Notebooks** y **Data API builder** avanzando todos en una sola versión, la extensión se está convirtiendo en un entorno de trabajo mucho más completo para el desarrollo centrado en bases de datos.

## El gancho práctico es el aprovisionamiento directamente desde el editor

La publicación original dice que ahora puedes crear una base de datos en la nube totalmente administrada «directamente desde tu editor y sin coste» usando la capa gratuita.

Ese es el tipo de función que parece pequeña hasta que te das cuenta de cuánta fricción de configuración elimina.

Para muchos desarrolladores, la parte molesta de las pruebas intensivas en datos no es SQL en sí. Es la brecha de entorno entre:

- idea
- base de datos
- esquema
- API
- backend que se pueda probar

Si esa brecha se acorta dentro de una sola herramienta, todo el flujo de trabajo se vuelve más atractivo.

## Así se ve un inner loop más fuerte para el trabajo con datos

Lo que me gusta de esta versión es que mantiene más parte del flujo de trabajo de base de datos en un solo lugar:

- aprovisionar la base de datos
- diseñar el esquema
- revisar cambios
- generar scripts ORM
- exponer APIs
- probar endpoints
- documentar y consultar mediante notebooks

Esa es una historia mucho más convincente que tratar SQL como una herramienta lateral desconectada en la pila.

## El flujo de esquema asistido por Copilot es donde el valor de la IA se siente real

Las novedades del diseñador de esquemas son especialmente interesantes porque parecen encontrar un buen equilibrio.

El valor no es «la IA diseña tu modelo de datos y tú confías ciegamente».

El valor es:

- puntos de partida más rápidos
- revisión visual
- seguimiento de cambios
- salida orientada a migración
- controles explícitos de aceptar/deshacer

Ese es un flujo de trabajo de IA mucho más saludable que la generación automática completa sin camino de inspección.

Y en el trabajo de bases de datos, la revisabilidad importa mucho.

## Data API builder es un multiplicador silencioso

La otra característica que no ignoraría es la integración de Data API builder.

Si puedes pasar de esquema a:

- REST
- GraphQL
- endpoints MCP

dentro del mismo entorno, eso crea una ruta muy eficiente para prototipos de backend y herramientas internas.

Eso no reemplaza una ingeniería backend más profunda. Pero sí acorta el camino desde la idea de base de datos hasta una interfaz funcional.

## Mi lectura

Esta versión hace que la extensión MSSQL se sienta más como una pequeña plataforma dentro de VS Code que como un simple complemento.

Para desarrolladores que crean APIs, herramientas de datos, herramientas de administración o prototipos respaldados por SQL, eso es un cambio significativo.

Y si Microsoft sigue ajustando este ciclo, la extensión se volverá mucho más útil estratégicamente de lo que mucha gente todavía asume.

Publicación original: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)