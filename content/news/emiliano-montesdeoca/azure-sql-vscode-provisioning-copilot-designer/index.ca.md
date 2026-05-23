---
title: "L'extensió MSSQL de VS Code s'està convertint silenciosament en una plataforma molt més gran"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "L'última actualització de l'extensió MSSQL afegeix provisió d'Azure SQL, disseny d'esquemes assistit per Copilot, Data API builder i notebooks. La part interessant és quanta feina de base de dades pot quedar ara dins de VS Code."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Aquest article s'ha traduït automàticament. Per veure la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

L'extensió MSSQL per a VS Code fa temps que creix, però aquesta última actualització deixa la direcció molt més clara.

Ja no és només «connecta't i executa unes consultes».

Amb la **provisió d'Azure SQL**, el **Schema Designer amb Copilot**, els **SQL Notebooks** i el **Data API builder** avançant tots en una sola versió, l'extensió s'està convertint en un espai de treball molt més complet per al desenvolupament centrat en bases de dades.

## El ganxo pràctic és la provisió directament des de l'editor

L'article original diu que ara pots crear una base de dades al núvol totalment gestionada «directament des de l'editor i sense cost» mitjançant la capa gratuïta.

Aquest és el tipus de funció que sembla petita fins que t'adones de tota la fricció de configuració que elimina.

Per a molts desenvolupadors, la part feixuga de les proves intensives en dades no és SQL en si. És la bretxa d'entorn entre:

- la idea
- la base de dades
- l'esquema
- l'API
- un backend que es pugui provar

Si aquesta bretxa es fa més curta dins d'una sola eina, tot el flux de treball es torna més atractiu.

## Així és com es veu un inner loop més fort per al treball amb dades

El que m'agrada d'aquesta versió és que manté més part del flux de treball de la base de dades en un sol lloc:

- provisió de la base de dades
- disseny de l'esquema
- revisió dels canvis
- generació de scripts ORM
- exposició d'APIs
- proves d'endpoints
- documentació i consultes mitjançant notebooks

Això és una història molt més convincent que tractar SQL com una eina lateral desconnectada dins de la pila.

## El flux de treball d'esquema assistit per Copilot és on el valor d'IA sembla real

Les novetats del dissenyador d'esquemes són especialment interessants perquè semblen trobar un bon equilibri.

El valor no és «la IA dissenya el teu model de dades i tu t'hi refies a cegues».

El valor és:

- punts de partida més ràpids
- revisió visual
- seguiment de canvis
- sortida orientada a migració
- controls explícits d'acceptar/desfer

És un flux de treball d'IA molt més saludable que una generació automàtica completa sense cap camí de revisió.

I en el treball de bases de dades, la revisabilitat importa molt.

## Data API builder és un multiplicador silenciós

L'altra característica que no ignoraria és la integració de Data API builder.

Si pots passar de l'esquema a:

- REST
- GraphQL
- endpoints MCP

dins del mateix entorn, això crea un camí molt eficient per a prototips de backend i eines internes.

Això no substitueix una enginyeria backend més profunda. Però sí que escurça el camí des de la idea de base de dades fins a una interfície funcional.

## La meva lectura

Aquesta versió fa que l'extensió MSSQL sembli més una petita plataforma dins de VS Code que un simple complement.

Per a desenvolupadors que creen APIs, eines de dades, eines d'administració o prototips recolzats en SQL, això és un canvi significatiu.

I si Microsoft continua ajustant aquest bucle, l'extensió esdevindrà molt més estratègicament útil del que molta gent encara assumeix.

Publicació original: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)