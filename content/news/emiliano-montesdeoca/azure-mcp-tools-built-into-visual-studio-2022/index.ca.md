---
title: "Les eines MCP d'Azure s'incorporen ara a Visual Studio 2022: no es requereix cap extensió"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Les eines d'Azure MCP s'envien com a part de la càrrega de treball de desenvolupament d'Azure a Visual Studio 2022. Més de 230 eines, 45 serveis d'Azure, sense extensions per instal·lar."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

Si heu estat utilitzant les eines de l'Azure MCP a Visual Studio mitjançant l'extensió separada, ja coneixeu l'exercici: instal·leu el VSIX, reinicieu, espereu que no es trenqui, gestioneu els desajustos de versions. Aquesta fricció ha desaparegut.

Yun Jung Choi [va anunciar](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) que les eines d'Azure MCP ara s'envien directament com a part de la càrrega de treball de desenvolupament d'Azure a Visual Studio 2022. Sense extensió. No VSIX. No reinicia el ball.

## Què significa realment això

A partir de la versió 17.14.30 de Visual Studio 2022, l'Azure MCP Server s'inclou amb la càrrega de treball de desenvolupament d'Azure. Si ja teniu aquesta càrrega de treball instal·lada, només cal que l'activeu a GitHub Copilot Chat i ja heu acabat.

Més de 230 eines en 45 serveis Azure, accessibles directament des de la finestra de xat. Enumereu els vostres comptes d'emmagatzematge, implementeu una aplicació ASP.NET Core, diagnostiqueu problemes del servei d'aplicacions, consulteu Log Analytics, tot sense obrir una pestanya del navegador.

## Per què això importa més del que sembla

Això és el que passa amb les eines per a desenvolupadors: cada pas addicional és fricció i la fricció mata l'adopció. Tenir MCP com a extensió independent significava desajustos de versions, errors d'instal·lació i una cosa més a mantenir actualitzada. Incorporar-lo a la càrrega de treball significa:

- **Camí d'actualització únic** mitjançant l'instal·lador de Visual Studio
- **Sense deriva de versió** entre l'extensió i l'IDE
- **Sempre actual**: el servidor MCP s'actualitza amb versions regulars de VS

Per als equips que s'estandarditzen a Azure, això és un gran problema. Instal·leu la càrrega de treball una vegada, activeu les eines i hi són per a cada sessió.

## Què pots fer amb ell

Les eines cobreixen tot el cicle de vida del desenvolupament mitjançant Copilot Chat:

- **Aprendre**: pregunteu sobre els serveis d'Azure, les pràctiques recomanades i els patrons d'arquitectura
- **Disseny i desenvolupament**: obteniu recomanacions de servei, configureu el codi de l'aplicació
- **Desplega**: proveïu recursos i implementeu-los directament des de l'IDE
- **Resolució de problemes**: consulteu registres, comproveu l'estat dels recursos, diagnosticeu problemes de producció

Un exemple ràpid: escriviu això a Copilot Chat:

```
List my storage accounts in my current subscription.
```

Copilot truca a les eines d'Azure MCP darrere de les escenes, consulta les vostres subscripcions i retorna una llista amb format amb noms, ubicacions i SKU. No cal cap portal.

## Com activar-lo

1. Actualització a Visual Studio 2022 **17.14.30** o superior
2. Assegureu-vos que la càrrega de treball **Desenvolupament d'Azure** estigui instal·lada
3. Obriu GitHub Copilot Chat
4. Feu clic al botó **Selecciona eines** (la icona de dues claus)
5. Activa **Servidor MCP d'Azure**

Això és tot. Es manté activat durant les sessions.

## Una advertència

Les eines estan desactivades de manera predeterminada: heu d'activar-les. I les eines específiques de VS 2026 no estan disponibles a VS 2022. La disponibilitat de les eines també depèn dels vostres permisos de subscripció a Azure, igual que el portal.

## La imatge més gran

Això forma part d'una tendència clara: MCP s'està convertint en la forma estàndard d'aprofitar les eines de núvol en els IDE de desenvolupadors. Ja hem vist la [versión estable d'Azure MCP Server 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) i les integracions MCP a VS Code i altres editors. Tenir-lo integrat al sistema de càrrega de treball de Visual Studio és la progressió natural.

Per als desenvolupadors de.NET que vivim a Visual Studio, això elimina un altre motiu per canviar de context al portal Azure. I sincerament, com menys canvis de pestanya, millor.
