---
title: "Agent Skills in Visual Studio: Insegna a Copilot Come Lavora Davvero il Tuo Team"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio ora supporta gli Agent Skills — set di istruzioni riutilizzabili che insegnano a Copilot i flussi di lavoro specifici, gli standard di codice e le convenzioni del tuo team. Definiscili una volta, applicali automaticamente."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Una delle frustrazioni persistenti con gli assistenti di codifica AI: conoscono bene la programmazione generale ma non conoscono le convenzioni specifiche del *tuo* team, le tue API interne o i tuoi pattern preferiti. In ogni sessione, rispieghi il contesto. Agent Skills in Visual Studio è progettato per risolvere questo problema.

## Cosa Sono gli Agent Skills

Set di istruzioni riutilizzabili — definiti in file `SKILL.md` — che insegnano agli agenti Copilot come gestire compiti specifici. Definisci uno skill per "come eseguire la nostra pipeline di build", "come generare boilerplate per il nostro layer di servizi" o "la nostra checklist di revisione del codice". L'agente applica lo skill automaticamente quando è rilevante.

Questo non è un concetto nuovo (`.github/copilot-instructions.md` esiste già da un po'), ma l'integrazione di Visual Studio li rende oggetti di prima classe con un'interfaccia di discovery.

## Creazione di Skills in Visual Studio

Il flusso dell'interfaccia integrata: fai clic sull'icona degli strumenti in Copilot Chat, apri il pannello degli skills, fai clic su `+`. Scegli l'ambito globale (personale) o a livello di soluzione, scegli un nome e Visual Studio genera un template. La modalità Agent di Copilot può quindi aiutarti a compilare il template — usa l'agente per scrivere lo skill per l'agente.

Attualmente nel canale Insiders, presto disponibile in Release.

Puoi anche creare skills manualmente:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Posizioni di Discovery

Gli skills vengono scoperti automaticamente dai percorsi standard:

**A livello di soluzione (condiviso tramite repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Globale/personale (il tuo profilo utente, disponibile ovunque):** `~/.copilot/skills/`, `~/.agents/skills/`

Il supporto multi-posizione significa che la stessa convenzione funziona con GitHub Copilot, Claude Code e altri framework di agenti — definisci i tuoi skills una volta, usali ovunque.

## Il Formato

Gli skills seguono il formato [agentskills.io/specification](https://agentskills.io/specification) — una specifica basata su Markdown leggibile sia dagli esseri umani che dalle macchine. Puoi includere script, template ed esempi accanto al `SKILL.md`.

## Valore Pratico

La vera potenza non sta nelle singole funzionalità — sta nella combinazione di skills condivisi dal team (tramite `.github/skills/`) e skills personali (tramite `~/.agents/skills/`). Gli skills del team codificano come la tua organizzazione fa le cose. Gli skills personali codificano come lavori specificatamente tu. L'agente ottiene entrambi i contesti automaticamente.

Per le organizzazioni che già usano intensamente Copilot, questo è un passo significativo verso rendere lo strumento veramente consapevole delle convenzioni specifiche del tuo codebase piuttosto che dare consigli generici.

Post originale: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
