---
title: "Aspire 13.2 एक Docs CLI लेकर आया है — और आपका AI Agent भी इसका उपयोग कर सकता है"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 में aspire docs जोड़ा गया है — terminal छोड़े बिना official documentation खोजने, browse करने और पढ़ने के लिए एक CLI। यह AI agents के लिए tool की तरह भी काम करता है। यहाँ जानें यह क्यों मायने रखता है।"
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-docs-cli-ai-skills" >}}).*

आपने वो पल ज़रूर महसूस किया होगा जब आप किसी Aspire AppHost में गहरे डूबे हों, integrations wire up कर रहे हों, और आपको ठीक-ठीक जाँचना हो कि Redis integration किन parameters की उम्मीद करती है। आप browser पर alt-tab करते हैं, aspire.dev पर खोजते हैं, API docs को ध्यान से देखते हैं, फिर editor पर वापस आते हैं। Context खो गया। Flow टूट गया।

Aspire 13.2 ने [इसका हल ship किया है](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/)। `aspire docs` CLI आपको official Aspire documentation को सीधे अपने terminal से search, browse, और पढ़ने देता है। और चूंकि यह reusable services से backed है, AI agents और skills वही commands use करके docs lookup कर सकते हैं, न कि ऐसी APIs hallucinate करें जो exist ही नहीं करतीं।

## यह वास्तव में किस समस्या को हल करता है

David Pine original post में बिल्कुल सही बात कहते हैं: AI agents Aspire apps बनाने में developers की मदद करने में *बेकार* थे। वे `aspire run` की जगह `dotnet run` recommend करते, aspire.dev के docs के लिए learn.microsoft.com reference करते, outdated NuGet packages suggest करते, और — मेरी personal favorite — ऐसी APIs hallucinate करते जो exist ही नहीं करतीं।

क्यों? क्योंकि Aspire polyglot बनने से कहीं ज़्यादा समय तक .NET-specific था, और LLMs ऐसे training data से काम कर रहे हैं जो latest features से पहले का है। जब आप एक AI agent को actual docs lookup करने की क्षमता देते हैं, तो वह अंदाज़े लगाना बंद कर देता है और उपयोगी बनने लगता है।

## तीन commands, शून्य browser tabs

CLI refreshingly simple है:

### सभी docs list करें

```bash
aspire docs list
```

aspire.dev पर available हर documentation page return करता है। Machine-readable output चाहिए? `--format Json` जोड़ें।

### किसी topic को search करें

```bash
aspire docs search "redis"
```

weighted relevance scoring के साथ titles और content दोनों में search करता है। वही search engine जो internally documentation tooling को power करता है। आपको titles, slugs, और relevance scores के साथ ranked results मिलते हैं।

### पूरा page पढ़ें (या सिर्फ एक section)

```bash
aspire docs get redis-integration
```

पूरा page markdown के रूप में आपके terminal में stream करता है। सिर्फ एक section चाहिए?

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

सटीक precision। 500 lines scroll करने की ज़रूरत नहीं। बस वो हिस्सा जो आपको चाहिए।

## AI agent का angle

यहाँ AI tooling के साथ build करने वाले developers के लिए दिलचस्प बात है। वही `aspire docs` commands AI agents के लिए tools की तरह काम करते हैं — skills, MCP servers, या simple CLI wrappers के ज़रिये।

आपके AI assistant के stale training data के आधार पर Aspire APIs बनाने की बजाय, वह `aspire docs search "postgres"` call कर सकता है, official integration docs ढूंढ सकता है, सही page पढ़ सकता है, और आपको documented approach दे सकता है। Real-time, current documentation — model ने छह महीने पहले जो memorize किया था वह नहीं।

इसके पीछे का architecture जानबूझकर बनाया गया है। Aspire team ने एक one-off integration की बजाय reusable services (`IDocsIndexService`, `IDocsSearchService`, `IDocsFetcher`, `IDocsCache`) बनाई हैं। इसका मतलब है कि वही search engine terminal में इंसानों के लिए, आपके editor में AI agents के लिए, और आपके CI pipeline में automation के लिए काम करता है।

## Real-world scenarios

**Quick terminal lookups:** आप तीन files गहरे हैं और Redis config parameters चाहिए। दो commands, नब्बे सेकंड, काम पर वापस:

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**AI-assisted development:** आपकी VS Code skill CLI commands को wrap करती है। आप पूछते हैं "Add a PostgreSQL database to my AppHost" और agent जवाब देने से पहले actual docs lookup करता है। कोई hallucinations नहीं।

**CI/CD validation:** आपकी pipeline AppHost configurations को programmatically official documentation के against validate करती है। `--format Json` output `jq` और अन्य tools में cleanly pipe होता है।

**Custom knowledge bases:** अपना AI tooling बना रहे हैं? Structured JSON output को directly अपने knowledge base में pipe करें:

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

कोई web scraping नहीं। कोई API keys नहीं। वही structured data जो docs tooling internally use करती है।

## Documentation हमेशा live है

यही वह हिस्सा है जो मुझे सबसे ज़्यादा पसंद है। CLI एक snapshot download नहीं करता — यह ETag-based caching के साथ aspire.dev query करता है। जिस moment docs update होते हैं, आपका CLI और उस पर बना कोई भी skill उसे reflect करता है। कोई stale copies नहीं, कोई "but the wiki said..." moments नहीं।

## निष्कर्ष

`aspire docs` उन छोटी features में से एक है जो एक असली समस्या को cleanly हल करती है। इंसानों को terminal-native documentation access मिलती है। AI agents को अंदाज़े लगाना बंद करके actual docs reference करने का तरीका मिलता है। और यह सब एक ही source of truth से backed है।

अगर आप .NET Aspire के साथ build कर रहे हैं और अभी तक CLI try नहीं किया है, तो `aspire docs search "your-topic-here"` चलाएं और देखें कैसा लगता है। फिर उन commands को जो भी AI skill या automation setup आप use कर रहे हैं उसमें wrap करने पर विचार करें — आपके agents आपको धन्यवाद देंगे।

[David Pine का deep dive](https://davidpine.dev/posts/aspire-docs-mcp-tools/) देखें कि docs tooling कैसे बनी, और सभी details के लिए [official CLI reference](https://aspire.dev/reference/cli/commands/aspire-docs/)।
