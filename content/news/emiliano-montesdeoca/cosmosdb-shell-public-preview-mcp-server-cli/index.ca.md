---
title: "Cosmos DB Shell Està en Versió Preliminar Pública — I Té un Servidor MCP Integrat"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell és una nova CLI de codi obert que exposa les ordres de base de dades com a eines MCP. Els vostres agents d'IA poden navegar per contenidors, executar consultes i gestionar dades usant la mateixa interfície que feu servir vosaltres."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Si alguna vegada heu hagut de navegar entre una pestanya del portal, una mostra de SDK i un script a mig acabar per respondre una sola pregunta de Cosmos DB, ja coneixeu la fricció que aquest projecte està dissenyat per eliminar.

Azure Cosmos DB Shell acaba d'entrar en versió preliminar pública. És una CLI de codi obert amb sintaxi semblant a bash i — la part que ho fa interessant — un servidor MCP integrat.

## Què el Fa Diferent d'Altres CLIs de Base de Dades

La CLI en si és útil: ordres familiars, suport per a scripts, integració CI/CD. Aquesta part és el mínim esperable per a una eina de base de dades orientada als desenvolupadors.

La part interessant és la integració del servidor MCP. Cada ordre que exposa la CLI es converteix en una eina MCP que els vostres agents d'IA poden cridar. No hi ha cap capa d'API personalitzada, ni codi d'integració per escriure. El vostre agent pot:

- Navegar per les jerarquies de bases de dades amb `cd`, `ls`, `pwd`
- Executar consultes SQL amb `query` i obtenir resultats estructurats
- Crear i modificar elements amb `create item`, `update`, `rm`
- Gestionar bases de dades i contenidors amb `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Inspeccionar el context actual amb `endpoint`, `pwd`

El canvi clau: el vostre agent no parla amb una API de Cosmos DB — parla amb la mateixa interfície de shell que feu servir vosaltres. Les ordres són deterministes, auditables i de codi obert per poder inspeccionar exactament el que passa.

## La Base de Codi Obert Importa

Això no és un servei gestionat de caixa negra. El shell és de codi obert, la qual cosa significa:

- Els equips de seguretat poden auditar la implementació
- Els equips de plataforma poden fer fork i ampliar-lo per als seus estàndards específics
- Els desenvolupadors poden contribuir amb millores que beneficien tothom

Per als equips empresarials que adopten eines d'IA, "podem veure exactament com funciona" és cada cop menys un requisit opcional. El codi obert aquí és un diferenciador significatiu.

## Tres Escenaris Que Es Tornen Més Fàcils

**Anàlisi intel·ligent de dades** — connecteu un agent al shell, feu preguntes en llenguatge natural, obteniu resultats de consultes estructurades. L'agent s'encarrega de la construcció de la consulta; el shell s'encarrega de l'execució.

**Gestió autònoma de dades** — els fluxos de treball que necessiten crear, actualitzar o eliminar dades a Cosmos DB poden fer-ho a través de les eines MCP sense necessitar una integració personalitzada.

**Supervisió i alertes en temps real** — un agent pot consultar contenidors periòdicament, comparar resultats i mostrar anomalies a través del canal de notificació que tingui sentit.

La interfície MCP fa que aquests escenaris siguin composables amb qualsevol plataforma d'IA que parli MCP — no només les eines de Microsoft.

## Per Començar

El shell està en versió preliminar pública. Instal·leu-lo, configureu la vostra connexió de Cosmos DB i habiliteu el servidor MCP. Des d'allà, qualsevol host d'agent compatible amb MCP pot descobrir i usar les eines.

Post original: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
