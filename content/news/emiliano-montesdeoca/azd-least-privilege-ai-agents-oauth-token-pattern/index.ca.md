---
title: "El Teu Agent d'IA Té un Problema d'Identitat (I Aquí Tens la Plantilla que el Resol)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Una nova plantilla azd de Curity i Microsoft mostra com construir agents d'IA que utilitzen tokens OAuth de curta durada amb àmbits de gra fi — perquè els agents mai puguin veure dades que no haurien de veure."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Hi ha un moment en cada projecte d'agent d'IA que funciona més o menys així: la demo funciona perfectament, l'agent interpreta el llenguatge natural, crida les API correctes, retorna les dades correctes. Llavors comences a pensar en els usuaris reals.

Què impedeix que la sessió de l'agent d'un usuari vegi les dades d'un altre usuari? Què passa si l'agent és enganyat mitjançant injecció de prompts? Què passa si crida una eina d'una manera inesperada?

Aquestes no són casos extrems. Són decisions de disseny que has de prendre abans d'envisar.

Una nova plantilla `azd` de Curity i Microsoft et dóna una referència funcional per a exactament aquest problema.

## El Problema Principal: Autenticació ≠ Autorització

La majoria de mostres d'agents gestionen bé l'autenticació d'usuaris. Gestionen malament l'autorització. Saber *qui* és l'usuari no et diu *quines dades* hauria de veure.

Una aplicació client tradicional fa crides d'API predictibles. Un agent d'IA és no determinista — interpreta el llenguatge natural i decideix a qui cridar. Pot ser creatiu. També pot estar equivocat. I si és manipulat a través d'injecció de prompts, necessites regles que no depenguin que la IA es comporti bé.

La solució que demostra aquesta plantilla: **tokens de curta durada que transporten exactament la informació correcta per a cada salt**.

## Com Funciona la Cadena de Tokens

La plantilla utilitza tokens d'accés OAuth 2.0 amb intercanvi de tokens per estrenyir els permisos a cada pas. Un token d'usuari s'intercanvia dues vegades abans d'arribar al servidor MCP:

1. **Primer intercanvi** — estreny l'àmbit i converteix el token opac en un JWT
2. **Segon intercanvi** — afegeix la identitat de l'agent i una nova audiència per al salt del servidor MCP

Com és el token del servidor MCP:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

El `customer_id` queda incorporat al token pel servidor d'autorització, no es passa com un paràmetre que controla l'agent. L'API comprova el token, no les instruccions de l'agent.

Això significa: fins i tot si algú enganya l'agent perquè intenti obtenir les dades d'un altre client, el token no ho autoritzarà.

## Què Desplega la Plantilla

Amb uns quants comandaments `azd` obtens:

- Un agent backend a Microsoft Foundry (C#, SDK de Microsoft A2A i MCP)
- Un servidor MCP que exposa una API de cartera de mostra
- Curity Identity Server com a servidor d'autorització, al costat d'Entra ID per a l'autenticació
- Passarel·les d'API externes i internes que gestionen l'intercanvi de tokens i el registre d'auditoria
- Bicep per a tota la infraestructura Azure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, emmagatzematge

Tot el patró és inspeccionable i personalitzable.

## El Principi de Disseny que Val la Pena Adoptar

Fins i tot si no uses Curity, el patró és transferible: **els agents mai haurien de tenir accés permanent a l'API**. Cada acció hauria d'usar un token de curta durada amb el mínim àmbit necessari per a aquella crida específica, emès a la identitat específica de l'agent, portant les reclamacions que l'API necessita per prendre decisions d'autorització.

Això resisteix agents creatius, errors i injecció de prompts de maneres que "assegura't que l'agent no faci coses dolentes" mai ho farà.

## Conclusió

Els patrons de seguretat per a agents d'IA encara s'estan definint a tota la indústria. Aquesta plantilla és una de les implementacions de referència més completes que he vist — cobreix el flux d'autorització real, no només l'autenticació.

Post original: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
