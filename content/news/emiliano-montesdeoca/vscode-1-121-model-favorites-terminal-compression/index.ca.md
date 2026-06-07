---
title: "VS Code 1.121: Fixar Models Favorits, Compressió de Sortida del Terminal, SSH d'Agent"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 afegeix models favorits, compressió ampliada de la sortida del terminal per a executors de proves i eines de compilació, un temporitzador de silenci inactiu per a terminals en segon pla i autenticació SSH interactiva per teclat a l'agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 continua les millores de qualitat de l'agent Copilot de 1.120, centrant-se en la gestió de models i el comportament del terminal.

## Fixar Models Favorits

El selector de models ara admet la fixació. Si sempre recorres al mateix model o a dos, fixa'ls a la part superior de la llista. Redueix el desplaçament quan tens accés a molts models de diversos proveïdors.

## Compressió Ampliada de la Sortida del Terminal

L'eina del terminal de l'agent ja comprimia la sortida per a les ordres habituals. 1.121 ho amplia per cobrir els executors de proves i les eines de compilació:

- **Executors de proves:** `pytest`, `jest`, `cargo test`
- **Eines de compilació:** `tsc`, `cargo build`, `make`
- **Linters, Docker, gestors de paquets**

Les sortides de compilació llargues i els informes de fallades de proves es comprimeixen en extractes rellevants abans de passar-les al model. Això manté l'ús del context manejable quan l'agent executa cicles de compilació o conjunts de proves que poden generar milers de línies de sortida.

## Temporitzador de Silenci Inactiu per a Terminals en Segon Pla

Un nou temporitzador de silenci inactiu per a l'eina `run_in_terminal`: si una ordre síncrona no genera cap sortida durant un període configurable, es promou automàticament a execució en segon pla. Això evita que les ordres de llarga durada bloquegin l'agent mentre processen en silenci. Reps un ID de terminal per comprovar-lo més tard.

## Variable d'Entorn VSCODE_AGENT

Quan Copilot Chat executa ordres al terminal, ara s'estableix una variable d'entorn `VSCODE_AGENT`. Útil si tens scripts o eines que es comporten de manera diferent quan s'invoquen des d'una sessió d'agent versus de manera interactiva.

## Afegir al Xat des del Navegador

Fer clic dret al navegador integrat ara mostra l'opció "Afegir al Xat". Selecciona contingut d'una pàgina web i afegeix-lo directament al context de Copilot Chat sense copiar i enganxar.

## Corregit: Ordres Shell Multilínia a l'Agent Host

Una correcció d'error molt esperada: les ordres shell multilínia a l'eina del terminal d'Agent Host ara funcionen correctament. Anteriorment, podien fallar o produir un comportament incorrecte.

## Autenticació SSH Interactiva per Teclat

Les connexions SSH d'Agent Host ara admeten l'autenticació interactiva per teclat — el mètode d'autenticació alternatiu que utilitzen alguns servidors SSH (incloses algunes configuracions corporatives antigues). Els agents que treballen en hosts SSH remots tenen menys probabilitats d'experimentar fallades d'autenticació.

Publicació original: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
