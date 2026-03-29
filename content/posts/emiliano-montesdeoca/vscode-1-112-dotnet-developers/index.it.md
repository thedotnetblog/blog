---
title: "VS Code 1.112: Cosa dovrebbe davvero interessare agli sviluppatori .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 è appena uscito ed è pieno di upgrade per gli agenti, un debugger browser integrato, sandboxing MCP e supporto monorepo. Ecco cosa conta davvero se sviluppi con .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 è appena atterrato, e onestamente? Questo colpisce diversamente se passi le tue giornate nel mondo .NET. C'è molto nelle [note di rilascio ufficiali](https://code.visualstudio.com/updates/v1_112), ma lascia che ti risparmi un po' di scrolling e mi concentri su quello che conta davvero per noi.

## Copilot CLI è diventato molto più utile

Il grande tema di questo rilascio è l'**autonomia dell'agente** — dare a Copilot più spazio per fare il suo lavoro senza che tu supervisioni ogni passo.

### Steering e coda dei messaggi

Conosci quel momento in cui Copilot CLI è a metà di un task e ti rendi conto che hai dimenticato di menzionare qualcosa? Prima, dovevi aspettare. Ora puoi inviare messaggi mentre una richiesta è ancora in corso — sia per dirigere la risposta corrente che per mettere in coda istruzioni di follow-up.

Questo è enorme per quei task di scaffolding `dotnet` più lunghi dove stai guardando Copilot configurare un progetto e pensi "oh aspetta, mi serve anche MassTransit lì dentro."

### Livelli di permessi

Questo è quello che mi entusiasma di più. Le sessioni Copilot CLI ora supportano tre livelli di permessi:

- **Permessi predefiniti** — il flusso solito dove gli strumenti chiedono conferma prima di eseguire
- **Bypass approvazioni** — auto-approva tutto e riprova in caso di errore
- **Autopilota** — completamente autonomo: approva strumenti, risponde alle proprie domande e continua finché il task non è completo

Se stai facendo qualcosa come creare una nuova API ASP.NET Core con Entity Framework, migrazioni e Docker setup — la modalità Autopilota significa che descrivi quello che vuoi e vai a prendere un caffè. Lo capirà da solo.

Puoi abilitare l'Autopilota con l'impostazione `chat.autopilot.enabled`.

### Anteprima delle modifiche prima della delega

Quando deleghi un task a Copilot CLI, crea un worktree. Prima, se avevi modifiche non committate, dovevi controllare il Source Control per vedere cosa sarebbe stato influenzato. Ora la vista Chat mostra le modifiche pendenti proprio lì prima che tu decida se copiarle, spostarle o ignorarle.

Piccola cosa, ma ti salva da quel momento "aspetta, cosa avevo in staging?"

## Debug delle web app senza lasciare VS Code

Il browser integrato ora supporta il **debugging completo**. Puoi impostare breakpoint, fare step through del codice e ispezionare variabili — tutto dentro VS Code. Basta passare a Edge DevTools.

C'è un nuovo tipo di debug `editor-browser`, e se hai già configurazioni di lancio `msedge` o `chrome` esistenti, migrare è semplice come cambiare il campo `type` nel tuo `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Per gli sviluppatori Blazor, questo è un game changer. Stai già eseguendo `dotnet watch` nel terminale — ora anche il tuo debugging resta nella stessa finestra.

Il browser ha anche ottenuto livelli di zoom indipendenti (finalmente), menu contestuali con clic destro appropriati, e lo zoom viene ricordato per sito web.

## Sandboxing dei server MCP

Questo conta più di quanto potresti pensare. Se usi server MCP — magari ne hai configurato uno personalizzato per le tue risorse Azure o query al database — giravano con gli stessi permessi del tuo processo VS Code. Questo significa accesso completo al tuo filesystem, rete, tutto.

Ora puoi metterli in sandbox. Nel tuo `mcp.json`:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Quando un server sandboxato ha bisogno di accedere a qualcosa che non ha, VS Code ti chiede di concedere il permesso. Molto meglio dell'approccio "speriamo che nessuno faccia nulla di strano".

> **Nota:** Il sandboxing è disponibile su macOS e Linux per ora. Il supporto Windows è in arrivo — scenari remoti come WSL funzionano però.

## Scoperta delle personalizzazioni nei monorepo

Se lavori in un monorepo (e siamo onesti, molte soluzioni .NET enterprise finiscono per diventarne uno), questo risolve un vero punto dolente.

Prima, se aprivi una sottocartella del tuo repo, VS Code non trovava il tuo `copilot-instructions.md`, `AGENTS.md` o skills personalizzati alla radice del repository. Ora con l'impostazione `chat.useCustomizationsInParentRepositories`, risale fino alla radice `.git` e scopre tutto.

Questo significa che il tuo team può condividere istruzioni per agenti, file di prompt e strumenti personalizzati tra tutti i progetti in un monorepo senza che tutti debbano aprire la cartella radice.

## /troubleshoot per il debugging degli agenti

Hai mai configurato istruzioni personalizzate o skills e ti sei chiesto perché non vengono rilevati? Il nuovo skill `/troubleshoot` legge i log di debug dell'agente e ti dice cosa è successo — quali strumenti sono stati usati o saltati, perché le istruzioni non sono state caricate, e cosa sta causando risposte lente.

Abilitalo con:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Poi scrivi semplicemente `/troubleshoot why is my custom skill not loading?` nella chat.

Puoi anche esportare e importare questi log di debug ora, il che è ottimo per condividerli con il team quando qualcosa non funziona come previsto.

## Supporto file immagine e binari

Gli agenti possono ora leggere file immagine dal disco e file binari nativamente. I file binari vengono presentati in formato hexdump, e gli output delle immagini (come screenshot dal browser integrato) appaiono in una vista carousel.

Per gli sviluppatori .NET, pensa: incolla uno screenshot di un bug UI nella chat e fai capire all'agente cosa c'è che non va, o fagli analizzare l'output del rendering di un componente Blazor.

## Riferimenti automatici ai simboli

Piccolo miglioramento di qualità della vita: quando copi il nome di un simbolo (una classe, metodo, ecc.) e lo incolli nella chat, VS Code ora lo converte automaticamente in un riferimento `#sym:Name`. Questo dà all'agente il contesto completo su quel simbolo senza che tu debba aggiungerlo manualmente.

Se vuoi testo semplice, usa `Ctrl+Shift+V`.

## I plugin possono ora essere abilitati/disabilitati

Prima, disabilitare un server MCP o plugin significava disinstallarlo. Ora puoi attivarli e disattivarli — sia globalmente che per workspace. Clic destro nella vista Estensioni o nella vista Personalizzazioni e hai fatto.

I plugin da npm e pypi possono anche auto-aggiornarsi ora, anche se chiederanno approvazione prima poiché gli aggiornamenti significano eseguire nuovo codice sulla tua macchina.

## Per concludere

VS Code 1.112 sta chiaramente spingendo forte sull'esperienza agent — più autonomia, debugging migliore, sicurezza più stretta. Per gli sviluppatori .NET, il debugging del browser integrato e i miglioramenti di Copilot CLI sono le funzionalità di punta.

Se non hai ancora provato a eseguire una sessione completa di Copilot CLI in modalità Autopilota per un progetto .NET, questo rilascio è un buon momento per iniziare. Ricorda solo di impostare i tuoi permessi e lasciare cuocere.

[Scarica VS Code 1.112](https://code.visualstudio.com/updates/v1_112) o aggiorna dall'interno di VS Code tramite **Aiuto > Controlla aggiornamenti**.
