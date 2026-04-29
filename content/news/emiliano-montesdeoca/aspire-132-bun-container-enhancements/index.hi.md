---
title: "Aspire 13.2 में Bun, बेहतर कंटेनर, और कम डिबगिंग झंझट"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 Vite ऐप्स के लिए Bun का प्रथम-श्रेणी समर्थन जोड़ता है, Yarn की विश्वसनीयता सुधारता है, और ऐसे कंटेनर सुधार लाता है जो स्थानीय विकास के व्यवहार को ज़्यादा सटीक बनाते हैं। यहाँ असल में क्या बदला और क्यों मायने रखता है।"
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

अगर आप Aspire में .NET बैकएंड और JavaScript फ्रंटएंड बना रहे हैं, तो 13.2 वह अपडेट है जो चुपचाप आपका दिन बेहतर कर देता है। कोई चमकदार नए paradigm नहीं। बस उन चीज़ों में ठोस सुधार जो थोड़ी परेशान करने वाली थीं।

चलो देखते हैं असल में क्या आया।

## Bun अब प्रथम-श्रेणी का नागरिक है

सबसे बड़ी खबर: Aspire में Vite ऐप्स के लिए Bun समर्थन। एक fluent call, और काम खत्म।

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

अगर आपकी टीम पहले से Bun इस्तेमाल करती है — और शायद करती भी है, क्योंकि इसकी install time बहुत तेज़ है और startup भी कहीं ज़्यादा तेज़ होता है — तो Aspire अब आपको धारा के खिलाफ नहीं धकेलता। पहले Aspire npm मानकर चलता था और आपको workaround करना पड़ता था। अब `.withBun()` `.withYarn()` और डिफ़ॉल्ट npm behavior के साथ एक first-class विकल्प है।

यह क्यों मायने रखता है? क्योंकि JavaScript tooling की गति सीधे आपके inner dev loop को प्रभावित करती है। अगर हर बार नया environment उठाने पर आपका frontend dependencies install करने में 30 सेकंड लेता है, तो वह जोड़ता जाता है। Bun इसे काफ़ी हद तक घटा देता है।

अगर आप C# में author करना पसंद करते हैं, तो C# AppHost equivalent [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun) पर documented हैं — वही patterns लागू होते हैं।

## Yarn अब और विश्वसनीय है

Bun headlines ले जाता है, लेकिन Yarn users को भी कुछ शायद और महत्वपूर्ण मिलता है: कम mysterious failures. Aspire 13.2 `addViteApp()` के साथ `withYarn()` की reliability बेहतर करता है।

ऐसे fixes तब तक exciting नहीं लगते जब तक आपने 20 मिनट यह पता लगाने में न बिताए हों कि Yarn-backed frontend resource start क्यों नहीं हो रहा था। इसे fixed मानिए।

## ऐसा कंटेनर publishing जिसे आप सच में समझ सकें

दो container improvements जानने लायक हैं:

### Explicit Pull Policy

Docker Compose publishing अब `PullPolicy` support करता है, जिसमें `Never` option भी शामिल है:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

यह वह workflow है जो कहता है, “मैंने जो image पहले ही build कर ली है, वही इस्तेमाल करो और registry को बीच में मत लाओ।” यह तब बहुत उपयोगी है जब आप locally images पर iterate कर रहे हों जिन्हें आप manually build और publish करते हैं, या जब आपका CI एक image बनाता है और आप चाहते हैं कि Compose बिल्कुल उसी image का उपयोग करे, बिना किसी remote pull के।

### PostgreSQL 18+ Volumes फिर से काम करते हैं

PostgreSQL 18 ने अपनी internal data directory layout बदल दी। इससे Aspire में volume mapping silently टूट गई — आपका data volume setup हो जाता था, लेकिन persistence सही तरीके से काम नहीं करती थी। 13.2 यह ठीक करता है।

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

अगर आप PostgreSQL 18 या उससे नए version के साथ data volume चला रहे हैं, तो Aspire 13.2 पर अपडेट करिए और फिर इसके बारे में दोबारा मत सोचिए।

## Debugging की quality-of-life improvements

कुछ चीज़ें जो AppHost session को step through करते समय कम frustrating बनाती हैं:

- **Core types पर `DebuggerDisplayAttribute`** — `DistributedApplication`, resources, और endpoint expressions अब debugger में useful values दिखाते हैं, object trees में गहराई तक जाने की ज़रूरत नहीं
- **बेहतर `WaitFor` failure messages** — जब resources start होने में fail होते हैं, error context अब सच में मददगार है
- **`BeforeResourceStartedEvent` सही समय पर fire होता है** — सिर्फ़ तब जब कोई resource वास्तव में start हो रहा हो, न कि unrelated state transitions पर
- **`launchSettings.json` ज़्यादा resilient है** — malformed setting के चलते dev startup के corrupt होने की संभावना कम

इनमें से कोई भी improvement अकेले में बहुत बड़ा नहीं है, लेकिन मिलकर debugging experience की friction कम करते हैं। अगर आपने कभी Aspire resource object के भीतर तीन level तक उतरकर यह पता लगाया हो कि वह कौन सा endpoint इस्तेमाल कर रहा है, तो सिर्फ़ debugger display improvement ही update के लायक है।

## समापन

Aspire 13.2 एक focused quality release है। Bun support headline है, लेकिन container और debugging improvements वही चीज़ें हैं जो रोज़मर्रा के काम को आसान बनाएँगी। अपडेट करना क़ाबिल-ए-गौर है — खासकर अगर आप PostgreSQL 18 के साथ data volumes इस्तेमाल कर रहे हैं।

पूरा विवरण [David Pine की original post](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) और [Aspire 13.2 whats new docs](https://aspire.dev/whats-new/aspire-13-2/) में है।