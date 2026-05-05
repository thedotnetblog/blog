---
title: "Foundry Toolboxes : Un seul endpoint pour tous les outils de vos agents"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry vient de lancer Toolboxes en preview publique — un moyen de centraliser, gérer et exposer les outils d'agents IA via un unique endpoint compatible MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Voici un problème qui semble banal jusqu'à ce qu'on le vive : l'organisation construit plusieurs agents IA, chacun nécessite des outils, et chaque équipe les reconfigure à partir de zéro. La même intégration de recherche web, la même config Azure AI Search, la même connexion au serveur MCP GitHub — mais dans un autre dépôt, par une autre équipe, avec d'autres credentials et sans gouvernance partagée.

Microsoft Foundry vient de lancer [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) en preview publique, et c'est une réponse directe à ce problème.

## Qu'est-ce qu'une Toolbox ?

Une Toolbox est un bundle d'outils nommé et réutilisable, défini une fois dans Foundry et exposé via un unique endpoint compatible MCP. N'importe quel runtime d'agent qui parle MCP peut le consommer — pas d'enfermement dans Foundry Agents.

La promesse est simple : **build once, consume anywhere**. Définir les outils, configurer l'authentification de façon centralisée (OAuth passthrough, identité managée Entra), publier l'endpoint. Chaque agent qui a besoin de ces outils se connecte à l'endpoint et les obtient tous.

## Les quatre piliers (deux disponibles aujourd'hui)

| Pilier | Statut | Ce qu'il fait |
|--------|--------|---------------|
| **Discover** | Bientôt | Trouver des outils approuvés sans recherche manuelle |
| **Build** | Disponible | Regrouper des outils en un bundle réutilisable |
| **Consume** | Disponible | Un endpoint MCP unique expose tous les outils |
| **Govern** | Bientôt | Auth centralisée + observabilité pour tous les appels |

## Exemple pratique

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Chercher dans la documentation et répondre aux issues GitHub.",
    tools=[
        {"type": "web_search", "description": "Recherche dans la documentation publique"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Une fois publié, Foundry fournit un endpoint unifié. Une connexion, tous les outils.

## Pas d'enfermement dans Foundry Agents

Les Toolboxes sont **créées et gérées** dans Foundry, mais la surface de consommation est le protocole MCP ouvert. On peut les utiliser depuis des agents personnalisés (Microsoft Agent Framework, LangGraph), GitHub Copilot et autres IDEs compatibles MCP, et tout runtime parlant MCP.

## Pourquoi c'est important maintenant

La vague multi-agents arrive en production. Chaque nouvel agent est une nouvelle surface pour de la configuration dupliquée, des credentials obsolètes et des comportements incohérents. La base Build + Consume suffit pour commencer à centraliser. Quand le pilier Govern arrivera, on aura une couche d'outils entièrement observable et contrôlée centralement pour toute la flotte d'agents.

## Conclusion

C'est encore tôt — preview publique, SDK Python en premier, Discover et Govern à venir. Mais le modèle est solide et le design natif MCP signifie qu'il fonctionne avec les outils qu'on construit déjà. Tous les détails dans l'[annonce officielle](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/).
