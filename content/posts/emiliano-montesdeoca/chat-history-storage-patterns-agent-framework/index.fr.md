---
title: "Où votre Agent se Souvient-il des Choses ? Guide Pratique sur le Stockage de l'Historique de Chat"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Géré par le service ou par le client ? Linéaire ou bifurquant ? La décision architecturale qui détermine ce que votre agent IA peut vraiment faire — avec des exemples de code en C# et Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Lors de la création d'un agent IA, vous consacrez la majeure partie de votre énergie au modèle, aux outils et aux prompts. La question de *l'endroit où vit l'historique des conversations* semble être un détail d'implémentation — mais c'est l'une des décisions architecturales les plus importantes que vous prendrez.

Elle détermine si les utilisateurs peuvent bifurquer des conversations, annuler des réponses, reprendre des sessions après un redémarrage, et si vos données quittent jamais votre infrastructure. L'[équipe Agent Framework a publié une analyse approfondie](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Deux modèles fondamentaux

**Géré par le service** : le service IA stocke l'état de la conversation. Votre application tient une référence et le service inclut automatiquement l'historique pertinent dans chaque requête.

**Géré par le client** : votre application maintient l'historique complet et envoie les messages pertinents avec chaque requête. Le service est sans état. Vous contrôlez tout.

## Comment Agent Framework abstrait cela

```csharp
// C# — fonctionne pareil quel que soit le fournisseur
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Je m'appelle Alice.", session);
var second = await agent.RunAsync("Quel est mon nom ?", session);
```

```python
# Python
session = agent.create_session()
first = await agent.run("Je m'appelle Alice.", session=session)
second = await agent.run("Quel est mon nom ?", session=session)
```

## Référence rapide des fournisseurs

| Fournisseur | Stockage | Modèle | Compaction |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Client | N/A | Vous |
| Foundry Agent Service | Service | Linéaire | Service |
| Responses API (défaut) | Service | Bifurquant | Service |
| Anthropic Claude, Ollama | Client | N/A | Vous |

## Comment choisir

1. **Besoin de bifurcation ou « annuler » ?** → Responses API géré par service
2. **Besoin de souveraineté des données ?** → Géré par client avec fournisseur base de données
3. **Simple chatbot ?** → Géré par service linéaire suffit

Lisez le [post complet](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) pour l'arbre de décision complet.
