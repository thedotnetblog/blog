---
title: "68 Minuts al Dia Reexplicant Codi a Copilot? Hi Ha una Solució"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "El context rot és real — el teu agent d'IA es deriva després de 30 torns, i pagues l'impost de la compactació cada hora. auto-memory dona a GitHub Copilot CLI una memòria quirúrgica sense cremar milers de tokens."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Saps aquell moment en què la teva sessió de Copilot arriba a `/compact` i l'agent oblida completament què estaves fent? Passes els cinc minuts següents reexplicant l'estructura de carpetes, el test que falla i les tres aproximacions que ja has provat. I després torna a passar. I una altra vegada.

Desi Villanueva ho va mesurar: **68 minuts al dia** — només en reorientació. No escrivint codi. No revisant PRs. Només posant la IA al corrent del que ja sabia.

Resulta que hi ha una raó concreta per això, i una solució concreta.

## La mentida de la finestra de context

El teu agent ve amb un número gran a la capsa. 200K tokens. Sona massiu. A la pràctica és un sostre, no una garantia.

Aquí tens la matemàtica real:

- 200K de context total
- Menys uns 65K per a eines MCP carregades a l'arrencada (~33%)
- Menys uns 10K per a fitxers d'instruccions com `AGENTS.md` o `copilot-instructions.md`

Això et deixa aproximadament **125K abans d'escriure ni una paraula**. I encara va a pitjor — els LLM no es degraden amb gràcia a mesura que el context s'omple. Xoquen amb una paret al voltant del 60% de la capacitat. El model comença a perdre coses esmentades fa 30 torns, contradiu respostes anteriors, i al·lucina noms de fitxer que havia dit amb total confiança fa 10 minuts. La indústria anomena això el problema de "lost in the middle".

Límit efectiu: **45K tokens** abans que la qualitat es degradi. Això són potser 20-30 torns de conversa activa abans que l'agent comenci a desviar-se. Per això estàs fent `/compact` cada 45 minuts — no perquè hagis omplert 200K tokens, sinó perquè el model ja està prou degradat a 120K.

## L'impost de la compactació

Cada `/compact` et fa perdre l'estat de flux. Estàs immers en una sessió de depuració. El context compartit s'ha anat construint durant 30 minuts. L'agent coneix l'estructura de fitxers, el test que falla i la hipòtesi. Llavors arriba l'avís.

- Ignora'l → l'agent es torna progressivament més tonto i comença a al·lucinar l'estat antic
- Executa `/compact` → l'agent obté un resum de dos paràgrafs d'una investigació de 30 minuts

En qualsevol dels dos casos perds. En qualsevol dels dos casos estàs narrant el teu propi projecte com si fos un nou empleat el primer dia.

La part cruel? **La memòria ja existeix**. Copilot CLI escriu cada sessió a una base de dades SQLite local a `~/.copilot/session-store.db` — cada fitxer tocat, cada torn, cada punt de control. Tot és al disc. L'agent simplement no ho pot llegir.

## auto-memory: una capa de recuperació, no un sistema de memòria

Aquesta és la idea clau darrere de [auto-memory](https://github.com/dezgit2025/auto-memory): no construeixis un sistema de memòria nou — construeix una capa de consulta només lectura sobre la que ja existeix.

```bash
pip install auto-memory
```

Unes 1.900 línies de Python. Zero dependències. S'instal·la en 30 segons.

En lloc d'inundar el context amb resultats de grep, li dones a l'agent accés quirúrgic al que realment importa:

| Operació | Tokens | Què obtens |
|----------|--------|------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 resultats, la majoria irrellevants |
| `find . -name "*.py"` | ~2,000 | Tots els fitxers Python, sense context |
| Reorientació de l'agent | ~2,000 | Tu explicant allò que ja hauria de saber |
| **`auto-memory files --json --limit 10`** | **~50** | **Els 10 fitxers en què vas treballar ahir** |

Això és una millora de 200x. L'agent s'estalvia l'excavació arqueològica i va directament al que importa.

El flux recomanat: quan t'acostis al 50-70% d'ús del context, executa `/clear` i després demana: "revisa les últimes sessions que vam parlar del tema X". En lloc de cremar 12K tokens en cerques a cegues, auto-memory extreu el context rellevant en 50.

## Per què això importa als desenvolupadors .NET

Si fas servir GitHub Copilot CLI per a feina de .NET — scaffolding de serveis, depuració de consultes EF Core, iteració sobre components Blazor — el problema del context rot et pega igual de fort. Les solucions complexes amb múltiples projectes, biblioteques compartides i cadenes de crida profundes són exactament el tipus de codebase en què l'agent perd el fil més ràpid.

La guia d'instal·lació explica com apuntar-hi Copilot CLI. És una configuració d'una sola vegada.

Sincerament? Recuperar 68 minuts al dia no és un petit ajust de qualitat de vida. Això és gairebé 6 hores a la setmana.

## Resumint

El context rot és una restricció arquitectònica real, no un bug que es corregirà. auto-memory la rodeja donant al teu agent un mecanisme de recuperació barat i precís en lloc d'una reexploració costosa i sorollosa. Si fas desenvolupament seriós assistit per IA amb GitHub Copilot CLI, val la pena la instal·lació de 30 segons.

Fes-hi un cop d'ull: [auto-memory a GitHub](https://github.com/dezgit2025/auto-memory). Post original de Desi Villanueva: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).