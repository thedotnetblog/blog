---
title: "Foundry Agent Service GA हो गया: .NET Agent Builders के लिए वास्तव में क्या मायने रखता है"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft का Foundry Agent Service GA हो गया है — private networking, Voice Live, production evaluations, और एक open multi-model runtime के साथ। यहाँ जानिए क्या जानना ज़रूरी है।"
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "foundry-agent-service-ga-what-matters" >}}).*

सच कहें तो — एक AI agent का prototype बनाना सबसे आसान हिस्सा है। मुश्किल हिस्सा है उसके बाद का सब कुछ: इसे production में ले जाना उचित network isolation के साथ, ऐसे evaluations चलाना जिनका वास्तव में कुछ मतलब हो, compliance की आवश्यकताओं को संभालना, और रात 2 बजे चीज़ें तोड़ने से बचना।

[Foundry Agent Service अभी GA हो गया है](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), और यह release उस "सब कुछ बाद में" की खाई को पाटने पर केंद्रित है।

## Responses API पर निर्मित

मुख्य बात यह है: next-gen Foundry Agent Service OpenAI Responses API पर बनाया गया है। अगर आप पहले से उस wire protocol के साथ build कर रहे हैं, तो Foundry पर migrate करने के लिए न्यूनतम code बदलाव की ज़रूरत है। आपको मिलेगा: enterprise security, private networking, Entra RBAC, full tracing, और evaluation — आपके existing agent logic के ऊपर।

Architecture जानबूझकर open है। आप किसी एक model provider या एक orchestration framework से locked नहीं हैं। Planning के लिए DeepSeek, generation के लिए OpenAI, orchestration के लिए LangGraph इस्तेमाल करें — runtime consistency layer को संभालता है।

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

> अगर आप `azure-ai-agents` package से आ रहे हैं, तो अब agents `azure-ai-projects` में `AIProjectClient` पर first-class operations हैं। standalone pin हटाएं और responses चलाने के लिए `get_openai_client()` इस्तेमाल करें।

## Private networking: enterprise की बाधा दूर हुई

यह वह feature है जो enterprise adoption को unblock करता है। Foundry अब BYO VNet के साथ पूर्ण end-to-end private networking सपोर्ट करता है:

- **कोई public egress नहीं** — agent traffic कभी public internet से नहीं गुज़रता
- **Container/subnet injection** आपके network में local communication के लिए
- **Tool connectivity शामिल** — MCP servers, Azure AI Search, Fabric data agents सभी private paths पर काम करते हैं

आखिरी बात critical है। सिर्फ inference calls ही private नहीं रहती — हर tool invocation और retrieval call भी आपकी network boundary के अंदर रहती है। उन teams के लिए जो data classification policies के तहत काम करती हैं जो external routing को prohibit करती हैं, यही वह था जो missing था।

## MCP authentication सही तरीके से

MCP server connections अब auth patterns का पूरा spectrum सपोर्ट करते हैं:

| Auth method | कब उपयोग करें |
|-------------|-------------|
| Key-based | org-wide internal tools के लिए simple shared access |
| Entra Agent Identity | Service-to-service; agent खुद को authenticate करता है |
| Entra Managed Identity | Per-project isolation; कोई credential management नहीं |
| OAuth Identity Passthrough | User-delegated access; agent users की तरफ से काम करता है |

OAuth Identity Passthrough दिलचस्प है। जब users को किसी agent को अपने personal data तक access देने की ज़रूरत होती है — उनका OneDrive, उनका Salesforce org, एक user-scoped SaaS API — agent उनकी तरफ से standard OAuth flows के साथ काम करता है। कोई shared system identity नहीं जो सबका रूप धारण करे।

## Voice Live: बिना plumbing के speech-to-speech

पहले किसी agent में voice जोड़ने का मतलब था STT, LLM, और TTS को आपस में जोड़ना — तीन services, तीन latency hops, तीन billing surfaces, सब हाथ से synchronize किए जाते। **Voice Live** इसे एक single managed API में समेट देता है जिसमें:

- Semantic voice activity और end-of-turn detection (सिर्फ silence नहीं, meaning समझता है)
- Server-side noise suppression और echo cancellation
- Barge-in support (users mid-response interrupt कर सकते हैं)

Voice interactions उसी agent runtime से गुज़रती हैं जो text के लिए है। वही evaluators, वही traces, वही cost visibility। Customer support, field service, या accessibility scenarios के लिए, यह उस custom audio pipeline की जगह लेता है जिसकी पहले ज़रूरत थी।

## Evaluations: checkbox से continuous monitoring तक

यहाँ Foundry production quality के बारे में गंभीर हो जाता है। Evaluation system में अब तीन layers हैं:

1. **Out-of-the-box evaluators** — coherence, relevance, groundedness, retrieval quality, safety। किसी dataset या live traffic से connect करें और scores वापस पाएं।

2. **Custom evaluators** — अपनी business logic, tone standards, और domain-specific compliance rules encode करें।

3. **Continuous evaluation** — Foundry live production traffic sample करता है, आपका evaluator suite चलाता है, और dashboards के ज़रिए results सामने लाता है। Azure Monitor alerts सेट करें जब groundedness गिरे या safety thresholds breach हों।

सब कुछ Azure Monitor Application Insights में publish होता है। Agent quality, infrastructure health, cost, और app telemetry — सब एक ही जगह।

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

## Hosted agents के लिए छह नए regions

Hosted agents अब East US, North Central US, Sweden Central, Southeast Asia, Japan East, और अन्य में उपलब्ध हैं। यह data residency requirements के लिए और latency कम करने के लिए मायने रखता है जब आपका agent अपने data sources के करीब चलता है।

## .NET developers के लिए यह क्यों मायने रखता है

भले ही GA announcement के code samples Python-first हों, underlying infrastructure language-agnostic है — और `azure-ai-projects` का .NET SDK वही patterns follow करता है। Responses API, evaluation framework, private networking, MCP auth — यह सब .NET से उपलब्ध है।

अगर आप AI agents के "cool demo" से "मैं इसे actually काम पर ship कर सकता हूँ" बनने का इंतज़ार कर रहे थे, तो यह GA release वह signal है। Private networking, proper auth, continuous evaluation, और production monitoring वे टुकड़े थे जो missing थे।

## निष्कर्ष

Foundry Agent Service अभी उपलब्ध है। SDK install करें, [portal](https://ai.azure.com) खोलें, और build करना शुरू करें। [Quickstart guide](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) आपको zero से एक running agent तक minutes में ले जाती है।

सभी code samples के साथ पूरे technical deep-dive के लिए, [GA announcement](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) देखें।
