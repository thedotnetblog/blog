---
title: "Construire des UIs Multi-Agents en Temps Réel Qui Ne Ressemblent Pas à une Boîte Noire"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI et Microsoft Agent Framework s'associent pour offrir aux workflows multi-agents un vrai frontend — avec du streaming en temps réel, des approbations humaines et une visibilité totale sur ce que font vos agents."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Voilà le truc avec les systèmes multi-agents : ils sont incroyables en démo. Trois agents qui se passent le travail, résolvent des problèmes, prennent des décisions. Puis tu essaies de le mettre devant de vrais utilisateurs et... silence. Un indicateur qui tourne. Aucune idée de quel agent fait quoi ni pourquoi le système est en pause. Ce n'est pas un produit — c'est un problème de confiance.

L'équipe Microsoft Agent Framework vient de publier un [excellent tutoriel](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) sur le couplage des workflows MAF avec [AG-UI](https://github.com/ag-ui-protocol/ag-ui), un protocole ouvert pour streamer les événements d'exécution des agents vers un frontend via les Server-Sent Events. Et franchement ? C'est exactement le pont qui nous manquait.

## Pourquoi c'est important pour les développeurs .NET

Si tu construis des applications alimentées par l'IA, tu as probablement déjà heurté ce mur. Ton orchestration backend fonctionne parfaitement — les agents se passent le relais, les outils se déclenchent, les décisions sont prises. Mais le frontend n'a aucune idée de ce qui se passe en coulisses. AG-UI résout ça en définissant un protocole standard pour streamer les événements d'agents (pense à `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) directement vers ta couche UI via SSE.

La démo est un workflow de support client avec trois agents : un agent de triage qui route les demandes, un agent de remboursement qui gère les questions d'argent, et un agent de commandes qui gère les remplacements. Chaque agent a ses propres outils, et la topologie de handoff est définie explicitement — pas de « devine à partir du prompt ».

## La topologie de handoff est la vraie star

Ce qui m'a marqué, c'est comment `HandoffBuilder` te permet de déclarer un graphe de routage dirigé entre les agents :

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Chaque `add_handoff` crée une arête dirigée avec une description en langage naturel. Le framework génère des outils de handoff pour chaque agent en se basant sur cette topologie. Les décisions de routage reposent donc sur ta structure d'orchestration, pas juste sur ce que le LLM a envie de faire. C'est un gain énorme pour la fiabilité en production.

## Le human-in-the-loop qui fonctionne vraiment

La démo présente deux patterns d'interruption dont toute app d'agents réelle a besoin :

**Interruptions d'approbation d'outils** — quand un agent appelle un outil marqué avec `approval_mode="always_require"`, le workflow se met en pause et émet un événement. Le frontend affiche un modal d'approbation avec le nom de l'outil et ses arguments. Pas de boucles de retry qui brûlent des tokens — juste un flux propre pause-approbation-reprise.

**Interruptions de demande d'information** — quand un agent a besoin de plus de contexte de la part de l'utilisateur (comme un ID de commande), il se met en pause et pose la question. Le frontend affiche la question, l'utilisateur répond, et l'exécution reprend exactement là où elle s'était arrêtée.

Les deux patterns sont streamés en tant qu'événements AG-UI standard, donc ton frontend n'a pas besoin de logique personnalisée par agent — il affiche simplement chaque événement qui arrive via la connexion SSE.

## L'intégration est étonnamment simple

L'intégration entre MAF et AG-UI se résume à un seul appel de fonction :

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

La `workflow_factory` crée un workflow frais par thread, pour que chaque conversation ait son propre état isolé. L'endpoint gère toute la plomberie SSE automatiquement. Si tu utilises déjà FastAPI (ou que tu peux l'ajouter comme couche légère), c'est quasiment zéro friction.

## Mon avis

Pour nous développeurs .NET, la question immédiate est : « Est-ce que je peux faire ça en C# ? » L'Agent Framework est disponible pour .NET et Python, et le protocole AG-UI est agnostique au langage (c'est juste du SSE). Donc même si cette démo spécifique utilise Python et FastAPI, le pattern se transpose directement. Tu pourrais câbler une API minimale ASP.NET Core avec des endpoints SSE suivant le même schéma d'événements AG-UI.

Le point plus important est que les UIs multi-agents deviennent une préoccupation de premier plan, pas un ajout après coup. Si tu construis quoi que ce soit où des agents interagissent avec des humains — support client, workflows d'approbation, traitement de documents — cette combinaison d'orchestration MAF et de transparence AG-UI est le pattern à suivre.

## Pour conclure

AG-UI + Microsoft Agent Framework te donne le meilleur des deux mondes : une orchestration multi-agents robuste côté backend et une visibilité en temps réel côté frontend. Fini les interactions d'agents en boîte noire.

Consulte le [tutoriel complet](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) et le [dépôt du protocole AG-UI](https://github.com/ag-ui-protocol/ag-ui) pour aller plus loin.
