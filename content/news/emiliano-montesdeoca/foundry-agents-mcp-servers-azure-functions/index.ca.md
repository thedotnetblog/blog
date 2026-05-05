---
title: "Connecteu els vostres servidors MCP a les funcions d'Azure amb els agents de Foundry: aquí teniu com"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Creeu el vostre servidor MCP una vegada, implementeu-lo a Azure Functions i connecteu-lo als agents de Microsoft Foundry amb l'autenticació adequada. Les vostres eines funcionen a tot arreu: VS Code, Cursor i ara agents d'IA empresarials."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

Aquí hi ha una cosa que m'encanta de l'ecosistema MCP: creeu el vostre servidor una vegada i funciona a tot arreu. VS Code, Visual Studio, Cursor, ChatGPT: cada client MCP pot descobrir i utilitzar les vostres eines. Ara, Microsoft afegeix un altre consumidor a aquesta llista: agents de Foundry.

Lily Ma de l'equip d'Azure SDK [va publicar una guia pràctica](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) sobre la connexió de servidors MCP desplegats a Azure Functions amb agents de Microsoft Foundry. Si ja teniu un servidor MCP, això és pur valor afegit, no cal reconstruir-lo.

## Per què aquesta combinació té sentit

Azure Functions us ofereix una infraestructura escalable, una autenticació integrada i una facturació sense servidor per allotjar servidors MCP. Microsoft Foundry us ofereix agents d'IA que poden raonar, planificar i prendre accions. Connectar les dues significa que les vostres eines personalitzades (consultar una base de dades, trucar a una API empresarial, executar una lògica de validació) esdevenen capacitats que els agents d'IA empresarials poden descobrir i utilitzar de manera autònoma.

El punt clau: el vostre servidor MCP es manté igual. Només esteu afegint Foundry com un altre consumidor. Les mateixes eines que funcionen a la configuració de VS Code ara alimenten un agent d'IA amb el qual interactuen el vostre equip o clients.

## Opcions d'autenticació

Aquí és on la publicació realment afegeix valor. Quatre mètodes d'autenticació segons el vostre escenari:

|Mètode|Cas d'ús|
|--------|----------|
|**Basat en clau** (per defecte)|Desenvolupament o servidors sense autenticació Entra|
|**Entrada de Microsoft**|Producció amb identitats gestionades|
|**Transmissió d'identitat OAuth**|Producció on cada usuari s'autentica individualment|
|**No autenticat**|Desenvolupament/proves o dades públiques només|

Per a la producció, el camí recomanat és Microsoft Entra amb la identitat de l'agent. El pas d'identitat d'OAuth és per quan el context de l'usuari importa: l'agent demana als usuaris que iniciïn sessió i cada sol·licitud porta el testimoni propi de l'usuari.

## Configurant-lo

El flux d'alt nivell:

1. **Implementeu el vostre servidor MCP a Azure Functions**: mostres disponibles per a [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript i Java
2. **Activa l'autenticació MCP integrada** a l'aplicació de funcions
3. **Obteniu l'URL del vostre punt final** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Afegiu el servidor MCP com a eina a Foundry**: aneu al vostre agent al portal, afegiu una eina MCP nova, proporcioneu el punt final i les credencials.

A continuació, proveu-ho al parc infantil de l'Agent Builder enviant un missatge que activaria una de les vostres eines.

## La meva opinió

La història de la composició aquí s'està fent molt forta. Creeu el vostre servidor MCP una vegada a.NET (o Python, TypeScript, Java), implementeu-lo a Azure Functions i tots els clients compatibles amb MCP el podran utilitzar: eines de codificació, aplicacions de xat i ara agents d'IA empresarials. Aquest és un patró "Escriu una vegada, utilitza a tot arreu" que realment funciona.

Per als desenvolupadors de.NET específicament, l'[extensió MCP d'Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) ho fa senzill. Definiu les vostres eines com a Azure Functions, les implementeu i disposeu d'un servidor MCP de nivell de producció amb tota la seguretat i escala que ofereix Azure Functions.

## Tancant

Si teniu eines MCP que s'executen a Azure Functions, connectar-les als agents de Foundry és una victòria ràpida: les vostres eines personalitzades es converteixen en capacitats d'IA empresarial amb una autenticació adequada i sense canvis de codi al propi servidor.

Llegiu la [guia completa](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) per obtenir instruccions pas a pas sobre cada mètode d'autenticació i consulteu la [documentació detallada](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) per a les configuracions de producció.
