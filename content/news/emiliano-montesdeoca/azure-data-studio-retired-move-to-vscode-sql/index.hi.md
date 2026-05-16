---
title: "Azure Data Studio रिटायर हो गया: अपना Azure SQL वर्कफ़्लो VS Code में लाएं"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio के रिटायरमेंट का .NET टीमों के लिए क्या अर्थ है और VS Code में Azure SQL वर्कफ़्लो के लिए व्यावहारिक माइग्रेशन पथ।"
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल संस्करण के लिए [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[Azure Data Studio Is Retired: Move Your Azure SQL Workflow to VS Code](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) पर गौर करना ज़रूरी है अगर आप .NET सिस्टम को बड़े पैमाने पर बना या चला रहे हैं।

मेरे नज़रिए से, मुख्य फ़ीचर उतना ज़रूरी नहीं जितना यह कि एक टीम इसे कितनी जल्दी एक सुरक्षित, दोहराने योग्य इंजीनियरिंग वर्कफ़्लो में बदल सकती है।

## .NET टीमों के लिए यह क्यों मायने रखता है

अधिकांश टीमें डिलीवरी की गति, प्लेटफ़ॉर्म की एकरूपता और गवर्नेंस के बीच संतुलन बनाती हैं। यह अपडेट उपयोगी है क्योंकि यह सब कुछ नए सिरे से लिखे बिना उन बाधाओं में से किसी एक को सुधारने का अधिक ठोस रास्ता देता है।

## व्यावहारिक अगले कदम

1. प्रोडक्शन-जैसे डेटा के साथ एक छोटे .NET पायलट में फ़ीचर की पुष्टि करें।
2. व्यापक रोलआउट से पहले स्पष्ट रोलबैक और ऑब्ज़र्वेबिलिटी चेकपॉइंट जोड़ें।
3. इम्प्लीमेंटेशन पैटर्न को अपने इंटरनल टेम्पलेट में कैप्चर करें ताकि दूसरी टीमें इसका पुनः उपयोग कर सकें।

## स्रोत

- मूल लेख: [https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/)
