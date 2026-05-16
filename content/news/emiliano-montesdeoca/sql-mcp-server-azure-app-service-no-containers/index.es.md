---
title: "SQL MCP Server en Azure App Service — Sin Contenedores"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "El SQL MCP Server ahora puede ejecutarse en Azure App Service sin Docker ni Kubernetes. Esto es lo que significa para los desarrolladores .NET que construyen agentes de IA que hablan con bases de datos SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Seré honesto contigo: cada vez que veo "requiere un contenedor" en un tutorial, una pequeña parte de mí suspira. Los contenedores son geniales, hasta que tu equipo no tiene una estrategia de contenedores, y de repente una funcionalidad que parecía simple está bloqueada por una sobrecarga de orquestación que no habías planeado.

Por eso esto me llamó la atención. El SQL MCP Server ahora puede ejecutarse en Azure App Service — sin Docker, sin Kubernetes, solo la misma configuración de Data API Builder (DAB) que expone tu base de datos SQL a través de MCP, REST y GraphQL.

## ¿Qué es el SQL MCP Server?

Contexto rápido si aún no lo conoces. El SQL MCP Server se sitúa entre tu agente de IA y tu base de datos SQL. En lugar de darle a tu agente acceso directo a la base de datos (lo cual es terrible idea), expone tus tablas y vistas como una capa de abstracción — entidades con permisos definidos.

Está construido sobre [Data API builder](https://learn.microsoft.com/es-es/azure/data-api-builder/), lo que significa que un único archivo de configuración gestiona MCP *y* REST *y* GraphQL simultáneamente. Tu agente habla con el endpoint MCP. Tu aplicación tradicional habla con REST o GraphQL. Misma config, mismo runtime, superficies diferentes.

Eso es genuinamente útil. No estás manteniendo dos capas de API separadas.

## El Problema del Contenedor (y la Solución)

El modelo de despliegue original del SQL MCP Server era con contenedores. Funciona bien en muchos equipos, pero no en todos. Muchos equipos .NET estandarizan en Azure App Service o VMs. Requerir un runtime de contenedor solo para exponer un endpoint SQL agrega fricción que nadie pidió.

El nuevo tutorial muestra cómo saltarte el contenedor por completo. Todo funciona con un comando `dab start`, alojado en App Service como un proceso web .NET 8 estándar.

Aquí está el flujo de configuración local en pocas palabras:

```bash
# Instalar Data API builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Inicializar la configuración
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Agregar una entidad
dab add products --source dbo.products --permissions "authenticated:*"

# Configurar el proveedor de auth de App Service
dab configure --runtime.host.authentication.provider AppService

# Iniciar el servidor
dab start
```

En este punto tienes MCP en `/mcp`, REST y GraphQL desde el mismo proceso, y nada corriendo en un contenedor.

## Autenticación Sin Claves de API Compartidas

Esta es la parte que más aprecio. Cuando despliegas en App Service, configuras Microsoft Entra ID como proveedor de autenticación. Sin secretos compartidos en archivos de configuración, sin claves de API que rotar.

La cadena de conexión permanece en una variable de entorno de App Service (no en `dab-config.json`), y el endpoint MCP está protegido por autenticación de plataforma. Si ya estás alineado con Entra ID en tus cargas de trabajo de Azure — lo cual probablemente sea el caso si usas agentes de Azure AI Foundry — esto encaja naturalmente.

Para el desarrollo local, cambias al modo `Simulator` y transporte STDIO. Vuelves al modo `AppService` cuando despliegas. Limpio y explícito.

## Despliegue en App Service

El despliegue real es trabajo estándar con Azure CLI:

```bash
# Crear el plan de App Service
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

# Crear la aplicación web (runtime .NET 8)
az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

# Configurar el comando de inicio
az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Luego despliega tu proyecto DAB usando el método de despliegue que tu equipo ya usa — VS Code, GitHub Actions, Zip Deploy. El detalle clave: es un despliegue de **código**, no de contenedor. Sin imagen que construir, publicar ni gestionar.

## Por qué Importa para los Desarrolladores .NET

Si estás construyendo agentes de IA en .NET — ya sea con el Microsoft Agent Framework, Semantic Kernel, o agentes hospedados en Azure AI Foundry — eventualmente tu agente necesita hablar con una base de datos. El SQL MCP Server te da una manera estructurada de hacer eso sin exponer cadenas de conexión en bruto ni escribir una capa de API personalizada.

Ejecutarlo en App Service cierra la brecha para equipos que no trabajan con contenedores. Es la misma configuración de DAB, la misma auth de Entra, el mismo protocolo MCP — solo en infraestructura que ya conoces.

Consulta el tutorial completo en el [post original del blog](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) y el [repositorio de muestra en GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Conclusión

El SQL MCP Server en App Service es una opción pragmática sólida para equipos .NET que quieren dar a sus agentes acceso estructurado a datos SQL sin una estrategia de contenedores. La combinación del modelo de entidades de DAB, la auth integrada de Entra en App Service, y el comando de inicio `dab start` resulta en un despliegue simple de explicar y fácil de operar.

Pruébalo. Tus agentes apreciarán la superficie de API limpia. Tu equipo de operaciones apreciará no tener que lidiar con registros de contenedores.
