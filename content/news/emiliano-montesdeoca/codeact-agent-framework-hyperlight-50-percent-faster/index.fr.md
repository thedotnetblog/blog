---
title: "CodeAct dans Agent Framework : Comment Réduire la Latence de votre Agent de Moitié"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct réduit les chaînes d'outils multi-étapes en un seul bloc de code sandboxé — réduisant la latence de 52% et l'utilisation des tokens de 64%. Ce que cela signifie pour vos agents et quand l'utiliser."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Il y a ce moment dans tout projet d'agents où vous regardez la trace et pensez : « pourquoi est-ce que ça prend autant de temps ? » Le modèle est bien. Les outils fonctionnent. Mais il y a sept allers-retours pour obtenir un résultat qu'on pourrait calculer en une seule fois.

C'est exactement le problème que CodeAct résout — et l'[équipe Agent Framework vient de publier un support alpha](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) via le nouveau paquet `agent-framework-hyperlight`.

## Qu'est-ce que CodeAct ?

Le [pattern CodeAct](https://arxiv.org/abs/2402.01030) est élégamment simple : au lieu de donner au modèle une liste d'outils à appeler un par un, vous lui donnez un seul outil `execute_code` et le laissez exprimer le *plan complet* comme un court programme Python. L'agent écrit le code une fois, le sandbox l'exécute, et vous récupérez un seul résultat consolidé.

| Câblage | Temps | Tokens |
|--------|------|--------|
| Traditionnel | 27,81s | 6 890 |
| CodeAct | 13,23s | 2 489 |
| **Amélioration** | **52,4%** | **63,9%** |

## Sécurité : Micro-VMs Hyperlight

Le paquet `agent-framework-hyperlight` utilise des micro-VMs [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Chaque appel `execute_code` obtient sa propre micro-VM fraîchement créée. Le démarrage se mesure en millisecondes. L'isolation est pratiquement gratuite.

Vos outils continuent de s'exécuter sur l'hôte. Le *code de collage* généré par le modèle s'exécute dans le sandbox. C'est le bon découpage.

## Configuration minimale

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## Quand utiliser CodeAct (et quand ne pas l'utiliser)

**Utilisez CodeAct quand :**
- La tâche enchaîne de nombreux petits appels d'outils (lookups, jointures, calculs)
- La latence et le coût en tokens comptent
- Vous voulez une isolation forte par appel pour le code généré par le modèle

**Restez avec le tool-calling traditionnel quand :**
- L'agent ne fait qu'un ou deux appels d'outils par tour
- Chaque appel a des effets secondaires à approuver individuellement
- Les descriptions d'outils sont peu détaillées

## Essayez maintenant

```bash
pip install agent-framework-hyperlight --pre
```

Consultez le [post complet sur le blog Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) pour une couverture approfondie.
