---
title: "Microsoft Foundry Març de 2026: GPT-5.4, Agent Service GA i l'SDK Refresh que ho canvia tot"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "L'actualització de març de 2026 de Microsoft Foundry és massiva: Agent Service arriba a GA, GPT-5.4 aporta un raonament fiable, l'SDK azure-ai-projects es manté estable en tots els idiomes i Fireworks AI porta models oberts a Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

Les publicacions mensuals "Què hi ha de nou a Microsoft Foundry" solen ser una barreja de millores incrementals i la funció de titular ocasional. La [edició de març de 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? Es tracta bàsicament de totes les funcions dels titulars. El servei d'agent de Foundry passa a GA, el GPT-5.4 s'envia per a la producció, l'SDK obté una versió estable important i Fireworks AI aporta la inferència de model obert a Azure. Permeteu-me desglossar el que importa per als desenvolupadors de.NET.

## El servei d'agent de Foundry està llest per a la producció

Aquest és el gran. El temps d'execució de l'agent de nova generació està disponible generalment: construït a partir de l'API OpenAI Responses, compatible amb cables amb els agents OpenAI i obert a models de diversos proveïdors. Si esteu creant amb l'API Responses avui, la migració a Foundry afegeix seguretat empresarial, xarxes privades, Entra RBAC, seguiment complet i avaluació a més de la vostra lògica d'agent existent.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Addicions clau: xarxes privades d'extrem a extrem, expansió d'autenticació MCP (inclòs OAuth passthrough), previsualització de Voice Live per a agents de veu a veu i agents allotjats en 6 regions noves.

## GPT-5.4: fiabilitat sobre la intel·ligència bruta

GPT-5.4 no es tracta de ser més intel·ligent. Es tracta de ser més fiable. Raonament més sòlid sobre interaccions llargues, millor adherència a les instruccions, menys errors en el flux de treball mitjà i capacitats integrades d'ús de l'ordinador. Per als agents de producció, aquesta fiabilitat és molt més important que les puntuacions de referència.

|Model|Preu (per M fitxes)|Millor per|
|-------|----------------------|----------|
|GPT-5.4 (≤272K)|2,50 $ / 15 $ de sortida|Agents de producció, codificació, fluxos de treball de documents|
|GPT-5.4 Pro|30 $ / 180 $ de sortida|Anàlisi profunda, raonament científic|
|GPT-5.4 Mini|Rentable|Classificació, extracció, trucades d'eines lleugeres|

El joc intel·ligent és una estratègia d'encaminament: GPT-5.4 Mini gestiona el treball de gran volum i de baixa latència, mentre que GPT-5.4 accepta les sol·licituds de gran raonament.

## L'SDK és finalment estable

`azure-ai-projects` SDK va enviar versions estables a tots els idiomes: Python 2.0.0, JS/TS 2.0.0, Java 2.0.0 i.NET 2.0.0 (1 d'abril). La dependència `azure-ai-agents` ha desaparegut: tot viu sota `AIProjectClient`. Instal·leu amb `pip install azure-ai-projects` i els paquets de paquets `openai` i `azure-identity` com a dependències directes.

Per als desenvolupadors de.NET, això significa un únic paquet NuGet per a tota la superfície de Foundry. No més fer malabars amb els SDK d'agents separats.

## Fireworks AI porta models oberts a Azure

Potser l'addició més interessant des del punt de vista arquitectònic: Fireworks AI processa més de 13 bilions de fitxes diaris a ~180.000 sol·licituds per segon, ara disponible a través de Foundry. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5 i MiniMax M2.5 al llançament.

La història real és **porta els teus propis pesos**: penja pesos quantificats o ajustats des de qualsevol lloc sense canviar la pila de porcions. Desplegueu mitjançant pagament per testimoni sense servidor o rendiment subministrat.

## Altres aspectes destacats

- **Phi-4 Reasoning Vision 15B**: raonament multimodal per a gràfics, diagrames i dissenys de documents
- **Avaluacions GA**: avaluadors predefinits amb un seguiment continu de la producció canalitzat a Azure Monitor
- **Processament prioritari** (visualització prèvia): carril informàtic dedicat per a càrregues de treball sensibles a la latència
- **Voice Live**: temps d'execució de veu a veu que es connecta directament als agents de Foundry
- **Tracing GA**: inspecció de traça d'agents d'extrem a extrem amb classificació i filtre
- **PromptFlow obsolet**: migració a Microsoft Framework Workflows abans de gener de 2027

## Tancant

El març de 2026 és un punt d'inflexió per a Foundry. Agent Service GA, SDK estables en tots els idiomes, GPT-5.4 per a agents de producció fiables i inferència de model obert mitjançant Fireworks AI: la plataforma està preparada per a càrregues de treball serioses.

Llegiu el [resum complet](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) i [creeu el vostre primer agent](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) per començar.
