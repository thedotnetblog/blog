---
title: "Un Plugin d'Agent WinUI per a GitHub Copilot i Claude Code"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "Microsoft ha publicat habilitats d'agent per al desenvolupament WinUI: scaffold, compilar, executar, provar, iterar — tot amb GitHub Copilot CLI o Claude Code. La innovació clau: eines de propòsit específic que ancoren l'agent en fets específics de WinUI."
tags:
  - WinUI
  - Windows App SDK
  - GitHub Copilot
  - AI
  - Agents
---

Microsoft ha publicat un conjunt de codi obert d'habilitats d'agent per al desenvolupament d'aplicacions WinUI, disponible a [aka.ms/winui-skills](https://aka.ms/winui-skills).

## Instal·lació i Configuració

Instal·la el plugin amb `/plugin install winui@awesome-copilot`, després executa la configuració inicial amb `/winui:winui-setup`. El procés de configuració verifica els requisits previs, instal·la les dependències necessàries i configura l'entorn per al desenvolupament d'aplicacions WinUI.

## El Bucle de Desenvolupament d'Extrem a Extrem

Les habilitats cobreixen el cicle de desenvolupament complet:

- **Scaffold:** Genera la plantilla de projecte correcta usant `dotnet new WinUI` amb els paràmetres adequats — l'agent coneix les plantilles correctes i els valors de configuració predeterminats.
- **Compilació:** Gestiona el model d'execució empaquetada que requereixen les aplicacions WinUI, incloent la signatura del paquet i les configuracions de manifest.
- **Interacció i validació:** Inicia l'aplicació, hi interactua i valida el comportament.
- **Correcció d'errors de compilació:** L'agent entén els missatges d'error específics de WinUI i sap com resoldre'ls.

## Eficiència de Tokens mitjançant Eines de Propòsit Específic

La innovació clau és que les habilitats inclouen eines de propòsit específic que obtenen dades de referència concretes a demanda:

- Detalls de l'API de WinUI i Fluent Design
- Patrons MVVM i millors pràctiques
- Empaquetatge MSIX, signatura de codi i enviament a la Store
- Accessibilitat, temes i automatització de la interfície d'usuari

En lloc d'injectar tota la documentació de WinUI al context, les eines obtenen exactament el que l'agent necessita en el moment que ho necessita. Això manté l'ús del context eficient i millora la precisió en els dominis especialitzats.

## Per Què les Habilitats de Propòsit Específic Són Importants

Els models de llenguatge d'ús general tenen un coneixement limitat sobre els matisos específics de WinUI: el model d'execució empaquetada, les API de Fluent Design, la integració MSIX o la forma específica en què Windows App SDK embolcalla la funcionalitat de Win32. Les eines de propòsit específic resolen això ancoraqnt l'agent en fets de WinUI verificats en lloc del coneixement del model potencialment obsolet o incorrecte.

El mateix patró s'aplica a qualsevol marc o SDK especialitzat amb les seves pròpies convencions i requisits que difereixen dels patrons de desenvolupament generals.

Publicació original: [A WinUI Agent Plugin for GitHub Copilot and Claude Code](https://devblogs.microsoft.com/ifdef-windows/winui-agent-plugin-github-copilot-claude-code/)
