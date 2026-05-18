---
title: "Extensió WinApp per a VS Code: Executa, Depura i Empaqueta Apps Windows Sense Sortir de l'Editor"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "L'extensió WinApp per a VS Code porta el CLI complet de Desenvolupament d'Apps Windows directament a VS Code — executa, depura amb identitat de paquet, empaqueta i signa apps Windows sense tocar Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Si alguna vegada has intentat construir una app Windows en VS Code, ja coneixes aquell moment. Estàs treballant fluïdament, editant codi al teu editor preferit, i de sobte necessites identitat de paquet per a una API de Windows. O necessites crear un MSIX. O signar un paquet. I de cop estàs obrint Visual Studio, o buscant a Google "msix packaging without visual studio" a les 11 de la nit.

Aquella fricció ja no existeix. L'[extensió WinApp per a VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) és en preview pública — i és el [CLI de Desenvolupament d'Apps Windows](https://github.com/microsoft/WinAppCli) complet integrat directament a VS Code. Sense instal·lació separada, sense Visual Studio requerit.

## Identitat de Paquet des de F5

El tema amb les APIs de Windows — notificacions, tasques en segon pla, funcions d'IA on-device, share targets — és que moltes requereixen que la teva app tingui **identitat de paquet**. Sense ella, aquestes APIs simplement no funcionen.

Aconseguir identitat de paquet tradicionalment significava construir un instal·lador MSIX complet o executar des de Visual Studio. L'extensió WinApp canvia això completament amb un tipus de depuració `winapp` personalitzat.

Afegeix això al teu `launch.json`:

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

Prem F5. L'extensió localitza el teu build output i manifest, dona a la teva app identitat de paquet via `winapp run`, i adjunta el depurador. Per a apps .NET és `coreclr` (requereix C# Dev Kit). C/C++ usa `cppvsdbg`. Node/Electron usa el depurador incorporat.

Pots configurar un `preLaunchTask` perquè el projecte es compili automàticament abans de cada F5 — mateix flux que Visual Studio, però a VS Code.

## Tot a la Paleta de Comandes

Obre `Ctrl+Shift+P`, escriu `WinApp`, i obtens el kit d'eines complet:

- **Initialize Project** — configura el teu projecte amb Windows SDK i/o Windows App SDK
- **Run Application** — llança com a app empaquetada amb identitat de paquet
- **Create MSIX Package** — empaqueta la teva app amb opcions de certificat i runtime
- **Update Manifest Assets** — genera automàticament totes les icones necessàries des d'una imatge font
- **Generate / Install Certificate** — gestió de certificats de desenvolupament
- **Sign Package** — signa un MSIX o executable
- **Run SDK Tool** — executa `makeappx`, `signtool`, `mt` o `makepri` directament

No cal instal·lar el CLI de WinApp tampoc. Ve inclòs amb l'extensió.

## Funciona amb Múltiples Frameworks

No és només una eina per a .NET WPF/WinUI. L'extensió funciona amb:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Aquesta amplitud és deliberada. VS Code és on viuen els desenvolupadors web i multiplataforma. Si estàs construint una app Tauri o Electron que necessita empaquetament Windows, aquesta extensió t'ho cobreix sense que hagis d'adoptar Visual Studio.

## Per Què Importa per als Desenvolupadors .NET

Treballo molt en VS Code — és on escric Markdown, gestiono configuracions, edito projectes petits i executo terminals. Però per al treball d'escriptori Windows en .NET, Visual Studio ha estat l'única opció real en el moment que necessites qualsevol cosa relacionada amb empaquetament.

Aquesta extensió tanca aquella bretxa. Ara pots tenir un cicle complet de desenvolupament d'escriptori Windows en .NET — editar, compilar, executar amb identitat de paquet, depurar, empaquetar, signar — sense sortir de VS Code. És una millora genuïna de qualitat de vida.

## Primers Passos

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

O cerca **WinApp** a la vista d'Extensions (`Ctrl+Shift+X`).

Requisits:
- Windows 10 o posterior
- VS Code 1.109.0 o posterior
- L'extensió de depurador per al llenguatge de la teva app

Llegeix l'[anunci complet de Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) per a més detalls.

## Conclusió

L'extensió WinApp per a VS Code és una benvinguda addició per als desenvolupadors d'escriptori Windows en .NET que viuen a VS Code però han hagut de canviar a Visual Studio per al treball d'empaquetament. Identitat de paquet des de F5, empaquetament MSIX des de la paleta de comandes, gestió de certificats integrada — és el conjunt correcte de funcionalitats.

Prova-la al teu pròxim projecte WPF o WinUI. La fricció que has estat evitant acaba de reduir-se considerablement.
