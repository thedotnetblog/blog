---
title: "Aspire 13.2 embarque une CLI de documentation — et votre agent IA peut l'utiliser aussi"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 ajoute aspire docs — une CLI pour rechercher, parcourir et lire la documentation officielle sans quitter votre terminal. Elle fonctionne aussi comme outil pour les agents IA. Voici pourquoi c'est important."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "aspire-docs-cli-ai-skills.md" >}}).*

Vous connaissez ce moment où vous êtes plongé dans un Aspire AppHost, en train de câbler des intégrations, et vous devez vérifier exactement quels paramètres l'intégration Redis attend ? Vous faites alt-tab vers votre navigateur, vous cherchez sur aspire.dev, vous plissez les yeux sur les docs de l'API, puis vous revenez à votre éditeur. Contexte perdu. Flow brisé.

Aspire 13.2 vient de [livrer une solution à ça](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). La CLI `aspire docs` vous permet de rechercher, parcourir et lire la documentation officielle d'Aspire directement depuis votre terminal. Et comme elle s'appuie sur des services réutilisables, les agents IA et les skills peuvent utiliser les mêmes commandes pour consulter la doc au lieu d'halluciner des APIs qui n'existent pas.

## Le problème que ça résout vraiment

David Pine le dit parfaitement dans le post original : les agents IA étaient *catastrophiques* pour aider les développeurs à construire des apps Aspire. Ils recommandaient `dotnet run` au lieu de `aspire run`, référençaient learn.microsoft.com pour des docs qui se trouvent sur aspire.dev, suggéraient des packages NuGet obsolètes, et — mon préféré — hallucinaient des APIs inexistantes.

Pourquoi ? Parce qu'Aspire a été spécifique à .NET bien plus longtemps qu'il n'est polyglotte, et les LLMs travaillent avec des données d'entraînement qui précèdent les dernières fonctionnalités. Quand vous donnez à un agent IA la capacité de consulter les docs actuels, il arrête de deviner et commence à être utile.

## Trois commandes, zéro onglet de navigateur

La CLI est d'une simplicité rafraîchissante :

### Lister toute la documentation

```bash
aspire docs list
```

Retourne chaque page de documentation disponible sur aspire.dev. Besoin d'une sortie lisible par une machine ? Ajoutez `--format Json`.

### Rechercher un sujet

```bash
aspire docs search "redis"
```

Recherche à la fois dans les titres et le contenu avec un score de pertinence pondéré. Le même moteur de recherche qui alimente les outils de documentation en interne. Vous obtenez des résultats classés avec titres, slugs et scores de pertinence.

### Lire une page complète (ou juste une section)

```bash
aspire docs get redis-integration
```

Envoie la page complète en markdown dans votre terminal. Besoin d'une seule section ?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

Précision chirurgicale. Pas besoin de scroller 500 lignes. Juste la partie dont vous avez besoin.

## L'angle agent IA

C'est là que ça devient intéressant pour nous, développeurs qui construisons avec des outils IA. Les mêmes commandes `aspire docs` fonctionnent comme outils pour les agents IA — via des skills, des serveurs MCP, ou de simples wrappers CLI.

Au lieu que votre assistant IA invente des APIs Aspire basées sur des données d'entraînement obsolètes, il peut appeler `aspire docs search "postgres"`, trouver les docs d'intégration officiels, lire la bonne page, et vous donner l'approche documentée. De la documentation en temps réel et à jour — pas ce que le modèle a mémorisé il y a six mois.

L'architecture derrière tout ça est intentionnelle. L'équipe Aspire a construit des services réutilisables (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) plutôt qu'une intégration ponctuelle. Cela signifie que le même moteur de recherche fonctionne pour les humains dans le terminal, les agents IA dans votre éditeur, et l'automatisation dans votre pipeline CI.

## Scénarios concrets

**Consultations rapides dans le terminal :** Vous êtes trois fichiers en profondeur et vous avez besoin des paramètres de configuration Redis. Deux commandes, quatre-vingt-dix secondes, retour au travail :

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**Développement assisté par IA :** Votre skill VS Code encapsule les commandes CLI. Vous demandez « Ajoute une base de données PostgreSQL à mon AppHost » et l'agent consulte les vrais docs avant de répondre. Pas d'hallucinations.

**Validation CI/CD :** Votre pipeline valide les configurations AppHost contre la documentation officielle de manière programmatique. La sortie `--format Json` se connecte proprement à `jq` et d'autres outils.

**Bases de connaissances personnalisées :** Vous construisez vos propres outils IA ? Envoyez la sortie JSON structurée directement dans votre base de connaissances :

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

Pas de web scraping. Pas de clés API. Les mêmes données structurées utilisées en interne par les outils de documentation.

## La documentation est toujours à jour

C'est la partie que j'apprécie le plus. La CLI ne télécharge pas un snapshot — elle interroge aspire.dev avec un cache basé sur les ETags. Dès que la documentation est mise à jour, votre CLI et tout skill construit dessus le reflète. Pas de copies obsolètes, pas de moments « mais le wiki disait... ».

## Pour conclure

`aspire docs` est une de ces petites fonctionnalités qui résout un vrai problème proprement. Les humains obtiennent un accès à la documentation natif au terminal. Les agents IA obtiennent un moyen d'arrêter de deviner et de commencer à référencer de vrais docs. Et tout est soutenu par la même source de vérité.

Si vous construisez avec .NET Aspire et n'avez pas encore essayé la CLI, lancez `aspire docs search "votre-sujet-ici"` et voyez comment ça se passe. Ensuite, envisagez d'intégrer ces commandes dans votre skill IA ou votre configuration d'automatisation — vos agents vous remercieront.

Consultez [l'analyse approfondie de David Pine](https://davidpine.dev/posts/aspire-docs-mcp-tools/) sur la construction des outils de documentation, et la [référence officielle de la CLI](https://aspire.dev/reference/cli/commands/aspire-docs/) pour tous les détails.
