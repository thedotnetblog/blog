---
title: "Visual Studio में Extension Projects के लिए SDK-Style Support"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio extensions के लिए SDK-style project support .NET extension development के लिए एक सार्थक सरलीकरण क्यों है।"
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल संस्करण के लिए [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[SDK-Style Support for Extension Projects in Visual Studio](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) पर गौर करना ज़रूरी है अगर आप .NET सिस्टम को बड़े पैमाने पर बना या चला रहे हैं।

मेरे नज़रिए से, मुख्य फ़ीचर उतना ज़रूरी नहीं जितना यह कि एक टीम इसे कितनी जल्दी एक सुरक्षित, दोहराने योग्य इंजीनियरिंग वर्कफ़्लो में बदल सकती है।

## .NET टीमों के लिए यह क्यों मायने रखता है

अधिकांश टीमें डिलीवरी की गति, प्लेटफ़ॉर्म की एकरूपता और गवर्नेंस के बीच संतुलन बनाती हैं। यह अपडेट उपयोगी है क्योंकि यह सब कुछ नए सिरे से लिखे बिना उन बाधाओं में से किसी एक को सुधारने का अधिक ठोस रास्ता देता है।

## व्यावहारिक अगले कदम

1. प्रोडक्शन-जैसे डेटा के साथ एक छोटे .NET पायलट में फ़ीचर की पुष्टि करें।
2. व्यापक रोलआउट से पहले स्पष्ट रोलबैक और ऑब्ज़र्वेबिलिटी चेकपॉइंट जोड़ें।
3. इम्प्लीमेंटेशन पैटर्न को अपने इंटरनल टेम्पलेट में कैप्चर करें ताकि दूसरी टीमें इसका पुनः उपयोग कर सकें।

## स्रोत

- मूल लेख: [https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)
