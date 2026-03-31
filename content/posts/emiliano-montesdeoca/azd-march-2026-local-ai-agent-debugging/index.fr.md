---
title: "azd permet maintenant d'exécuter et déboguer des agents IA localement — Ce qui a changé en mars 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI a publié sept versions en mars 2026. Les points forts : une boucle locale d'exécution et débogage pour les agents IA, l'intégration GitHub Copilot pour la configuration de projets, et le support des Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}}).*

Sept versions en un mois. C'est ce que l'équipe Azure Developer CLI (`azd`) a livré en mars 2026, et la fonctionnalité phare est celle que j'attendais : **une boucle locale d'exécution et débogage pour les agents IA**.

PC Chan [a publié le récapitulatif complet](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), et bien qu'il y ait beaucoup de contenu, laissez-moi filtrer ce qui compte vraiment pour les développeurs .NET qui construisent des apps alimentées par l'IA.

## Exécuter et déboguer des agents IA sans déployer

C'est le gros morceau. La nouvelle extension `azure.ai.agents` ajoute des commandes qui offrent une vraie boucle interne pour les agents IA :

- `azd ai agent run` — démarre votre agent localement
- `azd ai agent invoke` — lui envoie des messages (local ou déployé)
- `azd ai agent show` — affiche le statut du conteneur et sa santé
- `azd ai agent monitor` — diffuse les logs du conteneur en temps réel

Avant, tester un agent IA signifiait déployer sur Microsoft Foundry à chaque modification. Maintenant, vous pouvez itérer localement, tester le comportement de votre agent, et ne déployer que quand vous êtes prêt.

## GitHub Copilot configure votre projet azd

`azd init` offre maintenant une option "Set up with GitHub Copilot (Preview)". Au lieu de répondre manuellement aux prompts, un agent Copilot génère la configuration pour vous. Quand une commande échoue, `azd` propose un dépannage assisté par IA — tout sans quitter le terminal.

## Container App Jobs et améliorations de déploiement

- **Container App Jobs** : `azd` déploie maintenant `Microsoft.App/jobs` via la config existante `host: containerapp`.
- **Timeouts configurables** : Nouveau flag `--timeout` sur `azd deploy` et champ `deployTimeout` dans `azure.yaml`.
- **Fallback de build distant** : En cas d'échec du build ACR, `azd` retombe automatiquement sur Docker/Podman local.
- **Validation preflight locale** : Les paramètres Bicep sont validés localement avant le déploiement.

## Améliorations DX

- **Détection automatique pnpm/yarn** pour les projets JS/TS
- **Support pyproject.toml** pour le packaging Python
- **Répertoires de templates locaux** — `azd init --template` accepte les chemins du système de fichiers
- **Meilleurs messages d'erreur** en mode `--no-prompt`
- **Variables d'environnement de build** injectées dans tous les sous-processus de build (.NET, Node.js, Java, Python)

## Pour conclure

La boucle locale de débogage d'agents IA est la star de cette version, mais l'accumulation d'améliorations de déploiement et de polish DX rend `azd` plus mature que jamais. Si vous déployez des apps .NET sur Azure — surtout des agents IA — cette mise à jour vaut le détour.

Consultez les [notes de version complètes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) pour tous les détails.
