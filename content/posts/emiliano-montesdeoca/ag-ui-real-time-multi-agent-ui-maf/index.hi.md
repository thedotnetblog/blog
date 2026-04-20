---
title: "रियल-टाइम Multi-Agent UIs बनाना जो Black Box की तरह न लगें"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI और Microsoft Agent Framework मिलकर multi-agent workflows को एक उचित frontend देते हैं — real-time streaming, human approvals, और आपके agents क्या कर रहे हैं इसकी पूरी जानकारी के साथ।"
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

multi-agent systems के बारे में एक बात यह है: demos में वे बेहद शानदार लगते हैं। तीन agents काम आगे-पीछे भेज रहे हैं, समस्याएँ सुलझा रहे हैं, निर्णय ले रहे हैं। फिर आप इसे असली users के सामने रखने की कोशिश करते हैं और... खामोशी। एक घूमता हुआ indicator। कोई अंदाज़ा नहीं कि कौन-सा agent क्या कर रहा है या सिस्टम क्यों रुका हुआ है। यह कोई product नहीं है — यह एक भरोसे की समस्या है।

Microsoft Agent Framework team ने अभी-अभी MAF workflows को [AG-UI](https://github.com/ag-ui-protocol/ag-ui) के साथ जोड़ने पर एक [शानदार walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) प्रकाशित किया है। AG-UI एक open protocol है जो Server-Sent Events के ज़रिए agent execution events को frontend पर stream करता है। और सच में? यही वह bridge है जिसकी हमें कमी थी।

## .NET developers के लिए यह क्यों मायने रखता है

अगर आप AI-powered apps बना रहे हैं, तो आप शायद इस दीवार से टकरा चुके हैं। आपका backend orchestration बढ़िया काम करता है — agents एक-दूसरे को काम सौंपते हैं, tools चलते हैं, फैसले होते हैं। लेकिन frontend को पर्दे के पीछे क्या हो रहा है, इसका कोई अंदाज़ा नहीं। AG-UI इसे ठीक करता है — यह agent events (जैसे `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) को SSE पर सीधे आपकी UI layer तक stream करने के लिए एक standard protocol परिभाषित करता है।

जो demo उन्होंने बनाया वह तीन agents वाला customer support workflow है: एक triage agent जो requests को route करता है, एक refund agent जो पैसों का काम संभालता है, और एक order agent जो replacements manage करता है। हर agent के अपने tools हैं, और handoff topology स्पष्ट रूप से परिभाषित है — "prompt से खुद समझ लो" वाला कोई झमेला नहीं।

## Handoff topology असली सितारा है

जो चीज़ मेरी नज़र में आई वह यह है कि `HandoffBuilder` आपको agents के बीच एक directed routing graph घोषित करने देता है:

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

हर `add_handoff` एक natural-language description के साथ एक directed edge बनाता है। Framework इस topology के आधार पर हर agent के लिए handoff tools generate करता है। तो routing के फैसले आपकी orchestration structure पर आधारित हैं, न कि LLM की मर्ज़ी पर। production reliability के लिए यह बहुत बड़ी बात है।

## Human-in-the-loop जो वाकई काम करता है

Demo में दो interrupt patterns दिखाए गए हैं जो किसी भी real-world agent app को चाहिए:

**Tool approval interrupts** — जब कोई agent `approval_mode="always_require"` वाला tool call करता है, तो workflow रुक जाता है और एक event emit होता है। Frontend tool name और arguments के साथ एक approval modal render करता है। कोई token-burning retry loops नहीं — बस एक साफ pause-approve-resume flow।

**Information request interrupts** — जब किसी agent को user से ज़्यादा context चाहिए (जैसे कोई order ID), तो वह रुकता है और पूछता है। Frontend सवाल दिखाता है, user जवाब देता है, और execution ठीक वहाँ से दोबारा शुरू होती है जहाँ वह रुकी थी।

दोनों patterns standard AG-UI events की तरह stream होते हैं, इसलिए आपके frontend को हर agent के लिए custom logic की ज़रूरत नहीं — वह बस SSE connection से आने वाला event render करता है।

## Wiring up करना हैरानी की हद तक आसान है

MAF और AG-UI के बीच integration एक single function call है:

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

`workflow_factory` हर thread के लिए एक fresh workflow बनाता है, इसलिए हर conversation को isolated state मिलती है। Endpoint सारी SSE plumbing अपने आप handle करता है। अगर आप पहले से FastAPI use कर रहे हैं (या इसे एक lightweight layer के रूप में जोड़ सकते हैं), तो यह लगभग zero friction है।

## मेरी राय

हम .NET developers के लिए तुरंत यह सवाल उठता है: "क्या मैं यह C# में कर सकता हूँ?" Agent Framework .NET और Python दोनों के लिए उपलब्ध है, और AG-UI protocol language-agnostic है (यह बस SSE है)। तो यह specific demo Python और FastAPI use करता है, लेकिन pattern सीधे translate होता है। आप same AG-UI event schema का पालन करते हुए SSE endpoints के साथ एक ASP.NET Core minimal API wire up कर सकते हैं।

बड़ी बात यह है कि multi-agent UIs एक first-class concern बनती जा रही हैं, afterthought नहीं। अगर आप कुछ ऐसा बना रहे हैं जहाँ agents humans के साथ interact करते हैं — customer support, approval workflows, document processing — तो MAF orchestration और AG-UI transparency का यह combination वह pattern है जिसे follow करना चाहिए।

## Wrapping up

AG-UI + Microsoft Agent Framework आपको दोनों दुनियाओं का सर्वश्रेष्ठ देता है: backend पर robust multi-agent orchestration और frontend पर real-time visibility। Black-box agent interactions अब नहीं।

और गहराई से जानने के लिए [full walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) और [AG-UI protocol repo](https://github.com/ag-ui-protocol/ag-ui) देखें।
