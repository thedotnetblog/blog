---
title: "एजेंट बनाना आसान हिस्सा है — उन्हें सुरक्षित रूप से चलाना मुश्किल हिस्सा है"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework और Agent Governance Toolkit मिलकर रनटाइम पॉलिसी लागू करते हैं, टूल कॉल को नियंत्रित करते हैं और Merkle-चेन ऑडिट लॉग प्रदान करते हैं — एजेंट के प्रॉम्प्ट बदले बिना।"
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

AI एजेंट डेवलपमेंट में एक पैटर्न है जिसे मैंने "डेमो पछतावा" कहना शुरू किया है। एजेंट डेमो में बहुत अच्छा काम करता है। फिर कोई पूछता है: क्या होगा अगर यह गलत टूल को कॉल करे? अगर इसने उस डेटा को एक्सेस किया जो नहीं करना चाहिए? किसने ऑडिट किया?

Microsoft Agent Framework बिल्डिंग और ऑर्केस्ट्रेशन में आपका साथ देता है। Agent Governance Toolkit (AGT) उसके बाद का हिस्सा कवर करता है — गवर्नेंस, पॉलिसी एन्फोर्समेंट, और रनटाइम ऑडिटेबिलिटी।

## प्रत्येक प्रोजेक्ट वास्तव में क्या करता है

**Microsoft Agent Framework (MAF)** प्रोग्रामिंग मॉडल देता है: मल्टी-एजेंट वर्कफ्लो, A2A प्रोटोकॉल इंटरऑपेरेबिलिटी, मिडलवेयर हुक्स, मेमोरी, और Foundry Agent Service के जरिए मैनेज्ड होस्टिंग। यह मॉडल इनपुट/आउटपुट लेवल पर कंटेंट सेफ्टी हैंडल करता है।

**Agent Governance Toolkit (AGT)** उसी मिडलवेयर पाइपलाइन में प्लग होकर *एक्शन* को गवर्न करता है। हर टूल कॉल, रिसोर्स एक्सेस, और इंटर-एजेंट मैसेज को एग्जीक्यूशन से पहले पॉलिसी के विरुद्ध मूल्यांकन किया जाता है। सब-मिलीसेकंड ओवरहेड। कोई साइडकार नहीं, कोई प्रॉक्सी नहीं, कोई प्रॉम्प्ट नहीं बदले।

```
एजेंट एक्शन --> पॉलिसी चेक --> अनुमति / अस्वीकार --> ऑडिट लॉग    (< 0.1 ms)
```

अलग-अलग लेयर, पूरा कवरेज, एक पाइपलाइन।

## जुड़ना बस मिडलवेयर जोड़ना है

Python में, AGT उसी `middleware` पैरामीटर में जोड़ता है जिसे आप लॉगिंग या कंटेंट फिल्टर के लिए इस्तेमाल करेंगे:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

.NET में `.Use()` के जरिए वही पैटर्न:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

वही एजेंट, वही ऑर्केस्ट्रेशन, वही टूल्स। AGT एजेंट लॉजिक को बदले बिना गवर्नेंस क्षमताएं जोड़ता है।

## आपको क्या मिलता है

- **GovernancePolicyMiddleware** — हर एक्शन को डिक्लेरेटिव पॉलिसी नियमों के विरुद्ध मूल्यांकन करता है
- **CapabilityGuardMiddleware** — अलाउलिस्ट जो तय करती है कि एजेंट को कौन से टूल कॉल करने की अनुमति है (`approve_small_loan` टूल ऊपर की अनुमति सूची में जानबूझकर नहीं है)
- **RogueDetectionMiddleware** — रनटाइम पर असामान्य व्यवहार पैटर्न का पता लगाता है
- **AuditTrailMiddleware** — Merkle-चेन्ड ऑडिट लॉग ताकि हर एक्शन क्रिप्टोग्राफिकली टैम्पर-एविडेंट हो

अंतिम वाला कम्प्लायंस के लिए मायने रखता है। Merkle चेन का मतलब है: अगर कोई लॉग को बदलता है, चेन टूट जाती है। ऑडिट ही प्रमाण है।

## पांच उद्योग परिदृश्य

AGT रिपो में पांच पूरे एंड-टू-एंड परिदृश्य हैं: वित्तीय सेवाएं (लोन अधिकारी), स्वास्थ्य सेवा (रोगी डेटा), कानूनी (अनुबंध समीक्षा), सरकार (नागरिक सेवाएं), और निर्माण (गुणवत्ता नियंत्रण)। प्रत्येक वास्तविक MAF एजेंट को वास्तविक AGT गवर्नेंस मिडलवेयर के साथ जोड़ता है।

ये खिलौना डेमो नहीं हैं। ये वही परिदृश्य हैं जहां आपको वास्तव में प्रोडक्शन में गवर्नेंस की जरूरत होगी।

## निष्कर्ष

अगर आप ऐसे एजेंट बना रहे हैं जो वास्तविक डेटा को छूते हैं, परिणाम वाले निर्णय लेते हैं, या प्रोडक्शन में बिना निगरानी के चलते हैं — गवर्नेंस वैकल्पिक नहीं है। MAF + AGT का कॉम्बिनेशन आपको पूरा स्टैक देता है: Agent Framework से बनाएं, AGT से गवर्न करें।

दोनों प्रोजेक्ट ओपन सोर्स हैं। मूल लेख में पूरे कोड उदाहरणों के लिंक हैं।

मूल पोस्ट: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
