---
title: "Foundry Toolboxes: Un únic endpoint per a totes les eines dels teus agents"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry acaba de llançar Toolboxes en preview pública — una manera de curar, gestionar i exposar eines d'agents IA a través d'un únic endpoint compatible amb MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [feu clic aquí]({{< ref "index.md" >}}).*

Hi ha un problema que sembla avorrit fins que el pateixes de primera mà: la teva organització està construint múltiples agents d'IA, cadascun necessita eines, i cada equip les connecta des de zero. La mateixa integració de cerca web, la mateixa config d'Azure AI Search, la mateixa connexió al servidor MCP de GitHub — però en un altre repositori, per un altre equip, amb altres credencials i sense cap governança compartida.

Microsoft Foundry acaba de llançar [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) en preview pública, i és una resposta directa a aquest problema.

## Què és un Toolbox?

Un Toolbox és un bundle d'eines amb nom, reutilitzable, que defineixes una vegada a Foundry i exposes a través d'un únic endpoint compatible amb MCP. Qualsevol runtime d'agent que parli MCP pot consumir-lo — no estàs bloquejat a Foundry Agents.

La proposta és simple: **build once, consume anywhere**. Defineix les eines, configura l'autenticació de forma centralitzada, publica l'endpoint. Cada agent que necessiti les eines es connecta a l'endpoint i les obté totes.

## Els quatre pilars (dos disponibles avui)

| Pilar | Estat | Què fa |
|-------|-------|--------|
| **Discover** | Pròximament | Troba eines aprovades sense buscar manualment |
| **Build** | Disponible avui | Agrupa eines en un bundle reutilitzable |
| **Consume** | Disponible avui | Un únic endpoint MCP exposa totes les eines |
| **Govern** | Pròximament | Auth centralitzada + observabilitat en totes les crides |

## Exemple pràctic

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Cerca documentació i respon a issues de GitHub.",
    tools=[
        {"type": "web_search", "description": "Cerca documentació pública"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Un cop publicat, Foundry et dona un endpoint unificat. Un punt de connexió, totes les eines.

## No estàs bloquejat a Foundry Agents

Els Toolboxes es **creen i gestionen** a Foundry, però la superfície de consum és el protocol MCP obert. Pots usar-los des d'agents personalitzats amb Microsoft Agent Framework o LangGraph, GitHub Copilot i qualsevol runtime que parli MCP.

## Per què importa ara

L'onada multi-agent està arribant a producció. Cada nou agent és una nova superfície per a configuració duplicada, credencials desfasades i comportament inconsistent. La base de Build + Consume és suficient per començar a centralitzar. Quan arribi el pilar Govern, tindràs una capa d'eines observable i controlada centralment per a tota la teva flota d'agents.

## Conclusió

Això és aviat — preview pública, SDK Python primer. Però el model és sòlid i el disseny natiu MCP significa que funciona amb les eines que ja estàs construint. Fes una ullada a l'[anunci oficial](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) per començar.
