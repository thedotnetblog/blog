---
title: "LangChain + Azure Cosmos DB pour les applications agentiques et RAG"
date: 2026-05-12
author: "Emiliano Montesdeoca"
description: "langchain-azure-cosmosdb est un nouveau package Python qui consolide la recherche vectorielle, l'historique de chat, le checkpointing d'état d'agent, le cache sémantique et la mémoire à long terme dans un seul backend Azure Cosmos DB for NoSQL."
tags:
  - .NET
  - Azure Cosmos DB
  - LangChain
  - RAG
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[`langchain-azure-cosmosdb`](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/) (`pip install langchain-azure-cosmosdb`) est un nouveau package Python qui connecte LangChain et LangGraph à Azure Cosmos DB for NoSQL, remplaçant les 5+ services séparés habituels pour le stockage vectoriel, le cache, l'historique et la mémoire par une seule base de données.

## Six intégrations dans un seul package

Le package comprend six classes d'intégration (chacune avec des variantes synchrones et asynchrones) :

1. **AzureCosmosDBNoSqlVectorSearch** — recherche vectorielle, plein texte (BM25), hybride (vecteur+texte avec RRF) et hybride pondérée
2. **AzureCosmosDBNoSqlSemanticCache** — mise en cache des réponses LLM pour réduire la latence et le coût sur les requêtes répétées
3. **CosmosDBChatMessageHistory** — persistance de l'historique de conversation avec support TTL
4. **CosmosDBSaverSync / CosmosDBSaver** — checkpointer LangGraph : persiste l'état du graphe par thread_id entre les invocations
5. **CosmosDBCacheSync / CosmosDBCache** — mise en cache des résultats au niveau des nœuds LangGraph
6. **CosmosDBStore / AsyncCosmosDBStore** — mémoire à long terme avec organisation par espace de noms et recherche sémantique

L'authentification par clé d'accès et par Identité Managée (Entra ID) est prise en charge pour toutes les intégrations.

## Recherche vectorielle et hybride

Azure Cosmos DB for NoSQL prend en charge les index vectoriels DiskANN et Quantized Flat, passant de milliers à des milliards de vecteurs — la même base de données qui alimente les historiques de conversation et les mémoires de ChatGPT chez OpenAI. Configuration de la recherche hybride :

```python
vectorstore = AzureCosmosDBNoSqlVectorSearch(
    cosmos_client=...,
    embedding=AzureOpenAIEmbeddings(...),
    ...
)
results = vectorstore.similarity_search(
    "distributed database",
    k=5,
    search_type="hybrid",
    full_text_rank_filter=[{"search_field": "text", "search_text": "distributed"}]
)
```

## Agents multi-tours LangGraph avec checkpointing Cosmos

Le checkpointer `CosmosDBSaverSync` persiste l'état du graphe LangGraph pour que les agents mémorisent le contexte entre des invocations séparées — aucun état en mémoire requis :

```python
checkpointer = CosmosDBSaverSync(
    database_name="agents-db",
    container_name="checkpoints",
    endpoint="..."
)
app = graph.compile(checkpointer=checkpointer)

# Tour 1
app.invoke(
    {"messages": [("user", "Hi, I'm Alice!")]},
    config={"configurable": {"thread_id": "user-123"}}
)

# Tour 2 — état persisté depuis le tour 1
app.invoke(
    {"messages": [("user", "What's my name?")]},
    config={"configurable": {"thread_id": "user-123"}}
)
# Retourne : "Your name is Alice!"
```

## Une base de données au lieu de cinq

Tout consolider dans Cosmos DB for NoSQL signifie une connexion, un ensemble d'identifiants, un bouton de mise à l'échelle et un seul endroit où chercher quand quelque chose va mal. Le package est disponible sur PyPI et le code source se trouve sur [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure) sur GitHub.

Tous les détails sur [devblogs.microsoft.com](https://devblogs.microsoft.com/cosmosdb/langchain-azure-cosmos-db-agents-rag/).
