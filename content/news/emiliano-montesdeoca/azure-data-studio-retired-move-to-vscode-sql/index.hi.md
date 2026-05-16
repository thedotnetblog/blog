---
title: "Azure Data Studio बंद हो गया: अपना Azure SQL वर्कफ़्लो VS Code में ले जाएं"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio 6 फरवरी 2025 को बंद हो गया, सपोर्ट 28 फरवरी 2026 को समाप्त होगा। MSSQL एक्सटेंशन के साथ VS Code में माइग्रेशन का पूरा रास्ता यहां है।"
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[Azure Data Studio 6 फरवरी 2025 को बंद हो गया](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), सपोर्ट 28 फरवरी 2026 को समाप्त होगा — अनुशंसित विकल्प MSSQL एक्सटेंशन के साथ VS Code है।

## क्या इंस्टॉल करें

शुरुआत के लिए तीन चीजें:

- **MSSQL एक्सटेंशन** — VS Code Marketplace में "SQL Server (mssql)" खोजें
- **SQL Database Projects एक्सटेंशन** — कोड के रूप में स्कीमा, बिल्ड वैलिडेशन, गाइडेड पब्लिश
- **.NET 8 SDK** — बिल्ड सिस्टम के लिए आवश्यक; SDK न मिलना पहली बार के सबसे आम समस्या है

## ADS कनेक्शन और सेटिंग्स माइग्रेट करें

MSSQL एक्सटेंशन में **ADS Migration Toolkit** शामिल है जो एक गाइडेड फ्लो में एक बार का माइग्रेशन संभालता है: सेव किए गए कनेक्शन, कनेक्शन ग्रुप, सेटिंग्स और की बाइंडिंग सभी अपने आप इंपोर्ट हो जाते हैं।

## F5 की आदत वापस पाएं

ADS यूजर क्वेरी चलाने के लिए F5 पर निर्भर रहते हैं। **MSSQL Database Management Keymap** एक्सटेंशन इंस्टॉल करें और F5 सहित ADS-स्टाइल की बाइंडिंग वापस पाएं।

## SQL Database Projects: कोड के रूप में स्कीमा

प्रोजेक्ट पर राइट-क्लिक → **Publish** → टार्गेट कॉन्फ़िगर करें → जेनरेट T-SQL स्क्रिप्ट देखें → डिप्लॉय करें। डिप्लॉयमेंट से पहले स्क्रिप्ट प्रिव्यू मुख्य सेफ्टी फीचर है। आइटम टेम्पलेट टेबल, स्टोर्ड प्रोसीजर और व्यू के लिए स्टब जेनरेट करते हैं — SSDT जैसा ही वर्कफ्लो।

सामान्य समस्या: `.sqlproj` फाइल में **टार्गेट प्लेटफॉर्म मिसमैच** बिल्ड एरर देगा अगर प्रोजेक्ट किसी अलग SQL Server वर्जन के लिए बनाया गया था।

## Schema Compare और Schema Designer

एक्सटेंशन में **Schema Compare** (प्रोजेक्ट बनाम डिप्लॉय्ड डेटाबेस का diff) और **Schema Designer** (DDL लिखे बिना विजुअल स्कीमा एडिटिंग) भी शामिल हैं।

## Microsoft Fabric डेवलपर्स

सेटअप एक जैसा है, लेकिन VS Code में खोलने से पहले **Fabric पोर्टल** से शुरू करें और डेटाबेस को Git से कनेक्ट करें। Microsoft के पास एक समर्पित गाइड है: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*।

## सारांश

माइग्रेशन एक बार का गाइडेड फ्लो है, मैन्युअल रिबिल्ड नहीं। तीन टूल इंस्टॉल करें, ADS Migration Toolkit चलाएं, की बाइंडिंग रिस्टोर करें — और 10 मिनट से कम में सामान्य काम पर वापस आ जाएं।

स्टेप-बाय-स्टेप स्क्रीनशॉट और Fabric-स्पेसिफिक वॉकथ्रू के लिए [पूरा आर्टिकल](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) देखें।
