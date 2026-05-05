---
title: "Microsoft Agent Framework Hits 1.0: això és el que realment importa per als desenvolupadors de.NET"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0 està preparat per a la producció amb API estables, orquestració multiagent i connectors per a tots els principals proveïdors d'IA. Això és el que necessiteu saber com a desenvolupador.NET."
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

Si heu estat seguint el viatge de l'Agent Framework des dels primers dies del nucli semàntic i de l'AutoGen, aquest és significatiu. Microsoft Agent Framework només [accedir a la versió 1.0](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/): API estables, preparades per a la producció, compromís de suport a llarg termini. Està disponible tant per a.NET com per a Python, i està realment preparat per a càrregues de treball reals.

Permeteu-me reduir el soroll de l'anunci i centrar-me en allò que importa si esteu creant aplicacions basades en IA amb.NET.

## La versió curta

Agent Framework 1.0 unifica el que abans era Semantic Kernel i AutoGen en un únic SDK de codi obert. Abstracció d'un agent. Un motor d'orquestració. Diversos proveïdors d'IA. Si heu estat rebotant entre el nucli semàntic per a patrons empresarials i AutoGen per a fluxos de treball multiagent de grau de recerca, podeu aturar-vos. Aquest és l'SDK ara.

## Començar és gairebé injustament senzill

Aquí hi ha un agent que treballa a.NET:

```csharp
// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry;
using Azure.Identity;

var agent = new AIProjectClient(endpoint: "https://your-project.services.ai.azure.com")
    .GetResponsesClient("gpt-5.3")
    .AsAIAgent(
        name: "HaikuBot",
        instructions: "You are an upbeat assistant that writes beautifully."
    );

Console.WriteLine(await agent.RunAsync("Write a haiku about shipping 1.0."));
```

Això és tot. Un grapat de línies i teniu un agent d'IA que s'executa contra Azure Foundry. L'equivalent de Python és igualment concís. Afegiu eines de funció, converses de diversos torns i transmissió a mesura que avanceu: la superfície de l'API augmenta sense ser estrany.

## Orquestració multiagent: aquest és el veritable negoci

Els agents únics estan bé per a les demostracions, però els escenaris de producció solen necessitar coordinació. Agent Framework 1.0 s'envia amb patrons d'orquestració provats en batalla directament de Microsoft Research i AutoGen:

- **Seqüencial**: els agents processen per ordre (escriptor → revisor → editor)
- **Simultània**: es distribueix a diversos agents en paral·lel, convergeix els resultats
- **Handoff**: un agent delega a un altre segons la intenció
- **Xat de grup**: diversos agents discuteixen i convergeixen en una solució
- **Magentic-One**: el patró multiagent de grau de recerca de MSR

Tots admeten la transmissió en temps real, els punts de control, les aprovacions humanes en el bucle i la pausa/reprèn. La part del punt de control és crucial: els fluxos de treball de llarga durada sobreviuen als reinicis del procés. Per als desenvolupadors de.NET que hem creat fluxos de treball duradors amb Azure Functions, això ens sembla familiar.

## Les característiques que més importen

Aquí teniu la meva llista del que val la pena saber:

**Enganxs de middleware.** Saps com ASP.NET Core té canalitzacions de middleware? Mateix concepte, però per a l'execució de l'agent. Intercepteu totes les etapes (afegiu seguretat de contingut, registre, polítiques de compliment) sense tocar les indicacions de l'agent. Així és com podeu preparar els agents per a l'empresa.

**Memòria connectable.** Historial de conversa, estat clau-valor persistent, recuperació basada en vectors. Trieu el vostre backend: Foundry Agent Service, Mem0, Redis, Neo4j o enrotlleu el vostre. La memòria és el que converteix una trucada LLM sense estat en un agent que realment recorda el context.

**Agents YAML declaratius.** Definiu les instruccions, les eines, la memòria i la topologia d'orquestració del vostre agent en fitxers YAML controlats per versions. Carregueu i executeu amb una única trucada a l'API. Això és un canvi de joc per als equips que volen repetir el comportament de l'agent sense tornar a desplegar el codi.

**Compatibilitat amb A2A i MCP.** MCP (Model Context Protocol) permet als agents descobrir i invocar eines externes de manera dinàmica. A2A (protocol d'agent a agent) permet la col·laboració entre temps d'execució: els vostres agents.NET poden coordinar-se amb els agents que s'executen en altres marcs. El suport A2A 1.0 arribarà aviat.

## Les funcions de previsualització val la pena veure-les

Algunes funcions s'envien com a previsualització a la versió 1.0: funcionals, però les API poden evolucionar:

- **DevUI**: un depurador local basat en navegador per visualitzar l'execució de l'agent, els fluxos de missatges i les trucades d'eines en temps real. Penseu en Application Insights, però per al raonament dels agents.
- **GitHub Copilot SDK i Claude Code SDK**: utilitzeu Copilot o Claude com a arnès d'agent directament des del vostre codi d'orquestració. Escriu un agent capaç de codificar juntament amb els altres agents en el mateix flux de treball.
- **Agent Harness**: un temps d'execució local personalitzable que ofereix als agents accés a l'intèrpret d'ordres, al sistema de fitxers i als bucles de missatgeria. Penseu en agents de codificació i patrons d'automatització.
- **Habilitats**: paquets de capacitats de domini reutilitzables que ofereixen als agents capacitats estructurades de manera immediata.

## Migració des del nucli semàntic o AutoGen

Si teniu codi Semàntic Kernel o AutoGen, hi ha assistents de migració dedicats que analitzen el vostre codi i generen plans de migració pas a pas. La [guia de migració del nucli semàntic](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel) i la [guia de migració d'AutoGen](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen) us acompanyen tot.

Si heu estat als paquets RC, l'actualització a la 1.0 és només un augment de la versió.

## Tancant

Agent Framework 1.0 és la fita de producció que els equips empresarials estaven esperant. API estables, suport per a diversos proveïdors, patrons d'orquestració que funcionen realment a escala i rutes de migració tant del nucli semàntic com d'AutoGen.

El marc és [totalment de codi obert a GitHub](https://github.com/microsoft/agent-framework), i podeu començar avui mateix amb `dotnet add package Microsoft.Agents.AI`. Consulteu la [guia d'inici ràpid](https://learn.microsoft.com/en-us/agent-framework/get-started/) i les [mostres](https://github.com/microsoft/agent-framework) per embrutar-vos les mans.

Si heu estat esperant el senyal "Segur per utilitzar en producció", això és tot.
