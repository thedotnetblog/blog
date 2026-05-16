---
title: "Mises à jour d'Azure Developer CLI (azd) pour avril 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd a publié cinq versions en avril 2026, avec en tête le support des hooks multi-langages pour Python, JavaScript, TypeScript et .NET, ainsi que la préversion publique d'azd update, les vérifications préalables de quota IA et plus encore."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) a publié cinq versions en avril 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (de 1.23.14 à 1.24.2), avec pour grand thème les hooks qui s'exécutent désormais en Python, JavaScript, TypeScript et .NET — et pas seulement en Bash et PowerShell.

## Hooks multi-langages dans azure.yaml

Les hooks peuvent désormais pointer vers des fichiers `.py`, `.js`, `.ts` ou `.cs` en plus des scripts shell. Chaque langage bénéficie d'une résolution automatique des dépendances :

- **Python** — détecte `requirements.txt` ou `pyproject.toml`, crée un virtualenv et installe les dépendances avant l'exécution. Configurez le nom de l'environnement avec `virtualEnvName`.
- **JavaScript / TypeScript** — détecte `package.json` et exécute `npm install` automatiquement. TypeScript s'exécute via `npx tsx` sans étape de compilation. Choisissez votre gestionnaire de paquets avec le bloc de configuration `packageManager`.
- **.NET** — exécute les fichiers `.cs` avec `dotnet run`. Les scripts single-file sont pris en charge sur .NET 10+. Configurez le framework cible via le bloc `configuration/framework`.

Cela signifie que les équipes travaillant déjà dans l'un de ces langages n'ont plus besoin de maintenir un hook Bash ou PowerShell séparé juste pour connecter les événements du cycle de vie du provisionnement.

## azd update passe en préversion publique

`azd update` est désormais en préversion publique sur toutes les plateformes. Une seule commande gère la mise à jour quelle que soit la façon dont azd a été installé initialement — plus besoin de gérer séparément les chemins Homebrew, WinGet ou MSI.

## Mode non interactif via AZD_NON_INTERACTIVE

La définition de `AZD_NON_INTERACTIVE=true` (ou l'utilisation de `--non-interactive` / `--no-prompt`) produit désormais des échecs cohérents et déterministes dans les pipelines CI/CD lorsqu'une entrée requise ne peut pas être résolue automatiquement. Auparavant, le comportement était incohérent selon les commandes.

## Vérification préalable du quota des modèles IA

`azd provision` valide le quota Azure Cognitive Services avant de tenter de provisionner des ressources de modèles IA. Les déploiements qui échoueraient en raison de limites de quota affichent désormais l'erreur tôt dans le processus plutôt qu'à mi-chemin du provisionnement.

## « Corriger cette erreur » dans le dépannage Copilot

L'intégration de dépannage Copilot dans azd gagne la capacité d'appliquer directement un correctif suggéré — pas seulement de le décrire. Lorsque l'agent identifie un problème corrigeable, il peut effectuer le changement sur place.

## Fournisseurs de provisionnement personnalisés et résolveur de secrets Key Vault

Les auteurs d'extensions peuvent désormais enregistrer des backends d'infrastructure alternatifs avec `WithProvisioningProvider()`. Par ailleurs, azd résout automatiquement les références `@Microsoft.KeyVault(...)` avant de transmettre la configuration aux extensions, supprimant la nécessité d'une résolution manuelle des secrets dans les fournisseurs personnalisés.

## Exclusions pour les modèles et le mode watch

Deux nouveaux fichiers d'exclusion offrent un contrôle plus fin sur la gestion des fichiers :
- **`.azdignore`** — exclut les fichiers réservés aux contributeurs (documentation, configurations CI) des copies de modèles pour que les utilisateurs finaux obtiennent un projet propre.
- **`.azdxignore`** — exclut les répertoires du déclenchement de reconstructions pendant `azd x watch`, réduisant le bruit lors du développement itératif.

## Vérification préalable des noms réservés et option docker.network

azd avertit désormais lorsque les noms de ressources prévus contiendraient des mots réservés Azure (`MICROSOFT`, `WINDOWS` ou le préfixe `LOGIN`) avant le début du provisionnement. Une nouvelle option `docker.network` passe `--network` à `docker build`, utile dans les environnements de proxy d'entreprise qui nécessitent un réseau Docker spécifique.

## Correctifs de sécurité

Le paquet MSI Windows inclut désormais la vérification de signature de code. Un correctif distinct ferme une fuite de variable d'environnement qui pouvait exposer des valeurs entre les limites des commandes d'extension.

---

Un mois chargé — le support des hooks multi-langages en particulier supprime un vrai point de friction pour les équipes qui ne travaillent pas principalement en Bash. Consultez les [notes de version complètes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) pour le changelog complet des cinq versions.
