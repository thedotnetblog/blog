---
title: "Azure Data Studio se retira: mueve tu flujo de Azure SQL a VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio se retiró el 6 de febrero de 2025, con soporte hasta el 28 de febrero de 2026. Aquí está la ruta de migración completa a VS Code con la extensión MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[Azure Data Studio se retiró el 6 de febrero de 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), con soporte hasta el 28 de febrero de 2026 — el reemplazo recomendado es VS Code con la extensión MSSQL.

## Qué instalar

Tres cosas para empezar:

- **Extensión MSSQL** — busca "SQL Server (mssql)" en el Marketplace de VS Code
- **Extensión SQL Database Projects** — esquema como código, validación de compilación, publicación guiada
- **.NET 8 SDK** — requerido por el sistema de compilación; el SDK faltante es el problema más común al primer uso

## Migrar tus conexiones y configuraciones de ADS

La extensión MSSQL incluye el **ADS Migration Toolkit**, que gestiona la migración única en un flujo guiado: conexiones guardadas, grupos de conexiones, configuraciones y atajos de teclado se importan automáticamente.

## Recuperar el músculo del F5

Los usuarios de ADS dependen de F5 para ejecutar consultas. Instala la extensión **MSSQL Database Management Keymap** para recuperar los atajos de teclado al estilo ADS, incluido F5.

## SQL Database Projects: esquema como código

Clic derecho en un proyecto → **Publicar** → configurar destino → revisar el script T-SQL generado → desplegar. La vista previa del script antes del despliegue es la característica clave de seguridad. Las plantillas de elementos generan esqueletos para tablas, procedimientos almacenados y vistas — el mismo flujo que SSDT.

Problema frecuente: una **incompatibilidad de plataforma de destino** en el archivo `.sqlproj` causará errores de compilación si el proyecto fue creado contra una versión diferente de SQL Server.

## Schema Compare y Schema Designer

La extensión también incluye **Schema Compare** (diferencia entre tu proyecto y la base de datos desplegada) y **Schema Designer** (edición visual del esquema sin escribir DDL a mano).

## Desarrolladores de Microsoft Fabric

La configuración es idéntica, pero comienza desde el **portal de Fabric** y conecta la base de datos a Git primero antes de abrirla en VS Code. Microsoft tiene una guía dedicada: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Conclusión

La migración es un flujo guiado de una sola vez, no una reconstrucción manual. Instala las tres herramientas, ejecuta el ADS Migration Toolkit, restaura tus atajos de teclado y estarás de vuelta a la normalidad en menos de 10 minutos.

Consulta el [artículo completo](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) para capturas de pantalla paso a paso y el tutorial específico de Fabric.

Este cambio ayuda cuando hay que equilibrar velocidad de entrega, consistencia de plataforma y gobernanza.

## Siguientes pasos practicos

1. Valida la funcionalidad en un piloto .NET pequeno con datos realistas.
2. Define observabilidad y un plan de rollback antes de escalar.
3. Documenta el patron para reutilizarlo en otros equipos.

## Fuente

- Articulo original: [https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)
