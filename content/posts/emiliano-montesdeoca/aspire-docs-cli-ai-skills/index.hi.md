---
title: "Aspire 13.2 एक Docs CLI लाया — और आपका AI Agent भी इसे Use कर सकता है"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 aspire docs जोड़ता है — terminal छोड़े बिना official documentation search, browse और read करने का CLI। यह AI agents के लिए भी काम करता है।"
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-docs-cli-ai-skills" >}}).*

वह moment जानते हैं जब आप Aspire AppHost में गहरे होते हैं, integrations wire up कर रहे होते हैं, और आपको exactly check करना होता है कि Redis integration कौन से parameters expect करता है? आप browser में alt-tab करते हैं, aspire.dev पर खोजते हैं, API docs देखते हैं। Context lost।

Aspire 13.2 ने [इसका fix ship किया](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/)। `aspire docs` CLI आपको terminal से सीधे official Aspire documentation search, browse और read करने देता है।

## तीन commands, शून्य browser tabs

```bash
# सभी docs list करें
aspire docs list

# किसी topic को search करें
aspire docs search "redis"

# पूरा page read करें
aspire docs get redis-integration

# सिर्फ एक section
aspire docs get redis-integration --section "Add Redis resource"
```

## AI Agent angle

यहाँ से यह developers के लिए interesting हो जाता है जो AI tooling के साथ build कर रहे हैं। वही `aspire docs` commands AI agents के लिए tools के रूप में काम करते हैं।

आपका AI assistant stale training data पर based Aspire APIs बनाने की जगह `aspire docs search "postgres"` call कर सकता है, official integration docs find कर सकता है, और सही page read कर सकता है।

## समापन

`aspire docs` एक ऐसा small feature है जो real problem को cleanly solve करता है। [David Pine का deep dive](https://davidpine.dev/posts/aspire-docs-mcp-tools/) देखें।
