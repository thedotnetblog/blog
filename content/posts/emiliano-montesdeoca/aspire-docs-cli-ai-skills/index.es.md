---
title: "Aspire 13.2 incluye una CLI de documentación — y tu agente de IA también puede usarla"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 añade aspire docs — una CLI para buscar, explorar y leer documentación oficial sin salir de tu terminal. También funciona como herramienta para agentes de IA. Te cuento por qué esto importa."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "aspire-docs-cli-ai-skills.md" >}}).*

¿Conocés ese momento cuando estás metido hasta el cuello en un Aspire AppHost, conectando integraciones, y necesitás verificar exactamente qué parámetros espera la integración de Redis? Hacés alt-tab al navegador, buscás por aspire.dev, entrecerrás los ojos mirando los docs de la API, y volvés a tu editor. Contexto perdido. Flujo roto.

Aspire 13.2 acaba de [lanzar una solución para eso](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). La CLI `aspire docs` te permite buscar, explorar y leer documentación oficial de Aspire directamente desde tu terminal. Y como está respaldada por servicios reutilizables, los agentes de IA y skills pueden usar los mismos comandos para consultar docs en lugar de alucinar APIs que no existen.

## El problema que esto realmente resuelve

David Pine lo clava en el post original: los agentes de IA eran *terribles* ayudando a los desarrolladores a construir apps con Aspire. Recomendaban `dotnet run` en vez de `aspire run`, referenciaban learn.microsoft.com para docs que viven en aspire.dev, sugerían paquetes NuGet desactualizados, y — mi favorito personal — alucinaban APIs que no existen.

¿Por qué? Porque Aspire fue específico de .NET por mucho más tiempo del que lleva siendo políglota, y los LLMs trabajan con datos de entrenamiento que preceden las últimas funcionalidades. Cuando le das a un agente de IA la capacidad de buscar los docs actuales, deja de adivinar y empieza a ser útil.

## Tres comandos, cero pestañas del navegador

La CLI es refrescantemente simple:

### Listar todos los docs

```bash
aspire docs list
```

Devuelve cada página de documentación disponible en aspire.dev. ¿Necesitás salida legible por máquina? Agregá `--format Json`.

### Buscar un tema

```bash
aspire docs search "redis"
```

Busca tanto en títulos como en contenido con puntuación de relevancia ponderada. El mismo motor de búsqueda que alimenta la herramienta de documentación internamente. Obtenés resultados rankeados con títulos, slugs y puntuaciones de relevancia.

### Leer una página completa (o solo una sección)

```bash
aspire docs get redis-integration
```

Transmite la página completa como markdown a tu terminal. ¿Necesitás solo una sección?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Precisión quirúrgica. Sin hacer scroll por 500 líneas. Solo la parte que necesitás.

## El ángulo del agente de IA

Acá es donde se pone interesante para los que desarrollamos con herramientas de IA. Los mismos comandos de `aspire docs` funcionan como herramientas para agentes de IA — a través de skills, servidores MCP, o wrappers simples de CLI.

En vez de que tu asistente de IA invente APIs de Aspire basándose en datos de entrenamiento obsoletos, puede llamar a `aspire docs search "postgres"`, encontrar los docs oficiales de integración, leer la página correcta, y darte el enfoque documentado. Documentación en tiempo real y actual — no lo que el modelo memorizó hace seis meses.

La arquitectura detrás de esto es intencional. El equipo de Aspire construyó servicios reutilizables (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) en lugar de una integración única. Eso significa que el mismo motor de búsqueda funciona para humanos en la terminal, agentes de IA en tu editor, y automatización en tu pipeline de CI.

## Escenarios del mundo real

**Consultas rápidas en terminal:** Estás tres archivos adentro y necesitás los parámetros de configuración de Redis. Dos comandos, noventa segundos, de vuelta al trabajo:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**Desarrollo asistido por IA:** Tu skill de VS Code envuelve los comandos de la CLI. Preguntás "Agregá una base de datos PostgreSQL a mi AppHost" y el agente busca los docs reales antes de responder. Sin alucinaciones.

**Validación en CI/CD:** Tu pipeline valida configuraciones de AppHost contra documentación oficial de forma programática. La salida `--format Json` se conecta limpiamente con `jq` y otras herramientas.

**Bases de conocimiento personalizadas:** ¿Estás construyendo tu propia herramienta de IA? Enviá la salida JSON estructurada directamente a tu base de conocimiento:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Sin web scraping. Sin API keys. Los mismos datos estructurados que usa internamente la herramienta de documentación.

## La documentación siempre está actualizada

Esta es la parte que más aprecio. La CLI no descarga una captura estática — consulta aspire.dev con caché basado en ETag. En el momento en que los docs se actualizan, tu CLI y cualquier skill construido sobre ella lo refleja. Sin copias obsoletas, sin momentos de "pero el wiki decía...".

## Para cerrar

`aspire docs` es una de esas funcionalidades pequeñas que resuelve un problema real de forma limpia. Los humanos obtienen acceso a documentación nativa de terminal. Los agentes de IA obtienen una forma de dejar de adivinar y empezar a referenciar docs reales. Y todo está respaldado por la misma fuente de verdad.

Si estás construyendo con .NET Aspire y todavía no probaste la CLI, ejecutá `aspire docs search "tu-tema-aquí"` y fijate cómo se siente. Después considerá envolver esos comandos en cualquier skill de IA o configuración de automatización que estés usando — tus agentes te lo van a agradecer.

Mirá el [análisis profundo de David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/) sobre cómo se armó la herramienta de documentación, y la [referencia oficial de la CLI](https://aspire.dev/reference/cli/commands/aspire-docs/) para todos los detalles.
