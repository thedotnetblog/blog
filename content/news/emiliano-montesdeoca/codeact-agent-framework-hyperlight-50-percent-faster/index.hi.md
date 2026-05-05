---
title: "Agent Framework में CodeAct: अपने एजेंट की लेटेंसी को आधा कैसे करें"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct बहु-चरण टूल चेन को एक सैंडबॉक्स्ड कोड ब्लॉक में संकुचित करता है — लेटेंसी 52% और टोकन उपयोग 64% कम करता है।"
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल संस्करण के लिए [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

हर एजेंट प्रोजेक्ट में एक ऐसा पल आता है जब आप ट्रेस देखते हैं और सोचते हैं: "इसमें इतना समय क्यों लग रहा है?" मॉडल ठीक है। टूल काम कर रहे हैं। लेकिन एक ऐसे परिणाम के लिए सात राउंड ट्रिप हो रहे हैं जो एक बार में की जा सकती थी।

यही वह समस्या है जिसे CodeAct हल करता है — और [Agent Framework टीम ने नए `agent-framework-hyperlight` पैकेज के माध्यम से अल्फा सपोर्ट जारी किया है](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)।

## CodeAct क्या है?

[CodeAct पैटर्न](https://arxiv.org/abs/2402.01030) सुंदर रूप से सरल है: मॉडल को एक-एक करके टूल कॉल करने के बजाय, उसे एक `execute_code` टूल दें और पूरी योजना को एक छोटे Python प्रोग्राम के रूप में व्यक्त करने दें।

| तरीका | समय | टोकन |
|--------|------|--------|
| पारंपरिक | 27.81s | 6,890 |
| CodeAct | 13.23s | 2,489 |
| **सुधार** | **52.4%** | **63.9%** |

## सुरक्षा: Hyperlight माइक्रो-VM

`agent-framework-hyperlight` पैकेज [Hyperlight](https://github.com/hyperlight-dev/hyperlight) माइक्रो-VM का उपयोग करता है। प्रत्येक `execute_code` कॉल को अपना नया माइक्रो-VM मिलता है। स्टार्टअप मिलीसेकंड में होता है। आइसोलेशन मूल रूप से मुफ्त है।

आपके टूल होस्ट पर चलते रहते हैं। मॉडल द्वारा जेनरेट किया गया कोड सैंडबॉक्स में चलता है। यह सही विभाजन है।

## न्यूनतम सेटअप

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

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

## कब CodeAct उपयोग करें

**CodeAct का उपयोग करें जब:**
- कार्य में कई छोटी टूल कॉल हों (लुकअप, जॉइन, गणना)
- लेटेंसी और टोकन लागत महत्वपूर्ण हो
- मॉडल-जेनरेटेड कोड के लिए मजबूत आइसोलेशन चाहिए

**पारंपरिक टूल-कॉलिंग रखें जब:**
- एजेंट प्रति टर्न केवल एक-दो टूल कॉल करता हो
- प्रत्येक कॉल में अलग-अलग अनुमोदन की जरूरत हो

## अभी आज़माएं

```bash
pip install agent-framework-hyperlight --pre
```

[Agent Framework ब्लॉग की पूरी पोस्ट](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) पढ़ें।
