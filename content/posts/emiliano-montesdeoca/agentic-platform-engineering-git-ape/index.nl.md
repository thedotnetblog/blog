---
title: "Agentic Platform Engineering Wordt Werkelijkheid — Git-APE Laat Zien Hoe"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsofts Git-APE project brengt agentic platform engineering in de praktijk — met GitHub Copilot-agents en Azure MCP om natuurlijke taalverzoeken om te zetten in gevalideerde cloudinfrastructuur."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform engineering is een van die termen die geweldig klinkt op conferenties maar meestal "we hebben een intern portaal en een Terraform-wrapper gebouwd" betekent. De echte belofte — self-service infrastructuur die werkelijk veilig, beheerd en snel is — was altijd een paar stappen verwijderd.

Het Azure-team heeft zojuist [Deel 2 van hun agentic platform engineering-serie](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) gepubliceerd. Ze noemen het **Git-APE** — een open-source project dat GitHub Copilot-agents en Azure MCP-servers gebruikt om natuurlijke taalverzoeken om te zetten in gevalideerde, geïmplementeerde infrastructuur.

## Wat Git-APE eigenlijk doet

Het kernidee: in plaats van Terraform-modules te leren, praten ontwikkelaars met een Copilot-agent. De agent interpreteert de intentie, genereert Infrastructure-as-Code, valideert tegen beleid en implementeert — allemaal in VS Code.

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Open de werkruimte in VS Code, en de agent-configuratiebestanden worden automatisch gevonden door GitHub Copilot:

```
@git-ape deploy a function app with storage in West Europe
```

Opruimen is net zo eenvoudig:

```
@git-ape destroy my-resource-group
```

## Waarom dit ertoe doet

Voor degenen die op Azure bouwen, verschuift dit het platform engineering-gesprek van "hoe bouwen we een portaal" naar "hoe beschrijven we onze guardrails als API's."

Als .NET-ontwikkelaar: Azure MCP Server en GitHub Copilot-agents werken met elke Azure-workload — je ASP.NET Core API, .NET Aspire-stack — alles kan het doel zijn van een agentische deployment flow.

## Samenvatting

Git-APE is een vroeg maar concreet beeld van agentic platform engineering in de praktijk. Clone de [repo](https://github.com/Azure/git-ape) en lees de [volledige post](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/).
