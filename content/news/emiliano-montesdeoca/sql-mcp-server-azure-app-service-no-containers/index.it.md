---
title: "SQL MCP Server su Azure App Service — Senza Container"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Il SQL MCP Server ora può girare su Azure App Service senza Docker né Kubernetes. Cosa significa per gli sviluppatori .NET che costruiscono agenti AI che parlano con database SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Diciamoci la verità: ogni volta che vedo "richiede un container" in un tutorial, una piccola parte di me sospira. I container sono fantastici — finché il tuo team non ha una strategia per i container, e improvvisamente una funzionalità che sembrava semplice è bloccata da complessità di orchestrazione che nessuno aveva pianificato.

Ecco perché questo mi ha colpito. Il SQL MCP Server ora può girare su Azure App Service — senza Docker, senza Kubernetes, solo con la stessa configurazione di Data API Builder (DAB) che espone il tuo database SQL tramite MCP, REST e GraphQL.

## Cos'è il SQL MCP Server?

Contesto rapido se non lo conosci ancora. Il SQL MCP Server si trova tra il tuo agente AI e il tuo database SQL. Invece di dare all'agente accesso diretto al database (un'idea pessima), espone le tue tabelle e view come uno strato di astrazione — entità con permessi definiti.

È costruito su [Data API Builder](https://learn.microsoft.com/it-it/azure/data-api-builder/), il che significa che un singolo file di configurazione gestisce MCP *e* REST *e* GraphQL contemporaneamente. Il tuo agente parla con l'endpoint MCP. La tua applicazione tradizionale parla con REST o GraphQL. Stessa config, stesso runtime, superfici diverse.

Questo è genuinamente utile. Non stai mantenendo due strati API separati.

## Il Problema del Container (e la Soluzione)

Il modello di deployment originale del SQL MCP Server usava i container. Funziona bene in molti team — ma non in tutti. Molti team .NET standardizzano su Azure App Service o VM. Richiedere un runtime di container solo per esporre un endpoint SQL aggiunge attrito che nessuno ha chiesto.

Il nuovo walkthrough mostra come saltare completamente il container. Tutto funziona con un comando `dab start`, ospitato su App Service come un processo web .NET 8 standard.

```bash
# Installare Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Inizializzare la configurazione
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Aggiungere un'entità
dab add products --source dbo.products --permissions "authenticated:*"

# Configurare il provider di autenticazione App Service
dab configure --runtime.host.authentication.provider AppService

# Avviare il server
dab start
```

A questo punto hai MCP su `/mcp`, REST e GraphQL dallo stesso processo, e niente che gira in un container.

## Autenticazione Senza Chiavi API Condivise

Questa è la parte che apprezzo di più. Quando fai il deploy su App Service, configuri Microsoft Entra ID come provider di autenticazione. Nessun segreto condiviso nei file di configurazione, nessuna chiave API da ruotare.

La stringa di connessione rimane in una variabile d'ambiente di App Service (non in `dab-config.json`), e l'endpoint MCP è protetto dall'autenticazione della piattaforma. Se sei già allineato con Entra ID nei tuoi workload Azure, questo si integra naturalmente.

Per lo sviluppo locale, passi alla modalità `Simulator` e al trasporto STDIO. Torni alla modalità `AppService` prima del deployment. Pulito ed esplicito.

## Deploy su App Service

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

Poi fai il deploy del tuo progetto DAB usando il metodo di deployment del codice che il tuo team già utilizza. Il dettaglio chiave: è un deployment di **codice**, non di container.

## Perché Importa per gli Sviluppatori .NET

Se stai costruendo agenti AI in .NET, prima o poi il tuo agente dovrà comunicare con un database. Il SQL MCP Server ti dà un modo strutturato per farlo senza esporre stringhe di connessione grezze.

Consulta il tutorial completo nel [post originale](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) e il [repository di esempio su GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Conclusione

Il SQL MCP Server su App Service è una solida opzione pragmatica per i team .NET che vogliono dare ai propri agenti accesso strutturato ai dati SQL senza una strategia di container. Provalo — i tuoi agenti apprezzeranno la superficie API pulita.
