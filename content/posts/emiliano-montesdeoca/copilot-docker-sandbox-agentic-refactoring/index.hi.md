---
title: "Docker Sandbox Copilot Agents को आपकी Machine को Risk किए बिना Code Refactor करने देता है"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox GitHub Copilot agents को एक secure microVM देता है refactoring के लिए — कोई permission prompts नहीं, host को कोई risk नहीं। यह बड़े-scale .NET modernization के लिए सब कुछ क्यों बदल देता है।"
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

अगर आपने Copilot के agent mode को छोटी edits से परे किसी चीज़ के लिए use किया है, तो आप pain जानते हैं। हर file write, हर terminal command — एक और permission prompt।

Azure team ने [GitHub Copilot agents के लिए Docker Sandbox](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/) के बारे में एक post drop की।

## Docker Sandbox actually आपको क्या देता है

Core idea simple है: एक lightweight microVM spin up करें full Linux environment के साथ, अपना workspace उसमें sync करें, और Copilot agent को freely operate करने दें। जब यह done हो, changes sync back होते हैं।

यह "बस stuff container में चलाएं" से ज्यादा है:
- **Bidirectional workspace sync** जो absolute paths preserve करती है
- **Private Docker daemon** microVM के अंदर running
- **HTTP/HTTPS filtering proxies** जो network access control करती हैं
- **YOLO mode** — agent बिना permission prompts के runs करता है क्योंकि यह literally आपके host को damage नहीं कर सकता

## .NET developers को क्यों care करना चाहिए

Docker Sandbox के साथ, आप एक Copilot agent को एक project पर point कर सकते हैं, उसे microVM के अंदर freely refactor करने दे सकते हैं, `dotnet build` और `dotnet test` चला सकते हैं validate करने के लिए, और only वे changes accept कर सकते हैं जो actually काम करते हैं।

Post **parallel agents की fleet** run करने का describe करती है — हर एक अपने sandbox में — अलग-अलग projects को simultaneously tackle करते हुए।

## Security angle

जब आप एक AI agent को arbitrary commands execute करने देते हैं, आप उसे अपनी पूरी machine पर trust करते हैं। Docker Sandbox इस model को flip करता है।

## Takeaway

Docker Sandbox agentic coding के fundamental tension को solve करता है: agents को useful होने के लिए freedom चाहिए, लेकिन आपके host machine पर freedom dangerous है। MicroVMs आपको दोनों देती हैं।
