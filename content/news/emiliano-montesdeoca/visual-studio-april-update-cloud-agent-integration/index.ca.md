---
title: "Actualització d'abril de Visual Studio 2026: Agent del núvol, agents personalitzats i agent depurador"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "L'actualització d'abril de Visual Studio 2026 (18.5) incorpora integració d'agent del núvol, agents personalitzats a nivell d'usuari, eines C++ en GA i un Agent Depurador que valida les correccions contra el comportament real en temps d'execució."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[L'actualització d'abril de Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) inclou integració d'agent del núvol, agents personalitzats a nivell d'usuari, eines C++ que arriben a GA i un nou Agent Depurador.

## Agent del núvol: delegar feina a una sessió remota de Copilot

Des del selector d'agents de la finestra Chat, seleccionar **Cloud** permet delegar una tasca a un agent de codificació remot de Copilot. Descriviu la feina, l'agent crea un issue a GitHub al vostre repositori, i obre una PR quan acaba. Rebeu una notificació amb "View PR" / "Open in browser" — tot funciona mentre continueu codificant, o fins i tot amb l'IDE tancat.

## Els agents personalitzats ara us acompanyen

Els agents personalitzats a nivell d'usuari emmagatzemats a `%USERPROFILE%/.github/agents/` ja no estan limitats al repositori — us segueixen a través dels projectes. La ruta d'emmagatzematge és configurable a Tools > Options > GitHub > Copilot > Chat. El botó `+` al selector d'agents us permet crear nous agents directament. Obtenen les mateixes capacitats: consciència de l'espai de treball, eines, selecció de model i connexions MCP.

Agents integrats: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Les eines d'edició de codi C++ arriben a GA

Dues eines — `get_symbol_call_hierarchy` i `get_symbol_class_hierarchy` — ara estan activades per defecte. Proporcionen a Copilot navegació conscient del llenguatge en bases de codi C++, cobrint jerarquies d'herència i cadenes de crida de funcions. Activeu-les mitjançant la icona Tools a Copilot Chat. Funciona millor amb models de trucada d'eines.

## Agent Depurador: correccions validades contra el comportament real en temps d'execució

Comenceu des d'un issue de GitHub o Azure DevOps (o una descripció en llenguatge natural), canvieu al mode Debugger, i l'agent:

1. Crea un reproductor mínim
2. Genera hipòtesis de fallada
3. Instrumenta l'aplicació amb tracepoints i breakpoints condicionals
4. Executa una sessió de depuració real
5. Analitza telemetria en viu
6. Suggereix una solució precisa

Us manteniu en el bucle durant tot el procés — és interactiu, no completament autònom.

## Correcció de prioritat d'IntelliSense

VS ara suprimeix les completions de Copilot mentre la llista d'IntelliSense és activa. Un suggeriment alhora. Era un punt de fricció freqüent i ara està activat per defecte.

Notes de llançament completes i descàrrega a [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
