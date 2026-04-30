---
title: "GPT-5.5 Ja És Aquí a Azure Foundry — El que els Desenvolupadors .NET Han de Saber"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 ja és disponible a Microsoft Foundry. La progressió des de GPT-5 fins a 5.5, què ha millorat realment i com començar a usar-lo en els teus agents avui."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Microsoft acaba d'anunciar que [GPT-5.5 ja és disponible a Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Si has estat construint agents a Azure, aquesta és l'actualització que esperaves.

## La progressió de GPT-5

- **GPT-5**: va unificar raonament i velocitat en un sol sistema
- **GPT-5.4**: raonament multi-pas més robust, capacitats agèntiques per a empreses
- **GPT-5.5**: raonament de llarg context més profund, execució agèntica més fiable, millor eficiència de tokens

## Què ha canviat realment

**Millor codificació agèntica**: GPT-5.5 manté el context a través de grans bases de codi, diagnostica fallades arquitectòniques i anticipa requisits de proves.

**Eficiència de tokens**: Sortides de major qualitat amb menys tokens i menys reintents. Menys cost i latència en producció.

**Anàlisi de llarg context**: Gestiona documents extensos i historials multi-sessió sense perdre el fil.

## Preus

| Model | Entrada ($/M tokens) | Entrada en memòria cau | Sortida ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5.00 | $0.50 | $30.00 |
| GPT-5.5 Pro | $30.00 | $3.00 | $180.00 |

## Foundry Agent Service

Defineix agents en YAML o connecta'ls amb Microsoft Agent Framework, GitHub Copilot SDK, LangGraph o l'SDK d'OpenAI Agents — i executa'ls com a agents allotjats aïllats amb sistema de fitxers persistent, identitat de Microsoft Entra i preus d'escala a zero.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Ets un assistent útil.", name: "ElMeuAgent");
```

Consulta l'[anunci complet](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/).
