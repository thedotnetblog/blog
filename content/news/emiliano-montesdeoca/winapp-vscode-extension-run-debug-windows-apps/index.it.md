---
title: "Estensione WinApp per VS Code: Esegui, Esegui il Debug e Pacchettizza App Windows Senza Uscire dall'Editor"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "L'estensione WinApp per VS Code porta l'intera CLI di Sviluppo App Windows direttamente in VS Code — esegui, fai il debug con identità pacchetto, impacchetta e firma app Windows senza toccare Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Se hai mai provato a sviluppare un'app Windows in VS Code, conosci già quel momento. Stai lavorando in pieno flusso, modificando codice nel tuo editor preferito — e improvvisamente hai bisogno di identità pacchetto per un'API Windows. O devi creare un MSIX. O firmare un pacchetto. E ti ritrovi ad aprire Visual Studio, o a cercare su Google "msix packaging without visual studio" alle 23.

Quella frizione non esiste più. L'[estensione WinApp per VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) è in preview pubblica — ed è la [CLI di Sviluppo App Windows](https://github.com/microsoft/WinAppCli) completa integrata direttamente in VS Code. Nessuna installazione separata, nessun Visual Studio richiesto.

## Identità Pacchetto da F5

Il problema con le API Windows — notifiche, attività in background, funzionalità AI on-device, share targets — molte richiedono che la tua app abbia **identità pacchetto**. Senza di essa, quelle API semplicemente non funzionano.

Ottenere l'identità pacchetto tradizionalmente significava costruire un installer MSIX completo o eseguire da Visual Studio. L'estensione WinApp cambia tutto questo con un tipo di debug `winapp` personalizzato.

Aggiungi questo al tuo `launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

Premi F5. L'estensione individua il tuo build output e il manifest, assegna alla tua app l'identità pacchetto tramite `winapp run`, e collega il debugger. Per le app .NET è `coreclr` (richiede C# Dev Kit). C/C++ usa `cppvsdbg`. Node/Electron usa il debugger integrato.

Puoi configurare un `preLaunchTask` per far compilare automaticamente il progetto prima di ogni F5 — stesso flusso build-and-launch di Visual Studio, ma in VS Code.

## Tutto nella Palette dei Comandi

Apri `Ctrl+Shift+P`, digita `WinApp`, e ottieni il toolkit completo:

- **Initialize Project** — configura il progetto con Windows SDK e/o Windows App SDK
- **Run Application** — avvia come app pacchettizzata con identità pacchetto
- **Create MSIX Package** — impacchetta l'app con opzioni di certificato e runtime
- **Update Manifest Assets** — genera automaticamente tutte le icone necessarie da un'immagine sorgente
- **Generate / Install Certificate** — gestione certificati di sviluppo
- **Sign Package** — firma un MSIX o un eseguibile
- **Run SDK Tool** — esegui `makeappx`, `signtool`, `mt` o `makepri` direttamente

Non è necessario installare nemmeno la CLI WinApp. È inclusa nell'estensione.

## Funziona con Più Framework

Non è solo uno strumento per .NET WPF/WinUI. L'estensione funziona con:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Questa ampiezza è deliberata. VS Code è dove vivono gli sviluppatori web e cross-platform. Se stai sviluppando un'app Tauri o Electron che ha bisogno di packaging Windows, questa estensione ti copre senza dover adottare Visual Studio.

## Perché È Importante per gli Sviluppatori .NET

Lavoro molto in VS Code — è dove scrivo Markdown, gestisco configurazioni, modifico piccoli progetti ed eseguo terminali. Ma per lo sviluppo desktop Windows in .NET, Visual Studio è stata l'unica opzione reale nel momento in cui hai bisogno di qualcosa legato al packaging.

Questa estensione colma quel divario. Ora puoi avere un ciclo di sviluppo desktop Windows in .NET completo — modifica, compilazione, esecuzione con identità pacchetto, debug, packaging, firma — senza uscire da VS Code. È un genuino miglioramento della qualità del lavoro.

## Per Iniziare

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Oppure cerca **WinApp** nella vista Estensioni (`Ctrl+Shift+X`).

Requisiti:
- Windows 10 o successivo
- VS Code 1.109.0 o successivo
- L'estensione debugger per il linguaggio della tua app

Leggi l'[annuncio completo di Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) per maggiori dettagli.

## Conclusione

L'estensione WinApp per VS Code è una benvenuta aggiunta per gli sviluppatori di desktop Windows in .NET che vivono in VS Code ma hanno dovuto passare a Visual Studio per il lavoro di packaging. Identità pacchetto da F5, packaging MSIX dalla palette dei comandi, gestione certificati integrata — è il giusto insieme di funzionalità.

Provalo nel tuo prossimo progetto WPF o WinUI. La frizione che stavi aggirando è appena diventata molto più piccola.
