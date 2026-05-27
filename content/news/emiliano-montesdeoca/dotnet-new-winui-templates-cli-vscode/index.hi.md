---
title: "dotnet new WinUI: Visual Studio के बिना Windows ऐप बनाएं"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "WinUI प्रोजेक्ट टेम्प्लेट अब dotnet new के साथ काम करते हैं — blank ऐप्स, NavigationView पैटर्न और बहुत कुछ। VS Code सपोर्ट, Visual Studio की आवश्यकता नहीं, Fluent Design डिफॉल्ट बिल्ट-इन।"
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

WinUI डेवलपमेंट के लिए पहले Visual Studio की आवश्यकता होती थी। यह बदल रहा है: Microsoft ने WinUI के लिए open-source प्रोजेक्ट और आइटम टेम्प्लेट प्रकाशित किए हैं जो `dotnet new` के साथ काम करते हैं, Windows ऐप डेवलपमेंट को मानक CLI वर्कफ़्लो में लाते हैं।

## तीन कमांड में शुरुआत

```shell
# टेम्प्लेट इंस्टॉल करें
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# NavigationView ऐप बनाएं
dotnet new winui-navview -n MyApp

# चलाएं
cd MyApp
dotnet run
```

कोई Visual Studio नहीं, कोई मैन्युअल प्रोजेक्ट सेटअप नहीं। ऐप `dotnet run` से चलती है।

## क्या शामिल है

**Blank टेम्प्लेट** (`dotnet new winui`) — पहले से वायर्ड Fluent टाइटल बार के साथ एक आधुनिक शुरुआती बिंदु, `.ico` asset के साथ अपडेटेड डिफॉल्ट ऐप आइकन, और light/dark मोड के लिए सही डिफॉल्ट। पुराने blank टेम्प्लेट से बेहतर जो आपको खुद basics कॉन्फ़िगर करने के लिए छोड़ देता था।

**NavigationView टेम्प्लेट** (`dotnet new winui-navview`) — master-detail नेविगेशन पैटर्न, NavigationView, आधुनिक टाइटल बार और multi-page नेविगेशन स्ट्रक्चर के साथ पूरी तरह वायर्ड। नेविगेशन-आधारित ऐप्स के लिए मानक Windows ऐप सिल्हूट का अनुसरण करता है। अगर आप साइड नेविगेशन वाला कुछ बना रहे हैं, तो यहाँ से शुरू करें।

दोनों टेम्प्लेट [Windows ऐप सिल्हूट](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) का पालन करते हैं — लेआउट, नेविगेशन और विजुअल स्ट्रक्चर के लिए आधुनिक Fluent Design पैटर्न — बॉक्स से बाहर।

## Visual Studio के बाहर के डेवलपर्स के लिए यह क्यों मायने रखता है

VS Code, Rider या command-line टूल्स का उपयोग करने वाले WinUI डेवलपर्स के साथ अच्छा व्यवहार नहीं किया गया। मौजूदा Visual Studio टेम्प्लेट VS के बाहर उपयोग करने योग्य नहीं थे — प्रोजेक्ट स्ट्रक्चर को मैन्युअली फिर से बनाना और basics को वायर करना पड़ता था।

ये टेम्प्लेट open source हैं ([WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407) देखें), [community feedback](https://github.com/microsoft/microsoft-ui-xaml/issues/10388) से विकसित, और अभी उपलब्ध हैं। Visual Studio सपोर्ट काम में है — ये ही टेम्प्लेट अंततः वहाँ भी काम करेंगे।

उन टीमों के लिए जो अपना WinUI प्रोजेक्ट सेटअप स्क्रिप्ट करना चाहती हैं, इसे CI में इंटीग्रेट करना चाहती हैं, या बस Visual Studio के अलावा कोई एडिटर उपयोग करना चाहती हैं, यह एक meaningful सुधार है।

ओरिजिनल पोस्ट: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
