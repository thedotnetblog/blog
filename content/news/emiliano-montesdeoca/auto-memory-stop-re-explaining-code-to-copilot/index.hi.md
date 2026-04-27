---
title: "क्या Copilot को हर दिन 68 मिनट कोड फिर से समझाने में लग रहे हैं? इसका हल है"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context rot असली है — आपका AI agent 30 turns के बाद drift करने लगता है, और आप हर घंटे compaction tax चुकाते हैं। auto-memory GitHub Copilot CLI को हजारों tokens जलाए बिना surgical recall देता है।"
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

क्या आप वह पल जानते हैं जब आपकी Copilot session `/compact` पर पहुँचती है और agent पूरी तरह भूल जाता है कि आप क्या कर रहे थे? अगले पाँच मिनट आप file structure, failing test, और वे तीन approaches फिर से समझाते हैं जिन्हें आप पहले ही आज़मा चुके हैं। फिर यह सब दोबारा होता है। और फिर दोबारा।

Desi Villanueva ने इसे time किया: **68 minutes per day** — सिर्फ़ re-orientation में। कोड लिखने में नहीं। PRs review करने में नहीं। बस AI को वह याद दिलाने में जो वह पहले से जानता था।

असल में ऐसा क्यों होता है, और इसका एक ठोस हल भी है।

## कॉन्टेक्स्ट विंडो की झूठी कहानी

आपके agent के बॉक्स पर एक बड़ा नंबर लिखा होता है। 200K tokens. बहुत बड़ा लगता है। व्यवहार में यह एक ceiling है, कोई गारंटी नहीं।

असल गणित यह है:

- 200K कुल context
- लगभग 65K MCP tools के लिए जो startup पर लोड होते हैं (~33%)
- लगभग 10K instruction files के लिए, जैसे `AGENTS.md` या `copilot-instructions.md`

इससे आपके पास लगभग **125K बचते हैं, उससे पहले कि आप एक शब्द भी लिखें**। और हालात और खराब हैं — LLMs context भरते जाने पर शालीनता से degrade नहीं होते। वे लगभग 60% capacity पर दीवार से टकरा जाते हैं। मॉडल 30 turns पहले कही गई बातें खोने लगता है, पहले दिए गए जवाबों का विरोध करता है, और 10 मिनट पहले जिन file names को बहुत आत्मविश्वास से बताया था, उन्हें भी hallucinate करने लगता है। उद्योग इसे "lost in the middle" problem कहता है।

प्रभावी सीमा: **45K tokens** उसके बाद quality गिरने लगती है। यानी शायद 20-30 active conversation turns, फिर agent drift करने लगता है। इसी वजह से आप हर 45 मिनट में `/compact` कर रहे हैं — इसलिए नहीं कि आपने 200K tokens भर दिए, बल्कि इसलिए कि model पहले ही 120K पर खराब होने लगा है।

## कॉम्पैक्शन टैक्स

हर `/compact` आपका flow state छीन लेता है। आप एक deep debugging session में हैं। shared context 30 मिनट से बन रहा था। agent को file structure, failing test, और hypothesis पता है। फिर warning आ जाती है।

- अनदेखा करें → agent धीरे-धीरे बेवकूफ होता जाता है, पुरानी state hallucinate करता है
- `/compact` चलाएँ → agent को 30 मिनट की investigation का दो पैराग्राफ़ का सार मिल जाता है

दोनों ही हालात में नुकसान होता है। दोनों ही हालात में आप अपने project को किसी नए join किए हुए employee की तरह दोहरा रहे होते हैं।

कड़वी बात? **Memory पहले से मौजूद है**। Copilot CLI हर session को `~/.copilot/session-store.db` नाम की local SQLite database में लिखता है — हर touched file, हर turn, हर checkpoint. सब disk पर मौजूद है. Agent बस उसे पढ़ नहीं सकता.

## auto-memory: एक recall layer, memory system नहीं

auto-memory के पीछे यही मुख्य विचार है: नया memory system मत बनाइए — जो पहले से है, उसके ऊपर एक read-only query layer बनाइए।

```bash
pip install auto-memory
```

करीब 1,900 lines of Python। Zero dependencies. 30 seconds में install.

Context को grep results से भरने के बजाय, आप agent को उस चीज़ तक surgical access देते हैं जो सच में मायने रखती है:

| ऑपरेशन | Tokens | आपको क्या मिलता है |
|--------|--------|---------------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 results, जिनमें से ज़्यादातर irrelevant हैं |
| `find . -name "*.py"` | ~2,000 | सभी Python files, बिना context के |
| Agent re-orientation | ~2,000 | आप उसे वह समझा रहे हैं जो उसे पहले से पता होना चाहिए |
| **`auto-memory files --json --limit 10`** | **~50** | **कल आपने जिन 10 files पर काम किया था** |

यह 200x improvement है। Agent archaeology dig छोड़ देता है और सीधे उस चीज़ पर पहुँच जाता है जो मायने रखती है।

Recommended flow: जब आप 50-70% context usage के पास पहुँचें, `/clear` चलाएँ और फिर prompt करें: "उन पिछली sessions की समीक्षा करो जिनमें हमने विषय X पर बात की थी"। Blind searches पर 12K tokens जलाने के बजाय, auto-memory relevant context को 50 में निकाल लेता है।

## यह .NET developers के लिए क्यों मायने रखता है

अगर आप GitHub Copilot CLI का इस्तेमाल .NET work के लिए कर रहे हैं — services scaffold करना, EF Core queries debug करना, Blazor components पर iterate करना — तो context rot की समस्या उतनी ही तेज़ी से आती है। Multiple projects, shared libraries, और deep call chains वाली complex solutions वही codebases हैं जहाँ agent सबसे जल्दी track खो देता है।

Install guide बताती है कि Copilot CLI को इसकी ओर कैसे point करना है। यह एक one-time setup है।

सच कहें तो? 68 minutes a day वापस पाना कोई छोटा quality-of-life tweak नहीं है। यह लगभग 6 hours a week है।

## समापन

Context rot एक वास्तविक architectural constraint है, कोई ऐसा bug नहीं जो बस patch होकर ठीक हो जाएगा। auto-memory आपका agent expensive, noisy re-exploration करने के बजाय cheap और precise recall mechanism देकर इस सीमा को bypass करता है। अगर आप GitHub Copilot CLI के साथ serious AI-assisted development कर रहे हैं, तो 30-second install वाकई क़ीमती है।

देखिए: [GitHub पर auto-memory](https://github.com/dezgit2025/auto-memory). Original post by Desi Villanueva: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).