---
title: "Foundry Agent Service ist GA: Was für .NET-Agent-Entwickler wirklich zählt"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsofts Foundry Agent Service ist jetzt GA — mit Private Networking, Voice Live, Produktions-Evaluierungen und einer offenen Multi-Model-Runtime. Hier ist, was du wissen musst."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Seien wir ehrlich — einen KI-Agenten-Prototyp zu bauen ist der einfache Teil. Der schwierige Teil ist alles danach: ihn in Produktion zu bringen mit ordentlicher Netzwerk-Isolation, Evaluierungen durchzuführen die wirklich etwas bedeuten, Compliance-Anforderungen zu erfüllen und um 2 Uhr morgens nichts kaputt zu machen.

Der [Foundry Agent Service ist jetzt GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), und dieses Release ist laser-fokussiert auf genau diese "alles danach"-Lücke.

## Gebaut auf der Responses API

Die Schlagzeile: der Foundry Agent Service der nächsten Generation basiert auf der OpenAI Responses API. Wenn du bereits mit diesem Wire-Protokoll baust, erfordert die Migration zu Foundry minimale Code-Änderungen. Was du gewinnst: Enterprise-Sicherheit, Private Networking, Entra RBAC, vollständiges Tracing und Evaluierung — auf deiner bestehenden Agent-Logik.

Die Architektur ist bewusst offen. Du bist nicht an einen Modell-Anbieter oder ein Orchestrierungs-Framework gebunden. Nutze DeepSeek fürs Planen, OpenAI für die Generierung, LangGraph für die Orchestrierung — die Runtime kümmert sich um die Konsistenz-Schicht.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> Wenn du vom `azure-ai-agents`-Paket kommst: Agenten sind jetzt First-Class-Operationen auf `AIProjectClient` in `azure-ai-projects`. Entferne die standalone-Abhängigkeit und nutze `get_openai_client()` um Responses zu steuern.

## Private Networking: der Enterprise-Blocker beseitigt

Das ist die Funktion, die Enterprise-Adoption freischaltet. Foundry unterstützt jetzt vollständiges End-to-End Private Networking mit BYO VNet:

- **Kein öffentlicher Egress** — Agent-Traffic berührt nie das öffentliche Internet
- **Container/Subnet-Injection** in dein Netzwerk für lokale Kommunikation
- **Tool-Konnektivität inklusive** — MCP-Server, Azure AI Search, Fabric-Datenagenten operieren alle über private Pfade

Der letzte Punkt ist entscheidend. Es sind nicht nur Inferenz-Aufrufe, die privat bleiben — jeder Tool-Aufruf und jede Retrieval-Anfrage bleibt ebenfalls innerhalb deiner Netzwerk-Grenze. Für Teams, die unter Datenklassifizierungsrichtlinien arbeiten, die externes Routing verbieten, war das was fehlte.

## MCP-Authentifizierung richtig gemacht

MCP-Server-Verbindungen unterstützen jetzt das volle Spektrum an Auth-Patterns:

| Auth-Methode | Wann verwenden |
|--------------|----------------|
| Key-basiert | Einfacher geteilter Zugriff für org-weite interne Tools |
| Entra Agent Identity | Service-to-Service; der Agent authentifiziert sich als er selbst |
| Entra Managed Identity | Projekt-Isolation; kein Credential-Management |
| OAuth Identity Passthrough | Benutzer-delegierter Zugriff; Agent handelt im Auftrag der Benutzer |

OAuth Identity Passthrough ist der interessante. Wenn Benutzer einem Agenten Zugriff auf ihre persönlichen Daten geben müssen — ihr OneDrive, ihre Salesforce-Org, eine SaaS-API mit Benutzer-Scope — handelt der Agent in ihrem Auftrag mit Standard-OAuth-Flows. Keine geteilte System-Identität, die vorgibt, alle zu sein.

## Voice Live: Sprache-zu-Sprache ohne das Leitungswirrwarr

Einem Agenten Sprache hinzuzufügen bedeutete bisher, STT, LLM und TTS zusammenzufügen — drei Services, drei Latenz-Hops, drei Abrechnungsflächen, alles von Hand synchronisiert. **Voice Live** kollabiert das in eine einzige verwaltete API mit:

- Semantische Sprachaktivitäts- und Sprechende-Erkennung (versteht Bedeutung, nicht nur Stille)
- Serverseitige Rauschunterdrückung und Echokompensation
- Barge-in-Unterstützung (Benutzer können mitten in der Antwort unterbrechen)

Sprachinteraktionen laufen durch die gleiche Agent-Runtime wie Text. Gleiche Evaluatoren, gleiche Traces, gleiche Kosten-Transparenz. Für Kundensupport, Außendienst oder Barrierefreiheits-Szenarien ersetzt das, was vorher eine individuelle Audio-Pipeline erforderte.

## Evaluierungen: von der Checkbox zum kontinuierlichen Monitoring

Hier wird Foundry ernst bezüglich Produktionsqualität. Das Evaluierungs-System hat jetzt drei Schichten:

1. **Mitgelieferte Evaluatoren** — Kohärenz, Relevanz, Begründetheit, Retrieval-Qualität, Sicherheit. Verbinde mit einem Dataset oder Live-Traffic und erhalte Scores zurück.

2. **Eigene Evaluatoren** — kodiere deine eigene Geschäftslogik, Ton-Standards und domänenspezifische Compliance-Regeln.

3. **Kontinuierliche Evaluierung** — Foundry sampelt Live-Produktionstraffic, führt deine Evaluator-Suite aus und zeigt Ergebnisse in Dashboards. Setze Azure-Monitor-Alerts für sinkende Begründetheit oder Sicherheitsschwellen-Verletzungen.

Alles wird in Azure Monitor Application Insights veröffentlicht. Agent-Qualität, Infrastruktur-Gesundheit, Kosten und App-Telemetrie — alles an einem Ort.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Sechs neue Regionen für gehostete Agenten

Gehostete Agenten sind jetzt verfügbar in East US, North Central US, Sweden Central, Southeast Asia, Japan East und mehr. Das ist wichtig für Datenresidenz-Anforderungen und um Latenz zu komprimieren, wenn dein Agent nahe an seinen Datenquellen läuft.

## Warum das für .NET-Entwickler wichtig ist

Auch wenn die Code-Samples im GA-Announcement Python-first sind, ist die zugrundeliegende Infrastruktur sprachunabhängig — und das .NET SDK für `azure-ai-projects` folgt den gleichen Mustern. Die Responses API, das Evaluierungs-Framework, das Private Networking, die MCP-Auth — all das ist von .NET aus verfügbar.

Wenn du darauf gewartet hast, dass KI-Agenten von "coole Demo" zu "kann ich tatsächlich auf der Arbeit ausliefern" werden, ist dieses GA-Release das Signal. Private Networking, ordentliche Auth, kontinuierliche Evaluierung und Produktions-Monitoring sind die Teile, die gefehlt haben.

## Zusammenfassung

Foundry Agent Service ist jetzt verfügbar. Installiere das SDK, öffne [das Portal](https://ai.azure.com) und fang an zu bauen. Der [Schnellstart-Guide](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) bringt dich in Minuten von null zu einem laufenden Agenten.

Für den vollständigen technischen Deep-Dive mit allen Code-Samples, schau dir das [GA-Announcement](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) an.
