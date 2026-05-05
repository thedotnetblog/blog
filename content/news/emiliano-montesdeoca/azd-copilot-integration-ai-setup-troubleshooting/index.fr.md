---
title: "azd + GitHub Copilot : Configuration de projet assistée par IA et résolution intelligente des erreurs"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI s'intègre maintenant avec GitHub Copilot pour scaffolder ton projet et résoudre les erreurs de déploiement — sans quitter le terminal."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Cet article a été traduit automatiquement. Pour la version originale en anglais, [clique ici]({{< ref "index.md" >}}).*

Tu connais ce moment où tu veux déployer une app existante sur Azure et tu te retrouves à fixer un `azure.yaml` vide, en essayant de te rappeler si ton API Express devrait utiliser Container Apps ou App Service ? Ce moment vient de devenir beaucoup plus court.

L'Azure Developer CLI (`azd`) s'intègre maintenant avec GitHub Copilot de deux façons concrètes : scaffolding assisté par IA pendant `azd init`, et résolution intelligente des erreurs quand les déploiements échouent. Les deux fonctionnalités restent entièrement dans ton terminal — exactement là où je veux qu'elles soient.

## Configuration avec Copilot pendant azd init

Quand tu lances `azd init`, il y a maintenant une option "Set up with GitHub Copilot (Preview)". Sélectionne-la et Copilot analyse ta base de code pour générer l'`azure.yaml`, les templates d'infrastructure et les modules Bicep — basés sur ton code réel.

```
azd init
# Sélectionne : "Set up with GitHub Copilot (Preview)"
```

Prérequis :

- **azd 1.23.11 ou supérieur** — vérifie avec `azd version` ou mets à jour avec `azd update`
- **Un abonnement GitHub Copilot actif** (Individual, Business ou Enterprise)
- **GitHub CLI (`gh`)** — `azd` demandera la connexion si nécessaire

Ce que je trouve vraiment utile : ça fonctionne dans les deux sens. Tu construis depuis zéro ? Copilot t'aide à configurer les bons services Azure dès le départ. Tu as une app existante que tu voulais déployer depuis longtemps ? Pointe Copilot dessus et il génère la configuration sans que tu aies à restructurer quoi que ce soit.

### Ce que ça fait concrètement

Imaginons une API Express Node.js avec une dépendance PostgreSQL. Au lieu de décider manuellement entre Container Apps et App Service, puis d'écrire du Bicep depuis zéro, Copilot détecte ton stack et génère :

- Un `azure.yaml` avec les bons paramètres `language`, `host` et `build`
- Un module Bicep pour Azure Container Apps
- Un module Bicep pour Azure Database for PostgreSQL

Et il effectue des vérifications préalables avant de toucher quoi que ce soit — vérifie que ton répertoire git est propre, demande le consentement pour les outils du serveur MCP. Rien ne se passe sans que tu saches exactement ce qui va changer.

## Résolution d'erreurs avec Copilot

Les erreurs de déploiement, ça arrive. Paramètres manquants, problèmes de permissions, disponibilité des SKUs — et le message d'erreur ne te dit rarement la seule chose dont tu as vraiment besoin : *comment régler le problème*.

Sans Copilot, la boucle ressemble à : copier l'erreur → chercher dans la doc → lire trois réponses Stack Overflow hors sujet → exécuter quelques commandes `az` CLI → réessayer en espérant que ça marche. Avec Copilot intégré dans `azd`, cette boucle s'effondre. Quand une commande `azd` échoue, elle propose immédiatement quatre options :

- **Explain** — explication en langage naturel de ce qui s'est passé
- **Guidance** — instructions étape par étape pour corriger le problème
- **Diagnose and Guide** — analyse complète + Copilot applique le correctif (avec ton approbation) + nouvelle tentative optionnelle
- **Skip** — gérer toi-même

L'essentiel : Copilot a déjà le contexte de ton projet, la commande qui a échoué et les détails de l'erreur. Ses suggestions sont spécifiques à *ta situation*, pas de la documentation générique.

### Configurer un comportement par défaut

Si tu choisis toujours la même option, saute le prompt interactif :

```
azd config set copilot.errorHandling.category troubleshoot
```

Valeurs : `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Tu peux aussi activer l'auto-fix et le retry :

```
azd config set copilot.errorHandling.fix allow
```

Retour au mode interactif à tout moment :

```
azd config unset copilot.errorHandling.category
```

## Conclusion

C'est exactement le type d'intégration Copilot qui apporte une vraie valeur. Essaie-le en lançant `azd update` pour obtenir la dernière version, puis utilise `azd init` sur ton prochain projet.

Lis l'[annonce originale ici](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
