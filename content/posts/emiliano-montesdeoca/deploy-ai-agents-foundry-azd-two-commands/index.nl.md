---
title: "Van Laptop naar Productie: AI-agents Implementeren naar Microsoft Foundry met Twee Opdrachten"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "De Azure Developer CLI heeft nu 'azd ai agent'-opdrachten die je AI-agent in minuten van lokale ontwikkeling naar een live Foundry-eindpunt brengen."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "deploy-ai-agents-foundry-azd-two-commands" >}}).*

Ken je die kloof tussen 'het werkt op mijn machine' en 'het is geïmplementeerd en verwerkt verkeer'? Voor AI-agents was die kloof pijnlijk breed.

De Azure Developer CLI heeft dit een [zaak van twee opdrachten](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) gemaakt.

## De nieuwe `azd ai agent` workflow

```bash
azd ai agent init
azd up
```

Dat is alles. `azd ai agent init` maakt een infrastructuur-als-code-skelet in je repo, en `azd up` richt alles in op Azure en publiceert je agent.

## Wat er onder de motorkap gebeurt

De `init`-opdracht genereert echte, inspecterbare Bicep-sjablonen in je repo — Foundry Resource, Foundry Project, modelimplementatieconfiguratie, beheerde identiteit met RBAC.

## Dev inner loop

```bash
azd ai agent run    # agent lokaal starten
azd ai agent invoke # testprompts sturen
azd ai agent monitor --follow  # real-time logs streamen
```

## De volledige opdrachtset

| Opdracht | Wat het doet |
|---------|-------------|
| `azd ai agent init` | Foundry-agentproject scaffolden met IaC |
| `azd up` | Middelen inrichten en agent implementeren |
| `azd ai agent invoke` | Prompts sturen naar externe of lokale agent |
| `azd ai agent run` | Agent lokaal uitvoeren |
| `azd ai agent monitor` | Real-time logs streamen |
| `azd down` | Alle Azure-middelen opruimen |

Bekijk de [volledige walkthrough](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).
