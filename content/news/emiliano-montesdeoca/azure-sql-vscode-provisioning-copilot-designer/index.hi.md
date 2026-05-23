---
title: "VS Code के लिए MSSQL extension चुपचाप एक बहुत बड़े platform में बदल रही है"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "MSSQL extension का नवीनतम update Azure SQL provisioning, Copilot-assisted schema design, Data API builder, और notebooks जोड़ता है। सबसे दिलचस्प बात यह है कि अब database work का कितना हिस्सा VS Code के अंदर ही रह सकता है।"
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*यह लेख स्वचालित रूप से अनुवादित किया गया है। मूल संस्करण देखने के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

VS Code के लिए MSSQL extension काफी समय से बढ़ रही है, लेकिन यह नया update दिशा को बहुत स्पष्ट कर देता है।

यह अब सिर्फ़ «connect करो और कुछ queries चलाओ» नहीं है।

**Azure SQL provisioning**, **Copilot के साथ Schema Designer**, **SQL Notebooks**, और **Data API builder** को एक ही release में आगे बढ़ाने के साथ, extension database-centric development के लिए एक बहुत अधिक complete workspace बनती जा रही है।

## व्यावहारिक hook editor से सीधे provisioning है

Source post कहता है कि अब आप free tier का उपयोग करके «directly from your editor at no cost» एक fully managed cloud database बना सकते हैं।

यह उस तरह की feature है जो छोटी लगती है, जब तक कि आप न समझें कि यह setup friction कितना कम करती है।

कई developers के लिए data-heavy experimentation का annoying हिस्सा SQL खुद नहीं होता। वह environment gap होता है:

- idea
- database
- schema
- API
- testable backend

अगर यह gap एक tool के अंदर छोटा हो जाए, तो पूरा workflow अधिक आकर्षक बन जाता है।

## data work के लिए एक मजबूत inner loop ऐसा दिखता है

मुझे इस release में यह पसंद है कि यह database workflow का ज़्यादा हिस्सा एक ही जगह रखता है:

- database provision करना
- schema design करना
- changes review करना
- ORM scripts generate करना
- APIs expose करना
- endpoints test करना
- notebooks के ज़रिए document और query करना

यह SQL को stack में एक अलग side tool की तरह देखने से कहीं अधिक compelling कहानी है।

## Copilot-assisted schema workflow वह जगह है जहाँ AI value सच में महसूस होती है

Schema designer additions खास तौर पर दिलचस्प हैं क्योंकि वे एक अच्छा balance मारते हुए दिखते हैं।

Value यह नहीं है कि «AI आपका data model design करे और आप blind trust करें»।

Value यह है:

- तेज़ starting points
- visual review
- change tracking
- migration-oriented output
- स्पष्ट accept/undo controls

यह full auto-generation की तुलना में कहीं अधिक स्वस्थ AI workflow है, जिसमें inspection path ही न हो।

और database work में reviewability बहुत महत्वपूर्ण है।

## Data API builder एक quiet multiplier है

दूसरी feature जिसे मैं अनदेखा नहीं करूँगा, वह है Data API builder integration।

अगर आप schema से:

- REST
- GraphQL
- MCP endpoints

उसी environment में जा सकते हैं, तो यह backend prototypes और internal tools के लिए एक बहुत efficient path बनाता है।

यह deeper backend engineering की जगह नहीं लेता। लेकिन यह database idea से working interface तक का रास्ता जरूर छोटा करता है।

## मेरी राय

यह release MSSQL extension को VS Code के अंदर एक छोटे platform जैसा महसूस कराता है, न कि एक साधारण add-on जैसा।

APIs, data tools, admin tools, या SQL-backed prototypes बनाने वाले developers के लिए यह एक meaningful shift है।

और अगर Microsoft इस loop को और tight करता रहा, तो extension बहुत ज़्यादा strategically useful बन जाएगी जितना बहुत से लोग अभी भी मानते हैं।

मूल पोस्ट: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)