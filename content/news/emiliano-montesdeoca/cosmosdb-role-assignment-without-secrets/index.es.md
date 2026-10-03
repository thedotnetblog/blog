---
title: 'Acceso a Cosmos DB sin secretos es la nueva línea base'
date: 2026-07-16
author: 'Emiliano Montesdeoca'
description: 'Si tu aplicación de Cosmos DB aún depende de claves, ya estás atrasado en seguridad operativa.'
tags:
  - azure-cosmos-db
  - dotnet
  - managed-identity
  - rbac
  - cloud-security
---

Fuente original: [Which Azure Cosmos DB Role Does My App Need?](https://devblogs.microsoft.com/cosmosdb/which-azure-cosmos-db-role-does-my-app-need/)

La idea más importante en esta guía de Cosmos DB no es un comando, un ID de rol o un truco de CLI. Es arquitectónica: **deja de tratar las credenciales como configuración de aplicación** y comienza a tratar la identidad como estado de ejecución.