---
title: "Microsoft Foundry abril 2026: Foundry Local GA, GPT-5.5, CodeAct amb Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "El resum d'abril de Foundry és intens: Foundry Local arriba a GA, arriba GPT-5.5, Agent Framework obté traçat OpenTelemetry, CodeAct executa Python a micro-VM de Hyperlight i arriba el tauler de monitoratge d'agents."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Un mes agitat per a Microsoft Foundry. Aquí teniu els anuncis més importants.

## Foundry Local disponible de manera general

Foundry Local — el temps d'execució d'IA local multiplataforma de Microsoft — ha passat de la previsualització a GA a Windows, macOS (Apple Silicon) i Linux x64. Inferència de model local preparada per a producció amb un SDK amigable per als desenvolupadors. La versió 1.1 afegeix suport per a transcripció, embeddings i l'API Responses.

## GPT-5.5

El model més recent de la família GPT-5 ja està disponible a Foundry. Quota per defecte per a subscripcions Tier 5 i Tier 6. Si heu treballat amb variants anteriors de GPT-5, val la pena avaluar-lo per al vostre cas d'ús.

## Traçat d'Agent Framework a Foundry

Dues funcions de traçat arriben en previsualització aquest mes:

**Traçat de Microsoft Agent Framework** — Els agents MAF ara poden exportar traces d'OpenTelemetry a Foundry. Depureu el comportament de l'agent, seguiu execucions de múltiples passos, exposeu la latència i els errors en les crides d'eines. Això omple un buit real: saber *què va fer realment l'agent en producció*, no només el que va retornar.

**Traçat d'agents allotjats** — Les sessions, les crides d'eines i els passos d'execució dels agents allotjats també apareixen en les traces de Foundry. La mateixa història d'observabilitat s'estén a la capa allotjada.

## CodeAct amb Hyperlight (Alpha)

Aquesta és l'addició tècnicament més interessant: Agent Framework ara pot executar codi Python dins de màquines virtuals micro [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct és el patró on els agents generen i executen codi Python com a eina. La preocupació òbvia és la seguretat — esteu executant codi generat pel model. Les micro-VM de Hyperlight proporcionen aïllament a nivell de procés amb temps d'inici propers al natiu, fent que l'execució de codi en sandbox sigui pràctica sense la sobrecàrrega de contenidors o VM complets.

Per als fluxos de treball d'agents que necessiten execució de codi, aquesta és una millora de seguretat significativa en comparació d'executar codi al procés amfitrió.

## Tauler de monitoratge d'agents (Previsualització)

Un tauler operacional unificat que combina ús de tokens, latència, taxa d'èxit d'execució i puntuacions d'avaluadors en una sola vista. La diferència respecte als taulers d'observabilitat habituals: inclou resultats d'avaluació al costat de les mètriques operacionals, de manera que podeu correlacionar "l'agent s'ha tornat més lent" amb "les puntuacions de l'avaluador han baixat" — o confirmar que no tenen relació.

## Avaluadors personalitzats d'avaluació contínua (Previsualització)

Ara podeu portar els vostres propis avaluadors basats en codi o en prompts al pipeline d'avaluació contínua. Anteriorment, l'avaluació contínua es limitava als avaluadors integrats. Els avaluadors personalitzats us permeten aplicar estàndards de qualitat específics de l'equip en el bucle de monitoratge de producció.

## Inventari d'agents al Control Plane

La vista Operate del Control Plane de Foundry ara mostra tots els agents suportats a la vostra subscripció: agents de Foundry, Azure SRE Agent, bucles d'agents de Logic Apps i agents personalitzats registrats. Una sola vista per entendre què s'ha desplegat i on.

Publicació original: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
