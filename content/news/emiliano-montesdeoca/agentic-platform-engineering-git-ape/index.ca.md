---
title: "L'enginyeria de la plataforma agentica s'està tornant real: Git-APE mostra com"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "El projecte Git-APE de Microsoft posa en pràctica l'enginyeria de plataformes agents, utilitzant agents GitHub Copilot i Azure MCP per convertir les sol·licituds de llenguatge natural en una infraestructura de núvol validada."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

L'enginyeria de plataformes ha estat un d'aquells termes que sona molt bé a les conferències, però normalment significa "vam construir un portal intern i un embolcall de Terraform". La veritable promesa: una infraestructura d'autoservei que és realment segura, governada i ràpida, sempre ha estat a pocs passos.

L'equip d'Azure acaba de publicar la [Part 2 de la seva sèrie d'enginyeria de plataformes agents](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/), i aquesta tracta sobre la implementació pràctica. L'anomenen **Git-APE** (sí, l'acrònim és intencionat) i és un projecte de codi obert que utilitza agents GitHub Copilot més servidors Azure MCP per convertir les sol·licituds de llenguatge natural en una infraestructura validada i desplegada.

## Què fa realment Git-APE

La idea bàsica: en lloc que els desenvolupadors aprenguin mòduls de Terraform, naveguin per les interfícies d'usuari del portal o presenten entrades a un equip de plataforma, parlen amb un agent Copilot. L'agent interpreta la intenció, genera Infrastructure-as-Code, la valida amb polítiques i desplega, tot dins de VS Code.

Aquí teniu la configuració:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Obriu l'espai de treball a VS Code i GitHub Copilot descobreix automàticament els fitxers de configuració de l'agent. Interacciones directament amb l'agent:

```
@git-ape deploy a function app with storage in West Europe
```

L'agent utilitza Azure MCP Server sota el capó per interactuar amb els serveis d'Azure. La configuració de MCP a la configuració del codi VS permet capacitats específiques:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Per què això és important

Per a aquells que estem construint a Azure, això canvia la conversa sobre l'enginyeria de la plataforma de "com construïm un portal" a "com descriurem les nostres baranes com a API". Quan la interfície de la vostra plataforma és un agent d'IA, la qualitat de les vostres limitacions i polítiques es converteix en el producte.

El bloc de la Part 1 va exposar la teoria: les API ben descrites, els esquemes de control i les baranes explícites fan que les plataformes estiguin preparades per a agents. La part 2 demostra que funciona enviant eines reals. L'agent no només genera recursos a cegues, sinó que valida les millors pràctiques, respecta les convencions de denominació i aplica les polítiques de la vostra organització.

La neteja és igual de fàcil:

```
@git-ape destroy my-resource-group
```

## La meva opinió

Seré sincer: aquest tracta més del patró que de l'eina específica. El mateix Git-APE és una arquitectura de demostració/referència. Però la idea subjacent (agents com a interfície de la vostra plataforma, MCP com a protocol, GitHub Copilot com a amfitrió) és cap a on es dirigeix ​​l'experiència dels desenvolupadors empresarials.

Si sou un equip de plataformes que mira com fer que els vostres agents d'eines internes siguin amigables, no hi ha millor punt de partida. I si sou un desenvolupador de.NET i us pregunteu com es connecta això amb el vostre món: els agents Azure MCP Server i GitHub Copilot funcionen amb qualsevol càrrega de treball d'Azure. La vostra API ASP.NET Core, la vostra pila.NET Aspire, els vostres microserveis en contenidors: tot això pot ser l'objectiu d'un flux de desplegament agent.

## Tancant

Git-APE és una visió primerenca però concreta de l'enginyeria de plataformes agències a la pràctica. Cloneu el [repo](https://github.com/Azure/git-ape), proveu la demostració i comenceu a pensar com haurien de buscar un agent per utilitzar-los de manera segura les API i les polítiques de la vostra plataforma.

Llegiu la [publicació completa](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) per a la guia i les demostracions de vídeo.
