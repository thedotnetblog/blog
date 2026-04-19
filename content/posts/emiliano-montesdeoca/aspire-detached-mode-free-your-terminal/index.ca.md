---
title: "Deixeu de fer de cangur al vostre terminal: el mode desconnectat d'Aspire canvia el flux de treball"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 us permet executar el vostre AppHost en segon pla i recuperar el vostre terminal. Combinat amb les noves ordres de la CLI i el suport d'agents, això és més gran del que sembla."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

Cada vegada que executeu un Aspire AppHost, el vostre terminal desapareixerà. Tancat. Ocupat fins que en feu Ctrl+C. Necessites executar una comanda ràpida? Obre una altra pestanya. Voleu comprovar els registres? Una altra pestanya. És una petita fricció que s'acumula ràpidament.

Aspire 13.2 soluciona això. James Newton-King [va escriure tots els detalls](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), i sincerament, aquesta és una d'aquestes característiques que canvia immediatament la manera de treballar.

## Mode desconnectat: una comanda, terminal enrere

```bash
aspire start
```

Aquesta és l'abreviatura de `aspire run --detach`. El vostre AppHost s'inicia en segon pla i recupereu el terminal immediatament. Sense pestanyes addicionals. Sense multiplexor de terminals. Només la teva indicació, llest per començar.

## Gestionant el que s'està executant

Aquesta és la qüestió: executar-se en segon pla només és útil si realment podeu gestionar el que hi ha. Aspire 13.2 ofereix un conjunt complet d'ordres CLI per exactament això:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

Això converteix l'Aspire CLI en un gestor de processos adequat. Podeu iniciar diversos AppHosts, comprovar el seu estat, seguir els seus registres i tancar-los, tot des d'una única sessió de terminal.

## Combina-ho amb el mode aïllat

El mode separat es combina de manera natural amb el mode aïllat. Voleu executar dues instàncies del mateix projecte en segon pla sense conflictes de ports?

```bash
aspire start --isolated
aspire start --isolated
```

Cadascun obté ports aleatoris, secrets separats i el seu propi cicle de vida. Utilitzeu `aspire ps` per veure tots dos, `aspire stop` per matar el que hàgiu acabat.

## Per què això és enorme per als agents de codificació

Aquí és on es posa realment interessant. Un agent de codificació que treballa al vostre terminal ara pot:

1. Inicieu l'aplicació amb `aspire start`
2. Consulta el seu estat amb `aspire describe`
3. Comproveu els registres amb `aspire logs` per diagnosticar problemes
4. Atureu-ho amb `aspire stop` quan estigui acabat

Tot sense perdre la sessió del terminal. Abans del mode desconnectat, un agent que executava el vostre AppHost es bloquejaria fora del seu propi terminal. Ara pot començar, observar, iterar i netejar, exactament com voldríeu que funcionés un agent autònom.

L'equip d'Aspire es va inclinar en això. L'execució de `aspire agent init` configura un fitxer d'habilitats d'Aspire que ensenya als agents aquestes ordres. Així, eines com l'agent de codificació de Copilot poden gestionar les vostres càrregues de treball d'Aspire des de la caixa.

## Tancant

El mode desconnectat és una actualització del flux de treball disfressada com una simple bandera. Atureu el canvi de context entre terminals, els agents deixen de bloquejar-se i les noves ordres CLI us ofereixen una visibilitat real del que s'està executant. És pràctic, és net i fa que el cicle de desenvolupament diari sigui notablement més suau.

Llegiu la [publicació completa](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) per obtenir tots els detalls i agafeu Aspire 13.2 amb `aspire update --self`.
