---
title: "Creació d'interfícies d'usuari multiagent en temps real que no semblin com una caixa negra"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI i Microsoft Agent Framework s'uneixen per oferir als fluxos de treball multiagent una interfície adequada, amb transmissió en temps real, aprovacions humanes i visibilitat total del que estan fent els vostres agents."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

Això és el que passa amb els sistemes multiagent: tenen un aspecte increïble a les demostracions. Tres agents que passen treballant, resolent problemes, prenent decisions. Aleshores intentes posar-ho davant dels usuaris reals i... silenci. Un indicador de gir. No hi ha idea de quin agent està fent què o per què el sistema està en pausa. Això no és un producte, és un problema de confiança.

L'equip de Microsoft Agent Framework acaba de publicar una [revisió fantàstica](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) sobre la combinació de fluxos de treball MAF amb [AG-UI](https://github.com/ag-ui-protocol/ag-ui), un protocol obert per a esdeveniments d'execució d'agents de transmissió a una interfície sobre esdeveniments enviats pel servidor. I sincerament? Aquest és el tipus de pont que hem trobat a faltar.

## Per què això és important per als desenvolupadors de.NET

Si esteu creant aplicacions basades en intel·ligència artificial, probablement heu tocat aquest mur. La vostra orquestració de fons funciona molt bé: els agents s'entreguen, les eines es disparen i es prenen decisions. Però la interfície no té ni idea del que passa darrere de les escenes. AG-UI ho soluciona mitjançant la definició d'un protocol estàndard per als esdeveniments de l'agent de transmissió (penseu a `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) directament a la vostra capa d'IU a través de SSE.

La demostració que van crear és un flux de treball d'atenció al client amb tres agents: un agent de triatge que encamina les sol·licituds, un agent de reemborsament que gestiona els diners i un agent de comandes que gestiona les substitucions. Cada agent té les seves pròpies eines i la topologia de traspàs es defineix explícitament: no hi ha vibracions de "esbrinar-ho a partir del missatge".

## La topologia de traspàs és la veritable estrella

El que em va cridar l'atenció és com `HandoffBuilder` us permet declarar un gràfic d'encaminament dirigit entre agents:

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

Cada `add_handoff` crea una vora dirigida amb una descripció en llenguatge natural. El marc genera eines de transferència per a cada agent basant-se en aquesta topologia. Per tant, les decisions d'encaminament es basen en la vostra estructura d'orquestració, no només en el que el LLM vulgui fer. Això és un gran negoci per a la fiabilitat de la producció.

## Human-in-the-loop que realment funciona

La demostració mostra dos patrons d'interrupció que necessita qualsevol aplicació d'agent del món real:

**L'aprovació de l'eina s'interromp**: quan un agent truca a una eina marcada amb `approval_mode="always_require"`, el flux de treball s'atura i emet un esdeveniment. La interfície representa un modal d'aprovació amb el nom de l'eina i els arguments. No hi ha bucles de reintent de gravació de testimonis, només un flux net de pausa, aprovació i reinici.

**La sol·licitud d'informació s'interromp**: quan un agent necessita més context de l'usuari (com ara un identificador de comanda), s'atura i pregunta. La interfície mostra la pregunta, l'usuari respon i l'execució es reprèn exactament des d'on es va aturar.

Tots dos patrons es transmeten com a esdeveniments AG-UI estàndard, de manera que la vostra interfície no necessita lògica personalitzada per agent; només representa qualsevol esdeveniment que passi a través de la connexió SSE.

## El cablejat és sorprenentment senzill

La integració entre MAF i AG-UI és una única trucada de funció:

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

El `workflow_factory` crea un flux de treball nou per fil, de manera que cada conversa té un estat aïllat. El punt final gestiona tota la fontaneria SSE automàticament. Si ja esteu utilitzant FastAPI (o podeu afegir-lo com a capa lleugera), això és gairebé zero fricció.

## La meva opinió

Per als desenvolupadors de.NET, la pregunta immediata és: "Puc fer això en C#?" L'Agent Framework està disponible tant per a.NET com per a Python, i el protocol AG-UI és independent de l'idioma (només és SSE). Així, mentre que aquesta demostració específica utilitza Python i FastAPI, el patró es tradueix directament. Podeu connectar una API mínima ASP.NET Core amb punts finals SSE seguint el mateix esquema d'esdeveniments AG-UI.

El més important és que les interfícies d'usuari multiagent s'estan convertint en una preocupació de primera classe, no en una idea posterior. Si esteu creant qualsevol cosa on els agents interactuen amb humans (atenció al client, fluxos de treball d'aprovació, processament de documents), aquesta combinació d'orquestració MAF i transparència AG-UI és el patró a seguir.

## Tancant

AG-UI + Microsoft Agent Framework us ofereix el millor dels dos mons: una robusta orquestració multiagent al backend i visibilitat en temps real al frontend. No més interaccions d'agent de caixa negra.

Fes una ullada a la [revisió completa](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) i al [repositori del protocol AG-UI](https://github.com/ag-ui-protocol/ag-ui) per aprofundir.
