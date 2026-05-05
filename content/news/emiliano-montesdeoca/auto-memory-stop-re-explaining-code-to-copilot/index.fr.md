---
title: "68 Minutes par Jour à Ré-Expliquer Son Code ? Il Y a une Solution"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Le context rot est réel — votre agent IA dérive après 30 tours, et vous payez la taxe de compactage toutes les heures. auto-memory donne à GitHub Copilot CLI un rappel chirurgical sans brûler des milliers de tokens."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici](https://thedotnetblog.com/posts/emiliano-montesdeoca/auto-memory-stop-re-explaining-code-to-copilot/).*

Vous connaissez ce moment où votre session Copilot atteint `/compact` et que l'agent oublie complètement ce sur quoi vous travailliez ? Vous passez les cinq minutes suivantes à ré-expliquer la structure des fichiers, le test qui échoue, les trois approches déjà essayées. Puis ça recommence.

Desi Villanueva l'a chronométré : **68 minutes par jour** — juste pour la réorientation. Pas à écrire du code. Pas à revoir des PRs. Juste à remettre l'IA au courant de choses qu'elle savait déjà.

Il s'avère qu'il y a une raison concrète à cela — et une solution concrète.

## Le Mensonge de la Fenêtre de Contexte

Votre agent arrive avec un grand nombre sur la boîte. 200K tokens. Ça semble massif. En pratique c'est un plafond, pas une garantie.

Voici le calcul réel :

- 200K contexte total
- Moins ~65K pour les outils MCP chargés au démarrage (~33%)
- Moins ~10K pour les fichiers d'instructions comme `AGENTS.md`

Cela vous laisse environ **125K avant d'avoir tapé un seul mot**. Et ça empire — les LLMs ne se dégradent pas gracieusement. Ils atteignent un mur vers 60% d'utilisation. Le modèle commence à perdre des éléments mentionnés 30 tours plus tôt.

Limite effective : **45K tokens** avant que la qualité se dégrade.

## La Taxe de Compactage

Chaque `/compact` vous coûte votre état de flow. Vous êtes profondément dans une session de débogage. Contexte partagé construit sur 30 minutes. Puis l'avertissement arrive.

La partie cruelle : **La mémoire existe déjà.** Copilot CLI écrit chaque session dans une base de données SQLite locale à `~/.copilot/session-store.db`. L'agent ne peut tout simplement pas la lire.

## auto-memory : Une Couche de Rappel, Pas un Système de Mémoire

```bash
pip install auto-memory
```

~1 900 lignes de Python. Zéro dépendances. Installé en 30 secondes.

Au lieu d'inonder le contexte avec des résultats grep, vous donnez à l'agent un accès chirurgical à ce qui compte vraiment — **50 tokens au lieu de 10 000**.

## En Conclusion

Le context rot est une contrainte architecturale réelle. auto-memory le contourne en donnant à votre agent un mécanisme de rappel bon marché et précis.

Consultez-le : [auto-memory sur GitHub](https://github.com/dezgit2025/auto-memory). Post original de Desi Villanueva : [I Wasted 68 Minutes a Day](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).
