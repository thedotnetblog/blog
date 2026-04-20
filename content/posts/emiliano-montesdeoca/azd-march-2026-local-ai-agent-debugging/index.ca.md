---
title: "azd ara us permet executar i depurar agents d'IA localment: aquí teniu el que va canviar el març de 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI va enviar set versions el març de 2026. Els aspectes més destacats: un bucle local d'execució i depuració per a agents d'IA, integració de GitHub Copilot a la configuració del projecte i suport de Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

Set llançaments en un mes. Això és el que va impulsar l'equip de l'Azure Developer CLI (`azd`) el març de 2026, i la funció de titular és la que estava esperant: **un bucle local d'execució i depuració per als agents d'IA**.

PC Chan [va publicar el resum complet](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) i, tot i que hi ha moltes coses, permeteu-me filtrar-ho fins al que realment importa per als desenvolupadors de.NET que creen aplicacions basades en IA.

## Executeu i depureu agents d'IA sense desplegar-los

Aquest és el gran. La nova extensió `azure.ai.agents` afegeix un conjunt d'ordres que us ofereixen una experiència de bucle interior adequada per als agents d'IA:

- `azd ai agent run`: inicia el vostre agent localment
- `azd ai agent invoke`: li envia missatges (locals o desplegats)
- `azd ai agent show`: mostra l'estat i la salut del contenidor
- `azd ai agent monitor`: transmet els registres dels contenidors en temps real

Abans d'això, provar un agent d'IA significava desplegar-lo a Microsoft Foundry cada vegada que feies un canvi. Ara podeu iterar localment, provar el comportament del vostre agent i només implementar-lo quan estigueu preparat. Si heu estat creant agents amb Microsoft Agent Framework o Semantic Kernel, això canvia el vostre flux de treball diari.

L'ordre d'invocació funciona amb agents locals i desplegats, la qual cosa significa que podeu utilitzar el mateix flux de treball de prova independentment d'on s'executi l'agent. Aquest és el tipus de detall que us estalvia mantenir dos conjunts de scripts de prova.

## GitHub Copilot arma el vostre projecte azd

`azd init` ara ofereix una opció "Configura amb GitHub Copilot (vista prèvia)". En lloc de respondre manualment les sol·licituds sobre l'estructura del vostre projecte, un agent de Copilot us encarrega la configuració. Comprova si hi ha un directori de treball brut abans de modificar res i demana el consentiment de l'eina del servidor MCP per endavant.

Quan una ordre falla, `azd` ara ofereix una resolució de problemes assistida per IA: trieu una categoria (explica, orienta, soluciona problemes o salta), deixeu que l'agent suggereixi una solució i torneu-ho a provar, tot sense sortir del terminal. Per a configuracions d'infraestructures complexes, això suposa un estalvi de temps real.

## Feines de l'aplicació de contenidors i millores en el desplegament

Algunes funcions de desplegament que cal destacar:

- **Fines d'aplicacions de contenidors**: `azd` ara desplega `Microsoft.App/jobs` mitjançant la configuració existent `host: containerapp`. La vostra plantilla de bíceps determina si l'objectiu és una aplicació de contenidor o una feina, sense cap configuració addicional.
- **Temps d'espera de desplegament configurables**: nova marca `--timeout` a `azd deploy` i un camp `deployTimeout` a `azure.yaml`. Ja no cal endevinar el límit predeterminat de 1200 segons.
- **Recurs de compilació remota**: quan la compilació remota d'ACR falla, `azd` torna automàticament a la compilació local de Docker/Podman.
- **Validació local de preflight**: els paràmetres de bíceps es validen localment abans de desplegar-se, capturant els paràmetres que falten sense un viatge d'anada i tornada a Azure.

## Polit de l'experiència del desenvolupador

Algunes millores més petites que sumen:

- **Detecció automàtica de pnpm/fils** per a projectes JS/TS
- **Compatibilitat amb pyproject.toml** per a l'embalatge de Python
- **Directoris de plantilles locals** — `azd init --template` ara accepta camins del sistema de fitxers per a la iteració fora de línia
- **Millors missatges d'error** en mode `--no-prompt`: tots els valors que falten es reporten alhora amb ordres de resolució
- **Variables d'entorn de compilació** injectades a tots els subprocessos de creació de marcs (.NET, Node.js, Java, Python)

Aquesta última és subtil però important: la vostra compilació.NET ara té accés a les variables d'entorn `azd`, la qual cosa significa que podeu fer una injecció de configuració en temps de compilació sense scripts addicionals.

## Tancant

El bucle de depuració de l'agent d'IA local és l'estrella d'aquesta versió, però l'acumulació de millores en el desplegament i la poliment DX fa que `azd` se senti més madur que mai. Si esteu desplegant aplicacions.NET a Azure, especialment agents d'IA, aquesta actualització val la pena instal·lar-la.

Comproveu les [notes completes de la versió](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) per a cada detall o comenceu amb [instal·lació d'azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd).
