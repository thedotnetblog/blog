---
title: "VS Code 1.119: OpenTelemetry per a sessions d'agents, integració del navegador i seguretat"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (maig 2026) afegeix traçabilitat OpenTelemetry per a sessions d'agents, compartició de pestanyes del navegador, millores de confiança i seguretat, i un pedaç de seguretat 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) va sortir el 6 de maig de 2026 (amb un pedaç de seguretat 1.119.1 poc després). La versió se centra en l'observabilitat dels agents, la interacció amb el navegador i la reducció d'interrupcions.

## Traçabilitat OpenTelemetry per a sessions d'agents

Aquesta és la característica destacada per a qualsevol que executi agents en producció o depuri fluxos de treball agèntics. Activeu-la amb dos paràmetres:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Les traces segueixen les convencions semàntiques de GenAI. Cada sol·licitud d'agent produeix un span arrel `invoke_agent` amb spans fills imbricats: `chat`, `execute_tool` i `execute_hook`. L'ús de tokens s'informa per sol·licitud — incloent el recompte de lectures i creació de caché.

Funciona amb l'agent local, l'agent de fons de Copilot CLI i l'agent de Claude. Qualsevol backend compatible amb OTLP accepta les traces — el [Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) funciona bé per al desenvolupament local.

## Els agents ara poden accedir a les pestanyes del navegador

Els agents poden sol·licitar accés a les pestanyes del navegador integrat — però no és automàtic. Heu de compartir explícitament una pestanya mitjançant el selector de context, arrossegament i col·locació, o context suggerit. Hi ha un botó de compartició al navegador per revocar l'accés. Quan un agent intenta obrir una nova pestanya al mateix domini que una pestanya oberta (no compartida), VS Code us demana que reutilitzeu la pestanya existent.

## Ús optimitzat de tokens

Un model lleuger experimental ara gestiona les llistes de tasques dels agents, mantenint aquesta tasca administrativa fora del model principal més car. Redueix el consum de tokens en tasques que no necessiten plena capacitat de raonament.

## Confiança i seguretat

Menys interrupcions: VS Code 1.119 redueix les sol·licituds d'accés a la xarxa i escriptures a carpetes temporals dels agents. El pedaç 1.119.1 aborda problemes de seguretat específics — val la pena actualitzar si encara no ho heu fet.

## Canvi ràpid a la vista prèvia de Markdown

Petit però útil: ara podeu canviar ràpidament l'editor actual a la vista prèvia de Markdown sense navegar.

## VS Code Agents (previsualització Insiders)

La interfície de sessió d'agents redissenyada — nou selector de repositoris (local/repos/remot), millores de subsessions, poliment web i mòbil, animacions de progrés — està disponible a Insiders a [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Registre de canvis complet: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
