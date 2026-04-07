---
title: "MCP Apps bekommen eine Fluent API — Erstelle reichhaltige AI-Tool-UIs in .NET in drei Schritten"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Die neue Fluent-Konfigurations-API für MCP Apps auf Azure Functions ermöglicht es, jedes .NET MCP-Tool in eine vollständige App mit Views, Berechtigungen und CSP-Richtlinien in nur wenigen Codezeilen zu verwandeln."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}}).*

MCP-Tools sind großartig, um AI-Agenten Fähigkeiten zu geben. Aber was, wenn dein Tool dem Benutzer etwas zeigen muss — ein Dashboard, ein Formular, eine interaktive Visualisierung? Genau dafür gibt es MCP Apps, und sie sind jetzt viel einfacher zu erstellen.

Lilian Kasem vom Azure SDK-Team [hat die neue Fluent-Konfigurations-API vorgestellt](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) für MCP Apps auf .NET Azure Functions, und es ist die Art von Verbesserung der Entwicklererfahrung, bei der man sich fragt, warum es nicht schon immer so einfach war.

## Was sind MCP Apps?

MCP Apps erweitern das Model Context Protocol, indem sie Tools eigene UI-Views, statische Assets und Sicherheitskontrollen mitgeben können. Anstatt nur Text zurückzugeben, kann dein MCP-Tool vollständige HTML-Erlebnisse rendern — interaktive Dashboards, Datenvisualisierungen, Konfigurationsformulare — alles von AI-Agenten aufrufbar und den Benutzern durch MCP-Clients präsentiert.

Der Haken war, dass das manuelle Verkabeln all dieser Dinge tiefes Wissen über die MCP-Spezifikation erforderte: `ui://`-URIs, spezielle MIME-Types, Metadaten-Koordination zwischen Tools und Ressourcen. Nicht schwer, aber fummellig.

## Die Fluent API in drei Schritten

**Schritt 1: Definiere deine Funktion.** Ein standardmäßiges Azure Functions MCP-Tool:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Schritt 2: Mach sie zur MCP App.** In deinem Programm-Startup:

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

**Schritt 3: Füge deine HTML-View hinzu.** Erstelle `assets/hello-app.html` mit der UI, die du brauchst.

Das war's. Die Fluent API kümmert sich um die gesamte MCP-Protokoll-Plumbing — generiert die synthetische Ressourcen-Funktion, setzt den korrekten MIME-Type und injiziert die Metadaten, die dein Tool mit seiner View verbinden.

## Die API-Oberfläche ist gut durchdacht

Ein paar Dinge, die mir besonders gefallen:

**View-Quellen sind flexibel.** Du kannst HTML von Dateien auf der Festplatte servieren oder Ressourcen direkt in deine Assembly einbetten für eigenständige Deployments:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP ist komponierbar.** Du erlaubst explizit die Origins, die deine App braucht, nach dem Prinzip der minimalen Berechtigung. Rufe `WithCsp` mehrmals auf und die Origins akkumulieren sich:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Sichtbarkeitskontrolle.** Du kannst ein Tool nur für das LLM sichtbar machen, nur für die Host-UI oder für beides. Du willst ein Tool, das nur UI rendert und nicht vom Modell aufgerufen werden soll? Kein Problem:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Erste Schritte

Füge das Preview-Paket hinzu:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Wenn du bereits MCP-Tools mit Azure Functions baust, ist das nur ein Paket-Update. Der [MCP Apps Quickstart](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) ist der beste Einstiegspunkt, wenn du neu im Konzept bist.

## Zusammenfassung

MCP Apps sind eine der spannendsten Entwicklungen im AI-Tooling-Bereich — Tools, die nicht nur Dinge *tun*, sondern den Benutzern auch Dinge *zeigen* können. Die Fluent API entfernt die Protokollkomplexität und lässt dich auf das Wesentliche konzentrieren: die Logik deines Tools und seine Oberfläche.

Lies den [vollständigen Beitrag](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) für die komplette API-Referenz und Beispiele.
