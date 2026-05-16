---
title: "Azure Data Studio s'ha retirat: mou el teu flux d'Azure SQL a VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio es va retirar el 6 de febrer de 2025, amb suport fins al 28 de febrer de 2026. Aquí tens el camí de migració complet a VS Code amb l'extensió MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[Azure Data Studio es va retirar el 6 de febrer de 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), amb suport fins al 28 de febrer de 2026 — el reemplaçament recomanat és VS Code amb l'extensió MSSQL.

## Què cal instal·lar

Tres coses per començar:

- **Extensió MSSQL** — cerca "SQL Server (mssql)" al Marketplace de VS Code
- **Extensió SQL Database Projects** — esquema com a codi, validació de compilació, publicació guiada
- **.NET 8 SDK** — requerit pel sistema de compilació; el SDK absent és el problema més habitual en el primer ús

## Migrar les connexions i la configuració d'ADS

L'extensió MSSQL inclou l'**ADS Migration Toolkit**, que gestiona la migració única en un flux guiat: les connexions desades, els grups de connexions, la configuració i els accessos de teclat s'importen automàticament.

## Recuperar el reflex del F5

Els usuaris d'ADS depenen del F5 per executar consultes. Instal·la l'extensió **MSSQL Database Management Keymap** per recuperar els accessos de teclat d'estil ADS, inclòs el F5.

## SQL Database Projects: esquema com a codi

Clic dret en un projecte → **Publica** → configura el destí → revisa el script T-SQL generat → desplega. La previsualització del script abans del desplegament és la característica de seguretat clau. Les plantilles d'elements generen esqueletes per a taules, procediments emmagatzemats i vistes — el mateix flux que SSDT.

Problema habitual: una **incompatibilitat de plataforma de destí** al fitxer `.sqlproj` causarà errors de compilació si el projecte es va crear per a una versió diferent de SQL Server.

## Schema Compare i Schema Designer

L'extensió també inclou **Schema Compare** (diferència entre el teu projecte i la base de dades desplegada) i **Schema Designer** (edició visual de l'esquema sense escriure DDL a mà).

## Desenvolupadors de Microsoft Fabric

La configuració és idèntica, però comença des del **portal de Fabric** i connecta la base de dades a Git primer abans d'obrir-la a VS Code. Microsoft té una guia dedicada: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Conclusió

La migració és un flux guiat d'una sola vegada, no una reconstrucció manual. Instal·la les tres eines, executa l'ADS Migration Toolkit, restaura els teus accessos de teclat i estaràs de tornada a la normalitat en menys de 10 minuts.

Consulta l'[article complet](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) per a captures de pantalla pas a pas i el tutorial específic de Fabric.
