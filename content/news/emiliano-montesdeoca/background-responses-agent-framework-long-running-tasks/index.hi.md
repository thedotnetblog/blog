---
title: "Microsoft Agent Framework में Background Responses: Timeout की चिंता अब खत्म"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework अब आपको continuation tokens के साथ long-running AI tasks को offload करने देता है। यहाँ जानिए background responses कैसे काम करते हैं और आपके .NET agents के लिए ये क्यों महत्वपूर्ण हैं।"
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

अगर आपने o3 या GPT-5.2 जैसे reasoning models के साथ कुछ बनाया है, तो आप वो दर्द जानते हैं। आपका agent एक complex task पर सोचना शुरू करता है, client वहाँ इंतज़ार करता है, और "यह ठीक है" से "क्या यह crash हो गया?" के बीच कहीं आपका connection timeout हो जाता है। वो सारा काम? बेकार।

Microsoft Agent Framework ने [background responses](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) ship किए हैं — और सच में, यह उन features में से एक है जो पहले दिन से ही होना चाहिए था।

## Blocking calls की समस्या

एक पारंपरिक request-response pattern में, आपका client तब तक block रहता है जब तक agent finish नहीं हो जाता। यह quick tasks के लिए ठीक काम करता है। लेकिन जब आप एक reasoning model से deep research, multi-step analysis, या 20-page report generate करने को कहते हैं? आप wall-clock time में मिनटों की बात कर रहे हैं। उस window के दौरान:

- HTTP connections timeout हो सकते हैं
- Network blips पूरे operation को बर्बाद कर देते हैं
- आपका user spinner देखता है और सोचता है कि कुछ हो भी रहा है या नहीं

Background responses इसे उलट देते हैं।

## Continuation tokens कैसे काम करते हैं

Block होने की बजाय, आप agent task kick off करते हैं और एक **continuation token** वापस पाते हैं। इसे एक repair shop के claim ticket की तरह समझें — आप counter पर खड़े नहीं रहते, आप तब वापस आते हैं जब वो तैयार हो जाए।

Flow सीधा है:

1. अपना request `AllowBackgroundResponses = true` के साथ भेजें
2. अगर agent background processing support करता है, तो आपको एक continuation token मिलता है
3. अपने schedule पर poll करें जब तक token `null` न आ जाए — इसका मतलब है result तैयार है

यहाँ .NET version है:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Poll until complete
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

अगर agent तुरंत complete हो जाता है (simple tasks, वे models जिन्हें background processing की ज़रूरत नहीं), तो कोई continuation token return नहीं होता। आपका code बस काम करता है — कोई special handling ज़रूरी नहीं।

## Resume के साथ Streaming: असली जादू

Fire-and-forget scenarios के लिए polling ठीक है, लेकिन जब आप real-time progress चाहते हों? Background responses built-in resumption के साथ streaming भी support करते हैं।

हर streamed update अपना खुद का continuation token carry करता है। अगर mid-stream आपका connection drop हो जाए, तो आप ठीक वहीं से pick up करते हैं जहाँ छोड़ा था:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Simulate a network interruption
}

// Resume from exactly where we left off
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

Agent server-side processing जारी रखता है चाहे आपके client के साथ कुछ भी हो रहा हो। यह built-in fault tolerance है बिना आपके retry logic या circuit breakers लिखे।

## इसे वास्तव में कब use करें

हर agent call को background responses की ज़रूरत नहीं है। Quick completions के लिए, आप बिना किसी कारण complexity जोड़ रहे होंगे। लेकिन यहाँ वे shine करते हैं:

- **Complex reasoning tasks** — multi-step analysis, deep research, कुछ भी जो reasoning model को वास्तव में सोचने पर मजबूर करे
- **Long content generation** — detailed reports, multi-part documents, extensive analysis
- **Unreliable networks** — mobile clients, edge deployments, flaky corporate VPNs
- **Async UX patterns** — task submit करें, कुछ और करें, results के लिए वापस आएं

हम .NET developers जो enterprise apps बना रहे हैं, उनके लिए वो आखिरी scenario खास दिलचस्प है। एक Blazor app के बारे में सोचें जहाँ user एक complex report request करता है — आप agent task fire off करते हैं, उन्हें एक progress indicator दिखाते हैं, और उन्हें काम करते रहने देते हैं। कोई WebSocket gymnastics नहीं, कोई custom queue infrastructure नहीं, बस एक token और एक poll loop।

## निष्कर्ष

Background responses Microsoft Agent Framework में अभी .NET और Python दोनों के ज़रिए उपलब्ध हैं। अगर आप ऐसे agents बना रहे हैं जो simple Q&A से ज़्यादा complex कुछ करते हैं, तो यह अपने toolkit में जोड़ने लायक है। Continuation token pattern चीज़ों को simple रखता है जबकि एक बहुत real production problem solve करता है।

Complete API reference और अधिक examples के लिए [full documentation](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) देखें।
