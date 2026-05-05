---
title: "azd + GitHub Copilot: Configuració de projecte amb IA i resolució intel·ligent d'errors"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI ara s'integra amb GitHub Copilot per generar la infraestructura del teu projecte i resoldre errors de desplegament — sense sortir del terminal."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Aquest article ha estat traduït automàticament. Per veure la versió original en anglès, [fes clic aquí]({{< ref "index.md" >}}).*

Coneixes aquell moment en què vols desplegar una aplicació existent a Azure i et quedes mirant un `azure.yaml` en blanc, intentant recordar si la teva API Express hauria d'usar Container Apps o App Service? Aquell moment acaba de ser molt més curt.

L'Azure Developer CLI (`azd`) ara s'integra amb GitHub Copilot de dues maneres concretes: scaffolding assistit per IA durant `azd init`, i resolució intel·ligent d'errors quan els desplegaments fallen. Les dues funcions es queden completament al terminal — exactament on vull que siguin.

## Configuració amb Copilot durant azd init

Quan executes `azd init`, ara apareix l'opció "Set up with GitHub Copilot (Preview)". Selecciona-la i Copilot analitza el teu codebase per generar l'`azure.yaml`, les plantilles d'infraestructura i els mòduls Bicep — basant-se en el teu codi real.

```
azd init
# Selecciona: "Set up with GitHub Copilot (Preview)"
```

Requisits:

- **azd 1.23.11 o superior** — comprova amb `azd version` o actualitza amb `azd update`
- **Una subscripció activa de GitHub Copilot** (Individual, Business o Enterprise)
- **GitHub CLI (`gh`)** — `azd` demanarà login si cal

El que trobo genuïnament útil és que funciona en els dos sentits. Construint des de zero? Copilot t'ajuda a configurar els serveis Azure correctes des del principi. Tens una app existent que vols desplegar? Apunta Copilot cap a ella i genera la configuració sense haver de reestructurar res.

### El que fa realment

Imagina que tens una API Express en Node.js amb dependència de PostgreSQL. En lloc de decidir manualment entre Container Apps i App Service, i després escriure Bicep des de zero, Copilot detecta el teu stack i genera:

- Un `azure.yaml` amb els ajustaments correctes de `language`, `host` i `build`
- Un mòdul Bicep per a Azure Container Apps
- Un mòdul Bicep per a Azure Database for PostgreSQL

I fa comprovacions prèvies abans de tocar res — verifica que el teu directori git estigui net, demana consentiment per a les eines del servidor MCP. Res no passa sense que sàpigues exactament què canviarà.

## Resolució d'errors amb Copilot

Els errors de desplegament són inevitables. Paràmetres que falten, problemes de permisos, disponibilitat de SKUs — i el missatge d'error rarament et diu l'única cosa que realment necessites saber: *com solucionar-ho*.

Sense Copilot, el cicle és: copiar l'error → buscar als docs → llegir tres respostes irrellevants de Stack Overflow → executar alguns comandos `az` CLI → tornar-ho a intentar i rezar. Amb Copilot integrat a `azd`, aquest cicle s'esfondra. Quan qualsevol comandament `azd` falla, ofereix immediatament quatre opcions:

- **Explain** — descripció en llenguatge natural del que ha anat malament
- **Guidance** — instruccions pas a pas per solucionar-ho
- **Diagnose and Guide** — anàlisi completa + Copilot aplica la solució (amb la teva aprovació) + reintent opcional
- **Skip** — gestionar-ho tu mateix

El punt clau: Copilot ja té context sobre el teu projecte, el comandament que ha fallat i la sortida de l'error. Les seves suggerències són específiques per a *la teva situació*.

### Configurar un comportament predeterminat

Si sempre tries la mateixa opció, salta el prompt interactiu:

```
azd config set copilot.errorHandling.category troubleshoot
```

Valors: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. També pots habilitar auto-fix i reintent:

```
azd config set copilot.errorHandling.fix allow
```

Torna al mode interactiu en qualsevol moment:

```
azd config unset copilot.errorHandling.category
```

## Conclusió

Executa `azd update` per obtenir la versió més recent i usa `azd init` en el teu proper projecte. És exactament el tipus d'integració de Copilot que aporta valor real.

Llegeix l'[anunci original aquí](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
