---
title: "WinApp VS Code-extensie: Windows-apps Uitvoeren, Debuggen en Inpakken Zonder de Editor te Verlaten"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "De WinApp VS Code-extensie brengt de volledige Windows App Development CLI direct naar VS Code — voer WPF, WinUI, .NET en C++ apps uit, debug ze met pakketidentiteit, en pak ze in en teken ze zonder Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

Als je ooit hebt geprobeerd een Windows-app te bouwen in VS Code, ken je dat moment. Je werkt lekker door, bewerkt code in je favoriete editor — en dan heb je plotseling pakketidentiteit nodig voor een Windows API. Of moet je een MSIX aanmaken. Of een pakket ondertekenen. En voor je het weet open je Visual Studio, of zoek je om 23 uur naar "msix packaging without visual studio".

Die wrijving is nu weg. De [WinApp VS Code-extensie](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) is in publieke preview — en het is de volledige [Windows App Development CLI](https://github.com/microsoft/WinAppCli) direct geïntegreerd in VS Code. Geen aparte installatie, Visual Studio niet vereist.

## Pakketidentiteit Met F5

Het probleem met Windows API's — notificaties, achtergrondtaken, on-device AI-functies, share targets — veel ervan vereisen dat je app **pakketidentiteit** heeft. Zonder die identiteit werken die API's simpelweg niet.

Traditioneel betekende pakketidentiteit verkrijgen het bouwen van een volledige MSIX-installer of uitvoeren vanuit Visual Studio. De WinApp-extensie verandert dit volledig met een aangepast `winapp` debug-type.

Voeg dit toe aan je `launch.json`:

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

Druk op F5. De extensie vindt je build-uitvoer en manifest, geeft je app pakketidentiteit via `winapp run` en koppelt de debugger. Voor .NET-apps is dat `coreclr` (vereist C# Dev Kit). C/C++ gebruikt `cppvsdbg`. Node/Electron gebruikt de ingebouwde debugger.

Je kunt een `preLaunchTask` instellen zodat het project automatisch wordt gebouwd voor elke F5-druk — dezelfde build-and-launch-workflow als Visual Studio, maar dan in VS Code.

## Alles in het Opdrachtenpalet

Open `Ctrl+Shift+P`, typ `WinApp` — en je krijgt de volledige toolkit:

- **Initialize Project** — configureer je project met Windows SDK en/of Windows App SDK
- **Run Application** — starten als los-ingedeelde verpakte app met pakketidentiteit
- **Create MSIX Package** — app inpakken met certificaat- en runtime-opties
- **Update Manifest Assets** — alle vereiste app-pictogrammen automatisch genereren vanuit één bronafbeelding
- **Generate / Install Certificate** — beheer van ontwikkelingscertificaten
- **Sign Package** — een MSIX of uitvoerbaar bestand ondertekenen
- **Run SDK Tool** — `makeappx`, `signtool`, `mt` of `makepri` direct uitvoeren

WinApp CLI hoeft ook niet apart geïnstalleerd te worden. Het zit meegeleverd bij de extensie.

## Werkt Met Meerdere Frameworks

Dit is niet alleen een hulpmiddel voor .NET WPF/WinUI. De extensie werkt met:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Die breedte is bewust. VS Code is waar web- en cross-platform-ontwikkelaars thuishoren. Als je een Tauri- of Electron-app bouwt die Windows-packaging nodig heeft, dekt deze extensie je zonder dat je Visual Studio hoeft te adopteren.

## Waarom Dit Belangrijk Is voor .NET-ontwikkelaars

Ik werk veel in VS Code — daar schrijf ik Markdown, beheer ik configuraties, bewerk ik kleine projecten en voer ik terminals uit. Maar voor .NET Windows-desktopwerk was Visual Studio de enige echte optie zodra je iets nodig had met packaging.

Deze extensie sluit die kloof. Je kunt nu een volledige .NET Windows-desktopwerk-cyclus hebben — bewerken, bouwen, uitvoeren met pakketidentiteit, debuggen, inpakken, ondertekenen — zonder VS Code te verlaten. Dat is een echte verbetering van de werkkwaliteit.

## Aan de Slag

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Of zoek naar **WinApp** in de Extensions-weergave (`Ctrl+Shift+X`).

Vereisten:
- Windows 10 of later
- VS Code 1.109.0 of later
- De debugger-extensie voor de taal van je app

Lees de [volledige aankondiging van Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) voor meer details.

## Conclusie

De WinApp VS Code-extensie is een welkome aanvulling voor .NET Windows-desktopont-wikkelaars die in VS Code leven maar voor packaging-werk naar Visual Studio moesten overstappen. Pakketidentiteit met F5, MSIX-packaging vanuit het opdrachtenpalet, ingebouwd certificaatbeheer — dit is de juiste set functies.

Probeer het bij je volgende WPF- of WinUI-project. De wrijving die je altijd moest omzeilen is zojuist een stuk kleiner geworden.
