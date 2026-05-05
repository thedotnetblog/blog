---
title: "Echtzeit-Multi-Agent-UIs Bauen, Die Sich Nicht Wie eine Black Box Anfühlen"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI und Microsoft Agent Framework verbünden sich, um Multi-Agent-Workflows ein richtiges Frontend zu geben — mit Echtzeit-Streaming, menschlichen Freigaben und voller Transparenz darüber, was eure Agenten tun."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Hier ist das Ding mit Multi-Agent-Systemen: Sie sehen in Demos unglaublich aus. Drei Agenten, die Arbeit weiterreichen, Probleme lösen, Entscheidungen treffen. Dann versuchst du es echten Benutzern zu zeigen und... Stille. Ein drehender Ladeindikator. Keine Ahnung, welcher Agent was macht oder warum das System pausiert ist. Das ist kein Produkt — das ist ein Vertrauensproblem.

Das Microsoft Agent Framework Team hat gerade einen [fantastischen Walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) veröffentlicht, wie man MAF-Workflows mit [AG-UI](https://github.com/ag-ui-protocol/ag-ui) kombiniert — einem offenen Protokoll zum Streamen von Agent-Ausführungsereignissen an ein Frontend über Server-Sent Events. Und ehrlich gesagt? Das ist genau die Brücke, die uns gefehlt hat.

## Warum das für .NET-Entwickler wichtig ist

Wenn du KI-gestützte Apps baust, bist du wahrscheinlich schon an diese Wand gestoßen. Deine Backend-Orchestrierung funktioniert super — Agenten übergeben aneinander, Tools feuern, Entscheidungen werden getroffen. Aber das Frontend hat keine Ahnung, was hinter den Kulissen passiert. AG-UI löst das, indem es ein Standardprotokoll zum Streamen von Agent-Events definiert (denk an `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) direkt an deine UI-Schicht über SSE.

Die Demo ist ein Kundenservice-Workflow mit drei Agenten: ein Triage-Agent, der Anfragen weiterleitet, ein Erstattungs-Agent für Geldangelegenheiten, und ein Bestell-Agent für Austauschvorgänge. Jeder Agent hat seine eigenen Tools, und die Handoff-Topologie ist explizit definiert — kein "finde es aus dem Prompt heraus"-Vibe.

## Die Handoff-Topologie ist der eigentliche Star

Was mir aufgefallen ist, ist wie `HandoffBuilder` dir erlaubt, einen gerichteten Routing-Graphen zwischen Agenten zu deklarieren:

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

Jedes `add_handoff` erstellt eine gerichtete Kante mit einer natürlichsprachlichen Beschreibung. Das Framework generiert Handoff-Tools für jeden Agenten basierend auf dieser Topologie. Routing-Entscheidungen basieren also auf deiner Orchestrierungsstruktur, nicht nur darauf, was das LLM gerade für richtig hält. Das ist ein riesiger Gewinn für die Produktionszuverlässigkeit.

## Human-in-the-Loop, das tatsächlich funktioniert

Die Demo zeigt zwei Unterbrechungsmuster, die jede echte Agent-App braucht:

**Tool-Genehmigungs-Unterbrechungen** — wenn ein Agent ein Tool aufruft, das mit `approval_mode="always_require"` markiert ist, pausiert der Workflow und sendet ein Event. Das Frontend rendert ein Genehmigungs-Modal mit dem Tool-Namen und den Argumenten. Keine Token-verbrennenden Retry-Schleifen — einfach ein sauberer Pause-Genehmigung-Fortsetzen-Ablauf.

**Informationsanfrage-Unterbrechungen** — wenn ein Agent mehr Kontext vom Benutzer braucht (wie eine Bestell-ID), pausiert er und fragt nach. Das Frontend zeigt die Frage an, der Benutzer antwortet, und die Ausführung wird genau dort fortgesetzt, wo sie aufgehört hat.

Beide Muster werden als Standard-AG-UI-Events gestreamt, sodass dein Frontend keine agenten-spezifische Logik braucht — es rendert einfach jedes Event, das über die SSE-Verbindung kommt.

## Die Anbindung ist überraschend einfach

Die Integration zwischen MAF und AG-UI ist ein einziger Funktionsaufruf:

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

Die `workflow_factory` erstellt einen frischen Workflow pro Thread, sodass jede Konversation isolierten State bekommt. Der Endpoint übernimmt die gesamte SSE-Verkabelung automatisch. Wenn du bereits FastAPI nutzt (oder es als leichte Schicht hinzufügen kannst), ist das praktisch ohne Reibungsverluste.

## Meine Einschätzung

Für uns .NET-Entwickler ist die sofortige Frage: „Geht das auch in C#?" Das Agent Framework ist für .NET und Python verfügbar, und das AG-UI-Protokoll ist sprachunabhängig (es ist nur SSE). Obwohl diese spezifische Demo Python und FastAPI verwendet, lässt sich das Muster direkt übertragen. Du könntest eine ASP.NET Core Minimal API mit SSE-Endpoints nach dem gleichen AG-UI-Event-Schema aufbauen.

Die wichtigere Erkenntnis ist, dass Multi-Agent-UIs zu einem erstklassigen Thema werden — nicht mehr nur ein Nachgedanke. Wenn du irgendetwas baust, wo Agenten mit Menschen interagieren — Kundenservice, Genehmigungs-Workflows, Dokumentenverarbeitung — dann ist diese Kombination aus MAF-Orchestrierung und AG-UI-Transparenz das Muster, dem man folgen sollte.

## Zusammenfassung

AG-UI + Microsoft Agent Framework gibt dir das Beste aus beiden Welten: robuste Multi-Agent-Orchestrierung im Backend und Echtzeit-Transparenz im Frontend. Keine Black-Box-Agent-Interaktionen mehr.

Schau dir den [vollständigen Walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) und das [AG-UI-Protokoll-Repository](https://github.com/ag-ui-protocol/ag-ui) an, um tiefer einzutauchen.
