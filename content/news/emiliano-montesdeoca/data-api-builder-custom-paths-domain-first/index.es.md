---
title: 'Data API Builder Custom Paths te permite diseñar APIs para humanos, no para tablas'
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: 'Las rutas REST compuestas en DAB son una característica pequeña con gran impacto arquitectónico para el diseño de API orientado al dominio.'
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Fuente original: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

El nuevo soporte de rutas REST compuestas en Data API Builder puede parecer una mejora menor de configuración, pero en realidad resuelve una tensión de diseño de API de larga data: la topología de la base de datos filtrándose en el diseño de endpoints públicos.