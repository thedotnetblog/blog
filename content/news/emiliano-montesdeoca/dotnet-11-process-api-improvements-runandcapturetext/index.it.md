---
title: ".NET 11 finalmente risolve l'API dei Processi"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process riceve il suo aggiornamento più grande degli ultimi anni. RunAndCaptureTextAsync, KillOnParentExit, API SafeProcessHandle e controllo completo sul reindirizzamento degli handle standard — niente più boilerplate per i deadlock."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Ogni sviluppatore .NET che abbia mai avuto bisogno di avviare un processo e catturarne l'output ha scritto qualche variante dello stesso pericoloso boilerplate: lettura async da stdout, lettura async da stderr, `WaitForExitAsync`, senza dimenticare di svuotare entrambi gli stream altrimenti si va in deadlock. È una trappola ben nota che esiste da anni.

.NET 11 finalmente la risolve correttamente.

## RunAndCaptureTextAsync

L'aggiunta principale: un singolo metodo statico che avvia un processo, cattura stdout e stderr, e attende l'uscita senza deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Una sola chiamata. Nessuno svuotamento manuale degli stream. Nessun `WaitForExit` posizionato con cura. Se hai solo bisogno di eseguire qualcosa e ottenere il suo output, questa è l'API che vuoi.

C'è anche `Process.RunAsync` per il caso in cui vuoi aspettare l'uscita senza catturare l'output.

## KillOnParentExit

Un problema comune con i processi avviati: se il processo padre si arresta o viene terminato, i processi figli continuano a girare come orfani. `KillOnParentExit` ti permette di dichiarare all'avvio del processo che il processo figlio deve essere terminato quando il processo padre esce.

Questa è una funzionalità che esisteva in modi specifici per piattaforma (job objects su Windows, prctl su Linux) ma richiedeva p/invoke o librerie di terze parti per essere usata da .NET. Ora è una proprietà di prima classe su `ProcessStartInfo`.

## API Basate su SafeProcessHandle

La nuova superficie API leggera è costruita attorno a `SafeProcessHandle` piuttosto che alla classe `Process` completa. La classe `Process` completa porta molto stato ed è difficile da eliminare — il percorso `SafeProcessHandle` è più adatto al trimmer per le applicazioni che devono minimizzare le dimensioni dell'output (WASM, AOT nativo).

## Controllo Completo sull'Ereditarietà degli Handle

L'aggiornamento aggiunge anche un controllo granulare su quali handle un processo figlio eredita e come vengono reindirizzati gli handle standard. In precedenza potevi reindirizzare stdin/stdout/stderr ma non potevi specificare esattamente quali handle ereditare a livello di SO. Le nuove API espongono quel controllo.

## Perché È Importante

La classe `Process` è usata in tooling, sistemi di build, test runner e qualsiasi applicazione che invoca altri eseguibili. La vecchia superficie API risaliva a .NET Framework e mostrava la sua età. Non è un cambiamento che rompe la compatibilità — le vecchie API funzionano ancora — ma il nuovo codice dovrebbe preferire la nuova superficie.

Per le applicazioni trimmate o gli scenari di compilazione AOT, il percorso `SafeProcessHandle` è particolarmente benvenuto. La vecchia classe `Process` portava molto codice pesante di reflection che complicava il trimming.

Post originale: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
