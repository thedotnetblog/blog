---
title: "Per què el disseny en capes de Microsoft Agent Framework realment importa"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "La nova explicació del SDK en capes de Microsoft Agent Framework és més que una xerrada d'arquitectura. Mostra com Microsoft vol que els desenvolupadors passin de bucles senzills a una orquestració preparada per a producció sense llençar-ho tot per la borda."
tags:
  - Agent Framework
  - AI
  - .NET
  - Architecture
  - Developer Tools
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).

Les anunciacions de frameworks normalment van directes a les funcions.

Aquesta va començar amb la **filosofia de disseny**, i crec que és exactament per això que importa.

La nova explicació de com Microsoft Agent Framework s'organitza al voltant de **agent loops**, **workflows** i **harnesses** ens dona un senyal molt millor que una altra llista de funcionalitats. Ens diu com l'equip espera que creixin les aplicacions reals.

I per a qualsevol que construeixi agents en .NET, aquesta és la part valuosa.

## La majoria de les aplicacions d'agents superen molt ràpidament la seva primera arquitectura

Comences amb una crida al model.

Després hi afegeixes eines.

Després memòria.

Després un planificador.

Després reintents, telemetria, aprovacions, agents especialitzats i una mica de lògica de workflow, perquè un sol loop ja no n'hi ha prou.

Aquí és on moltes aplicacions d'IA es tornen un embolic. La primera versió funcionava, però cada capacitat nova s'enganxava des d'un nivell d'abstracció diferent.

El que m'agrada del text sobre Agent Framework és que fa explícites les capes:

- **loops** per al cicle d'execució principal
- **workflows** per a l'orquestració estructurada
- **harnesses** per a capacitats de runtime reutilitzables al voltant de l'agent

Pot semblar acadèmic al principi, però resol un problema molt pràctic: **pots fer evolucionar l'aplicació sense reescriure el model mental cada vegada que es fa més complexa**.

## El concepte de harness és especialment important

Si hagués de triar una part que crec que serà cada cop més important, triaria la idea de **harness**.

El harness és el lloc on el desenvolupament d'agents deixa de ser només prompting i es converteix en enginyeria.

És la capa on comences a fixar-te en:

- eines i middleware
- comportament de planificació
- integració de memòria
- observability
- controls i governance
- comportament de runtime repetible

També per això el disseny encaixa tan bé amb la resta de la pila de Microsoft. Foundry, les eines de governança, els hosted agents, les avaluacions i els ecosistemes d'eines tenen molt més sentit quan l'embolcall de runtime al voltant del model es tracta com una peça de primera classe.

## És un bon senyal per als desenvolupadors de .NET

Una cosa que sempre miro en aquests ecosistemes és si el framework continua sent útil després de la primera demo.

L'enfocament en capes suggereix que Microsoft està pensant en el recorregut complet:

1. construir un loop d'agent senzill
2. afegir capacitats estructurades sense caos
3. passar a workflows més formals quan l'aplicació els necessita
4. mantenir el runtime prou componible per integrar-lo amb sistemes empresarials

Això és una via de creixement molt més saludable que "aquí tens una abstracció monolítica, sort".

I s'alinea molt amb la manera com els desenvolupadors de .NET solen treballar: sistemes en capes, composició explícita, fronteres testables i control fort del runtime.

## La meva lectura

Aquest post és fàcil de subestimar perquè no porta una captura espectacular ni un abocament massiu d'API.

Però notes d'arquitectura com aquesta sovint prediuen millor si un framework aguantará d'aquí sis mesos.

Microsoft Agent Framework clarament intenta ser més que un embolcall de joguina al voltant de les crides al model. La història del SDK en capes diu que l'equip està construint per al tram complicat del mig: el lloc on els agents necessiten orquestració, eines, serveis de runtime i disciplina de producció.

És exactament el lloc que m'interessa.

Publicació original: [ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK]({{< ref "index.md" >}})
