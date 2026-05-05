---
title: "azd update — Une seule commande pour tous vos gestionnaires de paquets"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI dispose désormais d'une commande de mise à jour universelle qui fonctionne quelle que soit la méthode d'installation — winget, Homebrew, Chocolatey ou script d'installation."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "azd-update-universal-upgrade-command.md" >}}).*

Vous connaissez ce message « Une nouvelle version de azd est disponible » qui apparaît toutes les quelques semaines ? Celui que vous ignorez parce que vous ne vous souvenez plus si vous avez installé `azd` via winget, Homebrew ou ce script curl que vous avez exécuté il y a six mois ? Eh bien, c'est enfin réglé.

Microsoft vient de publier [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — une seule commande qui met à jour Azure Developer CLI vers la dernière version, quelle que soit la méthode d'installation d'origine. Windows, macOS, Linux — peu importe. Une seule commande.

## Comment ça marche

```bash
azd update
```

C'est tout. Si vous voulez un accès anticipé aux nouvelles fonctionnalités, vous pouvez passer au build insiders quotidien :

```bash
azd update --channel daily
azd update --channel stable
```

La commande détecte votre méthode d'installation actuelle et utilise le mécanisme de mise à jour approprié en arrière-plan. Fini le « attends, j'ai utilisé winget ou choco sur cette machine ? »

## Le petit bémol

`azd update` est disponible à partir de la version 1.23.x. Si vous êtes sur une version antérieure, vous devrez effectuer une dernière mise à jour manuelle en utilisant votre méthode d'installation d'origine. Après ça, `azd update` gère tout automatiquement.

Vérifiez votre version actuelle avec `azd version`. Si vous avez besoin d'une nouvelle installation, la [documentation d'installation](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) est là pour vous.

## Pourquoi c'est important

C'est une petite amélioration de confort, mais pour ceux d'entre nous qui utilisent `azd` quotidiennement pour déployer des agents IA et des apps Aspire sur Azure, être à jour signifie moins de moments « ce bug était déjà corrigé dans la dernière version ». Une chose de moins à laquelle penser.

Lisez l'[annonce complète](https://devblogs.microsoft.com/azure-sdk/azd-update/) et l'[analyse approfondie](https://blog.jongallant.com/2026/04/azd-update) de Jon Gallant pour plus de contexte.
