---
title: "Windows App Dev CLI v0.3: F5 des del terminal i automatització de UI per a agents"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 arriba amb winapp run per llançar i depurar des del terminal, winapp ui per a l'automatització de la interfície, i un paquet NuGet que fa funcionar dotnet run amb apps empaquetades."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [feu clic aquí]({{< ref "index.md" >}}).*

L'experiència F5 de Visual Studio és fantàstica. Però haver d'obrir VS només per llançar i depurar una app Windows empaquetada és excessiu quan estàs en un pipeline de CI, executant un workflow automatitzat, o quan un agent d'IA fa les proves.

Windows App Development CLI v0.3 acaba de [sortir](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) i ho aborda directament amb dues funcions destacades: `winapp run` i `winapp ui`.

## winapp run: F5 des de qualsevol lloc

`winapp run` pren una carpeta d'app sense empaquetar i un manifest, i fa tot el que VS fa en un debug launch: registra un paquet loose, llança l'app i preserva el `LocalState` entre re-deploys.

```bash
winapp run ./bin/Debug
```

Funciona per a WinUI, WPF, WinForms, Console, Avalonia i més. Els modes estan pensats per a developers i workflows automatitzats:

- **`--detach`**: Llança i retorna el control al terminal immediatament.
- **`--unregister-on-exit`**: Neteja el paquet registrat en tancar l'app.
- **`--debug-output`**: Captura missatges `OutputDebugString` i excepcions en temps real.

## Nou paquet NuGet: dotnet run per a apps empaquetades

Per a developers .NET hi ha un nou paquet NuGet: `Microsoft.Windows.SDK.BuildTools.WinApp`. Afegeix-lo al projecte i `dotnet run` gestiona tot l'inner loop: build, preparar un paquet loose-layout, registrar a Windows i llançar — tot en un pas.

```bash
winapp init
# o
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI Automation des de la línia de comandes

`winapp ui` et dóna accés complet d'UI Automation a qualsevol app Windows en execució — WPF, WinForms, Win32, Electron, WinUI3. Pots llistar finestres, navegar l'arbre de UI Automation, trobar elements, fer clics, prendre captures de pantalla i esperar l'aparició d'elements.

Combina `winapp ui` amb `winapp run` i tens un workflow complet build → llançar → verificar des del terminal. Un agent pot executar la teva app, inspeccionar l'estat de la UI i validar el resultat.

## Altres novetats

- **`winapp unregister`**: Elimina un paquet sideloaded quan acabes.
- **`winapp manifest add-alias`**: Afegeix un àlies per llançar l'app per nom des del terminal.
- **Tab completion**: Configura completat amb una sola comanda per a PowerShell.

## Com obtenir-ho

```bash
winget install Microsoft.WinAppCli
# o
npm install -g @microsoft/winappcli
```

Consulta el [repositori a GitHub](https://github.com/microsoft/WinAppCli) per a documentació completa i l'[anunci original](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) per a tots els detalls.
