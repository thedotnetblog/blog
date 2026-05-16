---
title: "SQL MCP Server a Azure App Service — Sense Contenidors"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "El SQL MCP Server ara pot executar-se a Azure App Service sense Docker ni Kubernetes. Això és el que significa per als desenvolupadors .NET que construeixen agents d'IA que parlen amb bases de dades SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Seré honest amb tu: cada cop que veig "requereix un contenidor" en un tutorial, una petita part de mi sospira. Els contenidors són fantàstics, fins que el teu equip no té una estratègia de contenidors, i de cop allò que semblava simple queda bloquejat per una sobrecàrrega d'orquestació que no havies planificat.

Per això aquest em va cridar l'atenció. El SQL MCP Server ara pot executar-se a Azure App Service — sense Docker, sense Kubernetes, únicament amb la mateixa configuració de Data API Builder (DAB) que exposa la teva base de dades SQL a través de MCP, REST i GraphQL.

## Què és el SQL MCP Server?

Context ràpid si encara no el coneixes. El SQL MCP Server se situa entre el teu agent d'IA i la teva base de dades SQL. En lloc de donar a l'agent accés directe a la base de dades (una idea terrible), exposa les teves taules i vistes com una capa d'abstracció — entitats amb permisos definits.

Està construït sobre [Data API Builder](https://learn.microsoft.com/es-es/azure/data-api-builder/), la qual cosa significa que un únic fitxer de configuració gestiona MCP *i* REST *i* GraphQL simultàniament. El teu agent parla amb l'endpoint MCP. La teva aplicació tradicional parla amb REST o GraphQL. Mateixa config, mateix runtime, superfícies diferents.

Això és genuïnament útil. No estàs mantenint dues capes d'API separades.

## El Problema del Contenidor (i la Solució)

El model de desplegament original del SQL MCP Server era amb contenidors. Funciona bé en molts equips, però no en tots. Molts equips .NET estandaritzen en Azure App Service o VMs. Requerir un runtime de contenidor únicament per exposar un endpoint SQL afegeix fricció que ningú va demanar.

El nou tutorial mostra com ometre el contenidor per complet. Tot funciona amb una ordre `dab start`, allotjat a App Service com un procés web .NET 8 estàndard.

```bash
# Instal·lar Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Inicialitzar la configuració
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Afegir una entitat
dab add products --source dbo.products --permissions "authenticated:*"

# Configurar el proveïdor d'autenticació d'App Service
dab configure --runtime.host.authentication.provider AppService

# Iniciar el servidor
dab start
```

En aquest punt tens MCP a `/mcp`, REST i GraphQL des del mateix procés, i res executant-se en un contenidor.

## Autenticació Sense Claus d'API Compartides

Aquesta és la part que més aprecio. Quan despliegues a App Service, configures Microsoft Entra ID com a proveïdor d'autenticació. Sense secrets compartits als fitxers de configuració, sense claus d'API que rotar.

La cadena de connexió es manté en una variable d'entorn d'App Service (no a `dab-config.json`), i l'endpoint MCP està protegit per l'autenticació de la plataforma. Si ja estàs alineat amb Entra ID a les teves càrregues de treball d'Azure, això encaixa de manera natural.

Per al desenvolupament local, canvies al mode `Simulator` i transport STDIO. Tornes al mode `AppService` quan despliegues. Net i explícit.

## Desplegament a App Service

El desplegament real és feina estàndard amb l'Azure CLI:

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Llavors desplegues el teu projecte DAB usant el mètode de desplegament que el teu equip ja utilitza. El detall clau: és un desplegament de **codi**, no de contenidor.

## Per Què Importa per als Desenvolupadors .NET

Si construeixes agents d'IA en .NET, eventualment el teu agent necessitarà parlar amb una base de dades. El SQL MCP Server t'ofereix una manera estructurada de fer-ho sense exposar cadenes de connexió en brut ni escriure una capa d'API personalitzada.

Consulta el tutorial complet al [post original](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) i el [repositori de mostra a GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Conclusió

El SQL MCP Server a App Service és una opció pragmàtica sòlida per a equips .NET que volen donar als seus agents accés estructurat a dades SQL sense una estratègia de contenidors. La combinació del model d'entitats de DAB, l'autenticació integrada d'Entra a App Service i la comanda d'inici `dab start` resulta en un desplegament senzill d'explicar i fàcil d'operar.

Prova-ho. Els teus agents agrairan la superfície d'API neta.
