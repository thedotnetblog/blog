---
title: "Le MCP Apps hanno una Fluent API — Crea interfacce ricche per strumenti AI in .NET in tre passaggi"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La nuova API di configurazione fluent per le MCP Apps su Azure Functions ti permette di trasformare qualsiasi strumento MCP .NET in un'app completa con viste, permessi e policy CSP in poche righe di codice."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}}).*

Gli strumenti MCP sono fantastici per dare capacità agli agenti AI. Ma cosa succede se il tuo strumento deve mostrare qualcosa all'utente — una dashboard, un form, una visualizzazione interattiva? È qui che entrano in gioco le MCP Apps, e ora sono diventate molto più facili da costruire.

Lilian Kasem del team Azure SDK [ha presentato la nuova API di configurazione fluent](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) per le MCP Apps su Azure Functions .NET, ed è il tipo di miglioramento dell'esperienza sviluppatore che ti fa chiedere perché non fosse sempre così semplice.

## Cosa sono le MCP Apps?

Le MCP Apps estendono il Model Context Protocol permettendo agli strumenti di portare le proprie viste UI, asset statici e controlli di sicurezza. Invece di restituire solo testo, il tuo strumento MCP può renderizzare esperienze HTML complete — dashboard interattive, visualizzazioni di dati, form di configurazione — tutto invocabile dagli agenti AI e presentato agli utenti dai client MCP.

Il problema era che collegare tutto manualmente richiedeva di conoscere la specifica MCP in profondità: URI `ui://`, tipi MIME speciali, coordinamento dei metadati tra strumenti e risorse. Non difficile, ma noioso.

## La Fluent API in tre passaggi

**Passaggio 1: Definisci la tua funzione.** Uno strumento MCP standard di Azure Functions:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Passaggio 2: Promuovila a MCP App.** Nello startup del tuo programma:

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**Passaggio 3: Aggiungi la tua vista HTML.** Crea `assets/hello-app.html` con l'interfaccia di cui hai bisogno.

Tutto qui. La Fluent API gestisce tutta l'infrastruttura del protocollo MCP — genera la funzione risorsa sintetica, imposta il tipo MIME corretto e inietta i metadati che collegano il tuo strumento alla sua vista.

## La superficie dell'API è ben progettata

Alcune cose che mi piacciono molto:

**Le fonti delle viste sono flessibili.** Puoi servire HTML da file su disco, o incorporare risorse direttamente nel tuo assembly per deployment autonomi:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**Il CSP è componibile.** Autorizzi esplicitamente le origini di cui la tua app ha bisogno, seguendo i principi del minimo privilegio. Chiama `WithCsp` più volte e le origini si accumulano:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Controllo della visibilità.** Puoi rendere uno strumento visibile solo al LLM, solo all'UI dell'host, o entrambi. Vuoi uno strumento che renderizza solo UI e non dovrebbe essere chiamato dal modello? Facile:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Per iniziare

Aggiungi il pacchetto preview:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Se stai già costruendo strumenti MCP con Azure Functions, è solo un aggiornamento del pacchetto. Il [quickstart MCP Apps](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) è il miglior punto di partenza se sei nuovo al concetto.

## Conclusione

Le MCP Apps sono uno degli sviluppi più entusiasmanti nello spazio degli strumenti AI — strumenti che non solo *fanno cose* ma possono *mostrare cose* agli utenti. La Fluent API rimuove la complessità del protocollo e ti permette di concentrarti su ciò che conta: la logica del tuo strumento e la sua interfaccia.

Leggi il [post completo](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) per il riferimento completo dell'API e gli esempi.
