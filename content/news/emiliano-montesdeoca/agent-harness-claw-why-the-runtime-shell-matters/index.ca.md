---
title: "Els Agent Harnesses Importen Perquè els Prompts No Són Suficients"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "El nou tutorial de claw i harness de Microsoft Agent Framework és un recordatori útil que els agents reals necessiten un shell d'execució al voltant del model: eines, planificació, memòria, sessions i un bucle d'execució pràctic."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Un dels errors més fàcils en el desenvolupament d'agents és pensar que el prompt és el producte.

No ho és.

El nou tutorial sobre **agent harness i claw** de l'equip de Microsoft Agent Framework és valuós perquè manté l'enfocament en la part que realment determina si un agent se sent utilitzable: el shell d'execució al voltant del model.

Això inclou:

* eines
* planificació
* estat de sessió
* memòria
* modes d'execució
* una consola o interfície utilitzable per a la iteració

L'article acompanya la implementació completa d'un agent de codificació autònom que opera des d'un contenidor Docker amb accés al sistema de fitxers, execució d'ordres i un bucle autònom sense intervenció humana. No és una abstracció teòrica: és el claw executant-se realment.

## Per què el claw és diferent

Si has seguit el projecte Semaphore de Microsoft Research, el claw et resultarà familiar. És un entorn on un agent pot:

* inspeccionar directoris i fitxers
* llegir i escriure fitxers
* executar ordres de shell
* processar la sortida i continuar iterant

La versió de Microsoft Agent Framework s'integra directament amb el claw: us permet executar un agent autònom configurat amb prompt i opcions dins d'un contenidor aïllat. El resultat és un patró repetible: contenidor → claw → agent. Sense dependències estranyes. Sense eines de compilació personalitzades.

## Per què això importa als desenvolupadors de .NET

El claw demostra alguna cosa que no es pot aconseguir només amb prompts: comportament autònom en bucle tancat sobre dades i sistemes reals.

Un agent de codificació que pot escriure un fitxer, executar proves i iterar sobre els resultats sense que un humà li passi cada fragment de text és qualitativament diferent d'un xat LLM al qual demanes que generi codi.

La diferència és la propietat del bucle tancat. Qui decideix què provar a continuació? Qui gestiona l'estat entre passos? Un harness fa que l'agent sigui propietari del bucle. Un prompt deixa el bucle a les mans de l'usuari.

## On aniria amb compte

No obstant això, el claw no és per a tot. L'execució autònoma en un bucle és potent, però també és una àrea on el cost i la correcció necessiten supervisió externa. És per això que l'article recomana executar el claw en un contenidor: conté el radi d'explosió.

Per a escenaris de baixa autonomia on les eines són simples i les interaccions són breus, un agent senzill amb un prompt ben escrit pot ser suficient.

El punt no és que el claw substitueixi tota conversa. El punt és que el ventall d'arquitectures d'agents que pots construir és més ampli del que permets si només penses en termes de model + prompt.

Publicació original: [Introducing agent harness and claw for the Microsoft Agent Framework](https://devblogs.microsoft.com/agent-framework/introducing-agent-harness-and-claw-for-the-microsoft-agent-framework/)