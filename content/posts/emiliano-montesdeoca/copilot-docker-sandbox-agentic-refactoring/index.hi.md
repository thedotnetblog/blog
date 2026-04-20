---
title: "Docker Sandbox, Copilot Agents को आपकी मशीन को जोखिम में डाले बिना Code Refactor करने देता है"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox, GitHub Copilot agents को refactoring के लिए एक सुरक्षित microVM देता है — कोई permission prompt नहीं, host को कोई खतरा नहीं। यहाँ जानें यह बड़े पैमाने पर .NET modernization के लिए सब कुछ कैसे बदलता है।"
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

अगर आपने Copilot के agent mode का उपयोग छोटे edits से परे किसी काम के लिए किया है, तो आप वह तकलीफ जानते हैं। हर file write, हर terminal command — एक और permission prompt। अब कल्पना करें कि यह 50 projects में चलाना हो। मज़ेदार नहीं।

Azure team ने [GitHub Copilot agents के लिए Docker Sandbox](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/) के बारे में एक post publish किया है, और सच में, यह सबसे practical agentic tooling improvements में से एक है जो मैंने देखी है। यह microVMs का उपयोग करता है ताकि Copilot को एक पूरी तरह से isolated environment मिल सके जहाँ यह खुलकर काम कर सके — packages install करना, builds चलाना, tests execute करना — आपके host system को छुए बिना।

## Docker Sandbox वास्तव में क्या देता है

Core idea सरल है: एक पूर्ण Linux environment के साथ एक lightweight microVM spin up करें, अपना workspace उसमें sync करें, और Copilot agent को उसके अंदर freely काम करने दें। जब यह हो जाए, changes sync back हो जाती हैं।

यहाँ वह है जो इसे सिर्फ "container में चीज़ें चलाने" से अधिक बनाता है:

- **Bidirectional workspace sync** जो absolute paths को preserve करता है। आपकी project structure sandbox के अंदर बिल्कुल एक जैसी दिखती है। Path-related build failures नहीं।
- **Private Docker daemon** जो microVM के अंदर चलता है। Agent containers build और run कर सकता है बिना कभी आपके host के Docker socket को mount किए। Security के लिए यह बहुत बड़ी बात है।
- **HTTP/HTTPS filtering proxies** जो control करते हैं कि agent network पर क्या reach कर सकता है। आप तय करते हैं कि कौन-से registries और endpoints allowed हैं। Sandbox के अंदर एक rogue `npm install` से supply chain attacks? Blocked।
- **YOLO mode** — हाँ, यही वे इसे कहते हैं। Agent बिना permission prompts के चलता है क्योंकि यह literally आपके host को नुकसान नहीं पहुँचा सकता। हर destructive action contained है।

## .NET Developers को क्यों परवाह करनी चाहिए

उस modernization work के बारे में सोचें जिसका सामना इतनी सारी teams कर रही हैं। आपके पास 30 projects का एक .NET Framework solution है, और आपको इसे .NET 9 पर move करना है। वह सैकड़ों file changes हैं — project files, namespace updates, API replacements, NuGet migrations।

Docker Sandbox के साथ, आप एक Copilot agent को किसी project पर point कर सकते हैं, उसे microVM के अंदर freely refactor करने दे सकते हैं, validate करने के लिए `dotnet build` और `dotnet test` चला सकते हैं, और केवल वे changes accept कर सकते हैं जो वास्तव में काम करती हैं। इस जोखिम के बिना कि experimenting करते समय यह आपके local dev environment को accidentally बर्बाद कर दे।

Post में **parallel agents की एक fleet** चलाने का भी वर्णन है — प्रत्येक अपने sandbox में — जो एक साथ अलग-अलग projects से निपटती हैं। बड़े .NET solutions या microservice architectures के लिए, यह बहुत बड़ा समय बचाने वाला है। एक agent per service, सभी isolated होकर चल रहे हैं, सभी independently validate हो रहे हैं।

## Security पक्ष मायने रखता है

यहाँ वह बात है जो ज़्यादातर लोग छोड़ देते हैं: जब आप एक AI agent को arbitrary commands execute करने देते हैं, तो आप उस पर अपनी पूरी machine का भरोसा कर रहे हैं। Docker Sandbox उस model को पलट देता है। Agent को एक throwaway environment के अंदर पूरी autonomy मिलती है। Network proxy सुनिश्चित करता है कि यह केवल approved sources से pull कर सकता है। आपका host filesystem, Docker daemon, और credentials अछूते रहते हैं।

Compliance requirements वाली teams के लिए — और ज़्यादातर enterprise .NET shops की यही स्थिति है — यह "हम agentic AI उपयोग नहीं कर सकते" और "हम इसे safely adopt कर सकते हैं" के बीच का अंतर है।

## निष्कर्ष

Docker Sandbox agentic coding के मूलभूत tension को हल करता है: agents को उपयोगी होने के लिए स्वतंत्रता चाहिए, लेकिन आपकी host machine पर स्वतंत्रता खतरनाक है। MicroVMs आपको दोनों देते हैं। अगर आप कोई बड़े पैमाने का .NET refactoring या modernization plan कर रहे हैं, तो इसे अभी set up करना उचित है। Copilot की code intelligence को एक safe execution environment के साथ मिलाना ठीक वही है जिसका production teams इंतज़ार कर रही थीं।
