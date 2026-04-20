---
title: "Les aplicacions MCP obtenen una API fluida: creeu interfícies d'usuari d'eines d'IA rica a.NET amb tres passos"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La nova API de configuració fluida per a aplicacions MCP a Azure Functions us permet convertir qualsevol eina.NET MCP en una aplicació completa amb vistes, permisos i polítiques de CSP en poques línies de codi."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

Les eines MCP són excel·lents per oferir capacitats als agents d'IA. Però, què passa si la vostra eina ha de mostrar alguna cosa a l'usuari: un tauler, un formulari, una visualització interactiva? Aquí és on entren les aplicacions MCP i són molt més fàcils de crear.

Lilian Kasem de l'equip de l'SDK d'Azure [va presentar la nova API de configuració fluida](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) per a les aplicacions MCP a.NET Azure Functions, i és el tipus de millora de l'experiència dels desenvolupadors que us fa preguntar-vos per què no sempre va ser tan senzill.

## Què són les aplicacions MCP?

Les aplicacions MCP amplien el protocol de context del model deixant que les eines portin les seves pròpies vistes d'interfície d'usuari, actius estàtics i controls de seguretat. En lloc de només retornar text, la vostra eina MCP pot representar experiències HTML completes (taulers interactius, visualitzacions de dades, formularis de configuració), tot això invocable pels agents d'IA i presentat als usuaris pels clients MCP.

El problema va ser que el cablejat de tot això manualment requeria conèixer íntimament les especificacions MCP: `ui://` URI, tipus de mime especials, coordinació de metadades entre eines i recursos. No és difícil, però complicat.

## L'API fluida en tres passos

**Pas 1: defineix la teva funció.** Només una eina MCP estàndard d'Azure Functions:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Pas 2: promocioneu-lo a una aplicació MCP.** A l'inici del vostre programa:

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

**Pas 3: afegiu la vostra vista HTML.** Creeu `assets/hello-app.html` amb la interfície d'usuari que necessiteu.

Això és tot. L'API fluida gestiona tota la fontaneria d'especificacions MCP: genera la funció de recursos sintètics, estableix el tipus de mime correcte, injecta les metadades que connecten l'eina a la seva vista.

## La superfície de l'API està ben dissenyada

Algunes coses que m'agraden molt:

**Les fonts de visualització són flexibles.** Podeu publicar HTML des de fitxers al disc o inserir recursos directament al vostre conjunt per a desplegaments autònoms:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP es pot redactar.** Llista de permisos explícita que els orígens de la teva aplicació necessita, seguint els principis de privilegis mínims. Truqueu a `WithCsp` diverses vegades i els orígens s'acumulen:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Control de visibilitat.** Podeu fer que una eina només sigui visible per al LLM, només per a la interfície d'usuari de l'amfitrió o ambdues. Voleu una eina que només representi la interfície d'usuari i que el model no l'hagi de cridar? Fàcil:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Primers passos

Afegeix el paquet de previsualització:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Si ja esteu creant eines MCP amb Azure Functions, això és només una actualització del paquet. El [inici ràpid de les aplicacions MCP](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) és el millor lloc per començar si sou nou al concepte.

## Tancant

Les aplicacions MCP són un dels desenvolupaments més interessants de l'espai d'eines d'IA: eines que no només * fan coses * sinó que poden * mostrar coses * als usuaris. L'API fluida elimina la complexitat del protocol i us permet centrar-vos en allò que importa: la lògica de l'eina i la seva interfície d'usuari.

Llegiu la [publicació completa](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) per obtenir la referència completa de l'API i els exemples.
