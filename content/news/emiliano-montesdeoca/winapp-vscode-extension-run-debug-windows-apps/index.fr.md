---
title: "Extension WinApp pour VS Code : Exécutez, Déboguez et Empaquetez des Apps Windows Sans Quitter l'Éditeur"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "L'extension WinApp pour VS Code apporte l'intégralité du CLI de Développement d'Apps Windows directement dans VS Code — exécutez, déboguez avec identité de paquet, empaquetez et signez des apps Windows sans toucher à Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Si vous avez déjà essayé de développer une app Windows dans VS Code, vous connaissez ce moment. Vous travaillez en plein flux, éditant du code dans votre éditeur préféré — et soudain vous avez besoin d'une identité de paquet pour une API Windows. Ou de créer un MSIX. Ou de signer un paquet. Et vous vous retrouvez à ouvrir Visual Studio, ou à chercher "msix packaging without visual studio" à 23h.

Cette friction appartient au passé. L'[extension WinApp pour VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) est en preview publique — et c'est la [CLI de Développement d'Apps Windows](https://github.com/microsoft/WinAppCli) complète intégrée directement dans VS Code. Pas d'installation séparée, pas de Visual Studio requis.

## Identité de Paquet Depuis F5

Le problème avec les APIs Windows — notifications, tâches en arrière-plan, fonctionnalités d'IA on-device, share targets — beaucoup d'entre elles exigent que votre app ait une **identité de paquet**. Sans elle, ces APIs ne fonctionnent tout simplement pas.

Obtenir une identité de paquet signifiait traditionnellement construire un installateur MSIX complet ou lancer depuis Visual Studio. L'extension WinApp change cela complètement avec un type de débogage `winapp` personnalisé.

Ajoutez ceci à votre `launch.json` :

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

Appuyez sur F5. L'extension localise votre build output et votre manifeste, donne à votre app une identité de paquet via `winapp run`, et attache le débogueur. Pour les apps .NET, c'est `coreclr` (nécessite C# Dev Kit). C/C++ utilise `cppvsdbg`. Node/Electron utilise le débogueur intégré.

Vous pouvez configurer un `preLaunchTask` pour que le projet se compile automatiquement avant chaque F5 — le même flux build-and-launch que Visual Studio, mais dans VS Code.

## Tout dans la Palette de Commandes

Ouvrez `Ctrl+Shift+P`, tapez `WinApp`, et vous obtenez la boîte à outils complète :

- **Initialize Project** — configurer votre projet avec Windows SDK et/ou Windows App SDK
- **Run Application** — lancer comme app packagée avec identité de paquet
- **Create MSIX Package** — packager votre app avec options de certificat et runtime
- **Update Manifest Assets** — générer automatiquement toutes les icônes requises depuis une image source
- **Generate / Install Certificate** — gestion des certificats de développement
- **Sign Package** — signer un MSIX ou un exécutable
- **Run SDK Tool** — exécuter `makeappx`, `signtool`, `mt` ou `makepri` directement

Pas besoin d'installer la CLI WinApp non plus. Elle est incluse avec l'extension.

## Fonctionne Sur Plusieurs Frameworks

Ce n'est pas uniquement un outil .NET WPF/WinUI. L'extension fonctionne avec :

- **.NET** : WPF, WinForms, Console, WinUI 3
- **C/C++** : Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Cette étendue est délibérée. VS Code est l'environnement de prédilection des développeurs web et multiplateforme. Si vous construisez une app Tauri ou Electron qui nécessite un packaging Windows, cette extension vous couvre sans devoir adopter Visual Studio.

## Pourquoi C'est Important pour les Développeurs .NET

Je travaille beaucoup dans VS Code — c'est là où j'écris du Markdown, gère des configurations, édite de petits projets et lance des terminaux. Mais pour le développement de bureau Windows en .NET, Visual Studio était la seule vraie option dès qu'on avait besoin de quoi que ce soit lié au packaging.

Cette extension comble cette lacune. Vous pouvez désormais avoir un cycle complet de développement de bureau Windows en .NET — éditer, compiler, exécuter avec identité de paquet, déboguer, packager, signer — sans quitter VS Code. C'est une vraie amélioration de la qualité de vie.

## Pour Commencer

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Ou cherchez **WinApp** dans la vue Extensions (`Ctrl+Shift+X`).

Prérequis :
- Windows 10 ou ultérieur
- VS Code 1.109.0 ou ultérieur
- L'extension de débogueur pour le langage de votre app

Lisez l'[annonce complète de Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) pour plus de détails.

## Conclusion

L'extension WinApp pour VS Code est une bienvenue addition pour les développeurs de bureau Windows en .NET qui vivent dans VS Code mais ont dû passer à Visual Studio pour les tâches de packaging. Identité de paquet depuis F5, packaging MSIX depuis la palette de commandes, gestion des certificats intégrée — c'est le bon ensemble de fonctionnalités.

Essayez-la sur votre prochain projet WPF ou WinUI. La friction que vous contourniez vient de se réduire considérablement.
