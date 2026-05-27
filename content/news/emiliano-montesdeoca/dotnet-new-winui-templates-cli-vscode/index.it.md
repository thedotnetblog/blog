---
title: "dotnet new WinUI: Crea app Windows senza toccare Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "I template di progetto WinUI ora funzionano con dotnet new — app vuote, pattern NavigationView e altro. Supporto VS Code, nessun Visual Studio richiesto, con impostazioni predefinite Fluent Design incluse."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

Lo sviluppo WinUI richiedeva Visual Studio. Questo sta cambiando: Microsoft ha pubblicato template open source di progetti ed elementi per WinUI che funzionano con `dotnet new`, portando lo sviluppo di app Windows nel workflow standard della CLI.

## Iniziare in tre comandi

```shell
# Installare i template
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Creare un'app NavigationView
dotnet new winui-navview -n MyApp

# Eseguirla
cd MyApp
dotnet run
```

Nessun Visual Studio, nessuna configurazione manuale del progetto. L'app si esegue con `dotnet run`.

## Cosa è incluso

**Template vuoto** (`dotnet new winui`) — un punto di partenza moderno con una barra del titolo Fluent già configurata, icona app predefinita aggiornata con asset `.ico`, e corrette impostazioni predefinite per la modalità chiara/scura. Meglio del vecchio template vuoto che ti lasciava a configurare le basi da solo.

**Template NavigationView** (`dotnet new winui-navview`) — il pattern di navigazione master-detail, completamente configurato con un NavigationView, barra del titolo moderna e struttura di navigazione multipagina. Segue la siluetta standard delle app Windows per applicazioni basate sulla navigazione. Se stai costruendo qualcosa con navigazione laterale, inizia da qui.

Entrambi i template seguono le [siluette delle app Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — moderni pattern Fluent Design per layout, navigazione e struttura visiva — già pronti all'uso.

## Perché è importante per gli sviluppatori che non usano Visual Studio

Gli sviluppatori WinUI che usano VS Code, Rider o strumenti da riga di comando sono stati penalizzati. I template Visual Studio esistenti non erano utilizzabili fuori da VS — bisognava ricreare manualmente la struttura del progetto e configurare le basi.

Questi template sono open source (vedi [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), sviluppati dai [feedback della community](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), e disponibili ora. Il supporto Visual Studio è in corso — questi stessi template funzioneranno anche lì eventualmente.

Per i team che vogliono automatizzare la configurazione dei progetti WinUI, integrarla nella CI, o semplicemente usare un editor diverso da Visual Studio, questo è un miglioramento significativo.

Post originale: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
