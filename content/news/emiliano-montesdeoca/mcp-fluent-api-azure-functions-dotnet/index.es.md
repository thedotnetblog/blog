---
title: "Las MCP Apps tienen una API fluida — Construye interfaces ricas para herramientas de IA en .NET en tres pasos"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La nueva API de configuración fluida para MCP Apps en Azure Functions te permite convertir cualquier herramienta MCP de .NET en una app completa con vistas, permisos y políticas CSP en pocas líneas de código."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}}).*

Las herramientas MCP son geniales para darle capacidades a los agentes de IA. Pero ¿qué pasa si tu herramienta necesita mostrarle algo al usuario — un dashboard, un formulario, una visualización interactiva? Ahí es donde entran las MCP Apps, y ahora son mucho más fáciles de construir.

Lilian Kasem del equipo de Azure SDK [presentó la nueva API de configuración fluida](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) para MCP Apps en Azure Functions con .NET, y es el tipo de mejora en experiencia de desarrollador que te hace preguntarte por qué no fue siempre así de simple.

## ¿Qué son las MCP Apps?

Las MCP Apps extienden el Model Context Protocol permitiendo que las herramientas lleven sus propias vistas de UI, assets estáticos y controles de seguridad. En lugar de solo devolver texto, tu herramienta MCP puede renderizar experiencias HTML completas — dashboards interactivos, visualizaciones de datos, formularios de configuración — todo invocable por agentes de IA y presentado a los usuarios por clientes MCP.

El problema era que conectar todo esto manualmente requería conocer la especificación MCP a fondo: URIs `ui://`, tipos MIME especiales, coordinación de metadatos entre herramientas y recursos. No era difícil, pero sí tedioso.

## La API fluida en tres pasos

**Paso 1: Define tu función.** Una herramienta MCP de Azure Functions estándar:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Paso 2: Promuévela a MCP App.** En el startup de tu programa:

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

**Paso 3: Añade tu vista HTML.** Crea `assets/hello-app.html` con la interfaz que necesites.

Eso es todo. La API fluida se encarga de toda la plomería del protocolo MCP — genera la función de recurso sintético, establece el tipo MIME correcto e inyecta los metadatos que conectan tu herramienta con su vista.

## La superficie de la API está bien diseñada

Algunas cosas que me gustan mucho:

**Las fuentes de las vistas son flexibles.** Puedes servir HTML desde archivos en disco, o embeber recursos directamente en tu ensamblado para despliegues autónomos:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**El CSP es componible.** Explícitamente permites los orígenes que tu app necesita, siguiendo principios de mínimo privilegio. Llama a `WithCsp` varias veces y los orígenes se acumulan:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Control de visibilidad.** Puedes hacer que una herramienta sea visible solo para el LLM, solo para la UI del host, o ambos. ¿Quieres una herramienta que solo renderice UI y no deba ser llamada por el modelo? Fácil:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Primeros pasos

Añade el paquete preview:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Si ya estás construyendo herramientas MCP con Azure Functions, esto es solo una actualización de paquete. El [quickstart de MCP Apps](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) es el mejor lugar para empezar si eres nuevo en el concepto.

## Para cerrar

Las MCP Apps son uno de los desarrollos más emocionantes en el espacio de herramientas de IA — herramientas que no solo *hacen cosas* sino que pueden *mostrar cosas* a los usuarios. La API fluida elimina la complejidad del protocolo y te permite enfocarte en lo que importa: la lógica de tu herramienta y su interfaz.

Lee el [post completo](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) para la referencia completa de la API y ejemplos.
