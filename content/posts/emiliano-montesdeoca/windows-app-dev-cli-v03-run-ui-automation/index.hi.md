---
title: "Windows App Dev CLI v0.3: टर्मिनल से F5 डीबग और एजेंट्स के लिए UI ऑटोमेशन"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 में winapp run (टर्मिनल से डीबग लॉन्च), winapp ui (UI ऑटोमेशन) और एक नया NuGet पैकेज आया है जो पैकेज्ड ऐप्स के साथ dotnet run को काम करने देता है।"
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल पोस्ट के लिए [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

Visual Studio का F5 अनुभव शानदार है। लेकिन सिर्फ एक पैकेज्ड Windows ऐप को लॉन्च और डीबग करने के लिए VS खोलना — चाहे वो CI पाइपलाइन हो, ऑटोमेटेड वर्कफ्लो हो, या AI एजेंट टेस्ट चला रहा हो — बहुत ज्यादा है।

Windows App Development CLI v0.3 अभी [लॉन्च हुई है](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) और दो मुख्य फीचर्स के साथ इसका सीधा समाधान देती है: `winapp run` और `winapp ui`।

## winapp run: कहीं से भी F5

`winapp run` एक अनपैकेज्ड ऐप फोल्डर और मैनिफेस्ट लेती है, और वो सब करती है जो VS डीबग लॉन्च में करता है: एक loose पैकेज रजिस्टर करना, ऐप लॉन्च करना और री-डिप्लॉय के बीच `LocalState` बनाए रखना।

```bash
# ऐप बिल्ड करें, फिर पैकेज्ड ऐप की तरह चलाएं
winapp run ./bin/Debug
```

WinUI, WPF, WinForms, Console, Avalonia और अधिक के लिए काम करता है। मोड्स डेवलपर्स और ऑटोमेटेड वर्कफ्लो दोनों के लिए बनाए गए हैं:

- **`--detach`**: लॉन्च के तुरंत बाद टर्मिनल को कंट्रोल वापस करता है। CI के लिए आदर्श।
- **`--unregister-on-exit`**: ऐप बंद होने पर रजिस्टर्ड पैकेज हटाता है।
- **`--debug-output`**: `OutputDebugString` संदेश और exceptions रियल-टाइम में कैप्चर करता है।

## नया NuGet पैकेज: पैकेज्ड ऐप्स के लिए dotnet run

.NET डेवलपर्स के लिए एक नया NuGet पैकेज है: `Microsoft.Windows.SDK.BuildTools.WinApp`। इंस्टॉल के बाद `dotnet run` पूरा इनर लूप संभालता है: बिल्ड, loose-layout पैकेज तैयार करना, Windows में रजिस्टर करना और लॉन्च — सब एक स्टेप में।

```bash
winapp init
# या
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: कमांड लाइन से UI ऑटोमेशन

यह वो फीचर है जो एजेंटिक सीनेरियो खोलता है। `winapp ui` टर्मिनल से किसी भी चल रहे Windows ऐप (WPF, WinForms, Win32, Electron, WinUI3) तक पूर्ण UI Automation एक्सेस देता है।

क्या किया जा सकता है:

- सभी टॉप-लेवल विंडो सूचीबद्ध करें
- किसी भी विंडो के पूर्ण UI Automation ट्री को नेविगेट करें
- नाम, टाइप या ऑटोमेशन ID से एलिमेंट खोजें
- क्लिक, invoke और मान सेट करें
- स्क्रीनशॉट लें
- एलिमेंट दिखने का इंतजार करें — टेस्ट सिंक्रोनाइजेशन के लिए आदर्श

`winapp ui` और `winapp run` को मिलाकर टर्मिनल से पूरा build → लॉन्च → वेरिफाई वर्कफ्लो बनाया जा सकता है। एक एजेंट ऐप चला सकता है, UI स्थिति देख सकता है, प्रोग्रामेटिकली इंटरेक्ट कर सकता है और परिणाम validate कर सकता है।

## अन्य नई सुविधाएं

- **`winapp unregister`**: काम पूरा होने पर sideloaded पैकेज हटाएं।
- **`winapp manifest add-alias`**: टर्मिनल से नाम से ऐप लॉन्च करने के लिए alias जोड़ें।
- **Tab completion**: PowerShell के लिए एक कमांड से completion सेटअप करें।

## कैसे प्राप्त करें

```bash
winget install Microsoft.WinAppCli
# या
npm install -g @microsoft/winappcli
```

CLI पब्लिक प्रीव्यू में है। पूरी डॉक्यूमेंटेशन के लिए [GitHub रिपॉजिटरी](https://github.com/microsoft/WinAppCli) देखें और सभी विवरण के लिए [मूल घोषणा](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) देखें।
