---
title: "Windows App Dev CLI v0.3: F5 dal terminale e UI Automation per gli agenti"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 porta winapp run per avviare e fare debug dal terminale, winapp ui per l'automazione dell'interfaccia e un nuovo pacchetto NuGet che fa funzionare dotnet run con le app pacchettizzate."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

L'esperienza F5 di Visual Studio è fantastica. Ma dover aprire VS solo per avviare e fare debug di un'app Windows pacchettizzata è eccessivo — che si tratti di una pipeline CI, di un workflow automatizzato o di un agente AI che esegue i test.

Windows App Development CLI v0.3 è [appena uscita](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) e lo affronta direttamente con due funzionalità principali: `winapp run` e `winapp ui`.

## winapp run: F5 da qualsiasi posto

`winapp run` prende una cartella di app non pacchettizzata e un manifesto, e fa tutto ciò che VS fa nel debug launch: registra un pacchetto loose, avvia l'app e preserva il `LocalState` tra i re-deploy.

```bash
# Compila l'app, poi avviala come app pacchettizzata
winapp run ./bin/Debug
```

Funziona per WinUI, WPF, WinForms, Console, Avalonia e altro. Le modalità sono pensate per sviluppatori e workflow automatizzati:

- **`--detach`**: Avvia e restituisce il controllo al terminale immediatamente. Perfetto per CI.
- **`--unregister-on-exit`**: Pulisce il pacchetto registrato alla chiusura dell'app.
- **`--debug-output`**: Cattura i messaggi `OutputDebugString` e le eccezioni in tempo reale.

## Nuovo pacchetto NuGet: dotnet run per le app pacchettizzate

Per gli sviluppatori .NET c'è un nuovo pacchetto NuGet: `Microsoft.Windows.SDK.BuildTools.WinApp`. Dopo l'installazione, `dotnet run` gestisce tutto l'inner loop: build, preparare un pacchetto loose-layout, registrare su Windows e avviare — tutto in un unico step.

```bash
winapp init
# o
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI Automation dalla riga di comando

Questa è la funzionalità che apre gli scenari agentici. `winapp ui` fornisce accesso completo UI Automation a qualsiasi app Windows in esecuzione — WPF, WinForms, Win32, Electron, WinUI3 — direttamente dal terminale.

Cosa si può fare:

- Elencare tutte le finestre di primo livello
- Navigare l'albero completo di UI Automation di una finestra
- Cercare elementi per nome, tipo o ID di automazione
- Cliccare, invocare e impostare valori
- Fare screenshot
- Attendere la comparsa di elementi — ideale per la sincronizzazione dei test

Combinare `winapp ui` con `winapp run` crea un workflow completo build → avvio → verifica dal terminale. Un agente può eseguire l'app, ispezionare lo stato dell'UI e validare il risultato.

## Altre novità

- **`winapp unregister`**: Rimuove un pacchetto sideloaded quando si è finito.
- **`winapp manifest add-alias`**: Aggiunge un alias per avviare l'app per nome dal terminale.
- **Tab completion**: Configura il completamento PowerShell con un singolo comando.

## Come ottenerlo

```bash
winget install Microsoft.WinAppCli
# o
npm install -g @microsoft/winappcli
```

La CLI è in preview pubblica. Il [repository su GitHub](https://github.com/microsoft/WinAppCli) ha la documentazione completa e l'[annuncio originale](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) ha tutti i dettagli.
