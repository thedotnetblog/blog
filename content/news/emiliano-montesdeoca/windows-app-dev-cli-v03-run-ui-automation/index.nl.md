---
title: "Windows App Dev CLI v0.3: F5 vanuit de terminal en UI Automation voor agenten"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 brengt winapp run voor debug-launches vanuit de terminal, winapp ui voor UI-automatisering en een nieuw NuGet-pakket dat dotnet run laat werken met gepackagede apps."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

De F5-ervaring in Visual Studio is fantastisch. Maar VS openen alleen om een gepackagede Windows-app te starten en te debuggen — of dat nu in een CI-pipeline is, een geautomatiseerde workflow, of wanneer een AI-agent de tests uitvoert — is te veel gevraagd.

Windows App Development CLI v0.3 is [net uitgekomen](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) en pakt dit direct aan met twee hoofdfuncties: `winapp run` en `winapp ui`.

## winapp run: F5 vanuit overal

`winapp run` neemt een ongepackagede app-map en een manifest, en doet alles wat VS doet bij een debug-launch: registreert een loose package, start de app op en bewaart de `LocalState` tussen re-deploys.

```bash
# Bouw de app, voer hem dan uit als gepackagede app
winapp run ./bin/Debug
```

Werkt voor WinUI, WPF, WinForms, Console, Avalonia en meer. De modi zijn ontworpen voor zowel developers als geautomatiseerde workflows:

- **`--detach`**: Start op en geeft meteen de controle terug aan de terminal. Perfect voor CI.
- **`--unregister-on-exit`**: Ruimt het geregistreerde package op bij het sluiten van de app.
- **`--debug-output`**: Legt `OutputDebugString`-berichten en uitzonderingen real-time vast.

## Nieuw NuGet-pakket: dotnet run voor gepackagede apps

Voor .NET-developers is er een nieuw NuGet-pakket: `Microsoft.Windows.SDK.BuildTools.WinApp`. Na installatie beheert `dotnet run` de gehele inner loop: bouwen, een loose-layout package voorbereiden, registreren bij Windows en starten — alles in één stap.

```bash
winapp init
# of
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI Automation vanuit de commandoregel

Dit is de functie die agentische scenario's mogelijk maakt. `winapp ui` biedt volledige UI Automation-toegang tot elke actieve Windows-app — WPF, WinForms, Win32, Electron, WinUI3 — direct vanuit de terminal.

Wat mogelijk is:

- Alle vensters op het hoogste niveau weergeven
- De volledige UI Automation-boom van een venster doorlopen
- Elementen zoeken op naam, type of automatiserings-ID
- Klikken, aanroepen en waarden instellen
- Screenshots maken
- Wachten op het verschijnen van elementen — ideaal voor testsynchronisatie

`winapp ui` combineren met `winapp run` geeft een complete build → starten → verifiëren workflow vanuit de terminal. Een agent kan de app uitvoeren, de UI-status inspecteren, programmatisch interageren en het resultaat valideren.

## Andere nieuwigheden

- **`winapp unregister`**: Verwijdert een sideloaded package na gebruik.
- **`winapp manifest add-alias`**: Voegt een alias toe om de app op naam te starten vanuit de terminal.
- **Tab-aanvulling**: Configureer PowerShell-aanvulling met één commando.

## Hoe te verkrijgen

```bash
winget install Microsoft.WinAppCli
# of
npm install -g @microsoft/winappcli
```

De CLI is in publieke preview. Bekijk de [GitHub-repository](https://github.com/microsoft/WinAppCli) voor volledige documentatie en de [originele aankondiging](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) voor alle details.
