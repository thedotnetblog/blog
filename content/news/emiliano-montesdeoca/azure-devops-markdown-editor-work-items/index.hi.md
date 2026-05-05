---
title: "Azure DevOps ने आखिरकार वो Markdown Editor UX ठीक किया जिसकी सबको शिकायत थी"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure DevOps में work items के Markdown editor को अब स्पष्ट preview और edit mode मिला है। यह एक छोटा बदलाव है जो एक वास्तविक परेशान करने वाली workflow समस्या को ठीक करता है।"
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-devops-markdown-editor-work-items" >}}).*

अगर आप Azure Boards इस्तेमाल करते हैं, तो शायद आपने यह अनुभव किया होगा: आप किसी work item की description पढ़ रहे हैं, शायद acceptance criteria review कर रहे हैं, और गलती से double-click हो जाती है। बस — आप edit mode में चले जाते हैं। आप कुछ edit करना नहीं चाहते थे। आप बस पढ़ रहे थे।

Dan Hellem ने [इस fix की घोषणा की](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), और यह उन बदलावों में से एक है जो सुनने में तो छोटा लगता है लेकिन वास्तव में आपकी रोज़ाना की workflow से असली परेशानी दूर करता है।

## क्या बदला

work item text fields के लिए Markdown editor अब **default रूप से preview mode में** खुलता है। आप content पढ़ और उसके साथ इंटरैक्ट कर सकते हैं — links follow कर सकते हैं, formatting review कर सकते हैं — बिना गलती से edit mode में जाने की चिंता किए।

जब आप वास्तव में edit करना चाहते हैं, तो field के ऊपर edit icon पर क्लिक करें। जब काम हो जाए, तो explicitly preview mode पर वापस आ जाएं। सरल, जानबूझकर, और अनुमानित।

बस इतना ही। यही बदलाव है।

## यह जितना लगता है उससे ज़्यादा मायने क्यों रखता है

इस पर [community feedback thread](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) काफी लंबा था। double-click-to-edit का behavior जुलाई 2025 में Markdown editor के साथ आया था, और शिकायतें लगभग तुरंत शुरू हो गईं। समस्या केवल गलत edits तक सीमित नहीं थी — पूरा interaction अप्रत्याशित लगता था। आपको कभी पता नहीं चलता था कि click करने से read होगा या edit।

जो teams Azure Boards के साथ sprint planning, backlog grooming, या code review करती हैं, उनके लिए इस तरह की micro-friction जमा होती रहती है। हर गलत edit mode entry एक context switch है। हर "रुको, क्या मैंने कुछ बदला?" वाला पल ध्यान की बर्बादी है।

नया default सबसे आम interaction pattern का सम्मान करता है: आप work items को edit करने से कहीं ज़्यादा बार पढ़ते हैं।

## Rollout की स्थिति

यह पहले से ही कुछ customers के लिए rollout हो रहा है और अगले दो से तीन हफ्तों में सभी के लिए उपलब्ध हो जाएगा। अगर आपको अभी नहीं दिख रहा, तो जल्द ही दिखेगा।

## निष्कर्ष

हर सुधार को headline feature नहीं होना चाहिए। कभी-कभी सबसे अच्छा update बस कुछ परेशान करने वाली चीज़ को हटाना होता है। यह उन्हीं में से एक है — एक छोटा UX fix जो Azure Boards को उन लोगों के लिए कम कठिन बनाता है जो बस शांति से अपने work items पढ़ना चाहते हैं।
