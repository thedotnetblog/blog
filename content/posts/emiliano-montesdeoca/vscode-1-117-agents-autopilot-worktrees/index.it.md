---
title: "VS Code 1.117: Gli Agent Stanno Ottenendo i Propri Branch Git e Io Sono Tutto a Favore"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 porta l'isolamento con worktree per le sessioni degli agent, la modalità Autopilot persistente e il supporto per i subagent. Il workflow di coding agentico è diventato molto più reale."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

La linea tra "assistente IA" e "compagno di squadra IA" continua ad assottigliarsi. VS Code 1.117 è appena uscito e le [note di rilascio complete](https://code.visualstudio.com/updates/v1_117) sono piene, ma la storia è chiara: gli agent stanno diventando cittadini di prima classe nel tuo workflow di sviluppo.

Ecco cosa conta davvero.

## La modalità Autopilot finalmente ricorda la tua preferenza

Prima, dovevi riattivare Autopilot ogni volta che iniziavi una nuova sessione. Fastidioso. Ora la tua modalità di permessi persiste tra le sessioni, e puoi configurare il valore predefinito.

L'Agent Host supporta tre configurazioni di sessione:

- **Default** — gli strumenti chiedono conferma prima di eseguire
- **Bypass** — approva tutto automaticamente
- **Autopilot** — completamente autonomo, risponde alle proprie domande e va avanti

Se stai creando un nuovo progetto .NET con migrazioni, Docker e CI — impostalo su Autopilot una volta e dimenticatene. Quella preferenza resta.

## Worktree e isolamento git per le sessioni degli agent

Questa è la grande novità. Le sessioni degli agent ora supportano l'isolamento completo con worktree e git. Questo significa che quando un agent lavora su un task, ottiene il proprio branch e la propria directory di lavoro. Il tuo branch principale resta intatto.

Ancora meglio — Copilot CLI genera nomi di branch significativi per queste sessioni worktree. Basta con `agent-session-abc123`. Ottieni qualcosa che descrive davvero cosa sta facendo l'agent.

Per gli sviluppatori .NET che gestiscono più feature branch o correggono bug mentre un lungo task di scaffolding è in esecuzione, questo è un punto di svolta. Puoi avere un agent che costruisce i tuoi controller API in un worktree mentre tu fai debug di un problema nel service layer in un altro. Nessun conflitto. Nessun stashing. Nessun casino.

## Subagent e team di agent

L'Agent Host Protocol ora supporta i subagent. Un agent può avviare altri agent per gestire parti di un task. Pensalo come delegare — il tuo agent principale coordina, e agent specializzati si occupano dei pezzi.

Siamo ancora all'inizio, ma il potenziale per i workflow .NET è ovvio. Immagina un agent che gestisce le tue migrazioni EF Core mentre un altro configura i tuoi test di integrazione. Non siamo ancora completamente lì, ma il fatto che il supporto al protocollo arrivi ora significa che gli strumenti seguiranno velocemente.

## L'output del terminale incluso automaticamente quando gli agent inviano input

Piccolo ma significativo. Quando un agent invia input al terminale, l'output del terminale viene ora automaticamente incluso nel contesto. Prima, l'agent doveva fare un turno extra solo per leggere cosa era successo.

Se hai mai visto un agent eseguire `dotnet build`, fallire, e poi fare un altro giro solo per vedere l'errore — quella frizione è sparita. Vede l'output immediatamente e reagisce.

## L'app Agents su macOS si aggiorna automaticamente

L'app standalone Agents su macOS ora si aggiorna automaticamente. Basta scaricare manualmente nuove versioni. Resta semplicemente aggiornata.

## Le cose più piccole che vale la pena sapere

- Gli **hover su package.json** ora mostrano sia la versione installata che l'ultima disponibile. Utile se gestisci strumenti npm insieme ai tuoi progetti .NET.
- Le **immagini nei commenti JSDoc** vengono renderizzate correttamente negli hover e nei completamenti.
- Le **sessioni Copilot CLI** ora indicano se sono state create da VS Code o esternamente — comodo quando salti tra i terminali.
- **Copilot CLI, Claude Code e Gemini CLI** sono riconosciuti come tipi di shell. L'editor sa cosa stai eseguendo.

## Il punto chiave

VS Code 1.117 non è un dump di feature appariscenti. È infrastruttura. Isolamento con worktree, permessi persistenti, protocolli per subagent — questi sono i mattoni per un workflow dove gli agent gestiscono task reali e paralleli senza pestare il tuo codice.

Se stai sviluppando con .NET e non ti sei ancora buttato nel workflow agentico, onestamente, ora è il momento di iniziare.
