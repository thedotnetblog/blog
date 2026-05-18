---
title: "WinApp VS Code एक्सटेंशन: एडिटर छोड़े बिना Windows ऐप्स चलाएं, डीबग करें और पैकेज करें"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "WinApp VS Code एक्सटेंशन पूरी Windows App Development CLI को सीधे VS Code में लाता है — Visual Studio के बिना WPF, WinUI, .NET, C++ ऐप्स को पैकेज ID के साथ चलाएं, डीबग करें, पैकेज करें और साइन करें।"
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

अगर आपने कभी VS Code में Windows ऐप बनाने की कोशिश की है, तो आप वह पल जानते हैं। आप अपने पसंदीदा एडिटर में कोड लिख रहे होते हैं — और अचानक किसी Windows API के लिए पैकेज ID की जरूरत पड़ जाती है। या MSIX बनाना पड़ता है। या पैकेज साइन करना पड़ता है। और अचानक आप Visual Studio खोल रहे होते हैं, या रात 11 बजे "msix packaging without visual studio" सर्च कर रहे होते हैं।

वह परेशानी अब खत्म हो गई है। [WinApp VS Code एक्सटेंशन](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) पब्लिक प्रीव्यू में आ गया है — और यह पूरा [Windows App Development CLI](https://github.com/microsoft/WinAppCli) सीधे VS Code में एकीकृत है। कोई अलग इंस्टॉलेशन नहीं, Visual Studio की जरूरत नहीं।

## F5 से पैकेज ID

Windows APIs के साथ समस्या है — नोटिफिकेशन, बैकग्राउंड टास्क, ऑन-डिवाइस AI फीचर, शेयर टार्गेट — इनमें से कई के लिए आपके ऐप को **पैकेज ID** की जरूरत होती है। इसके बिना, वे APIs बस काम नहीं करते।

पहले पैकेज ID पाने के लिए पूरा MSIX इंस्टॉलर बनाना पड़ता था या Visual Studio से रन करना पड़ता था। WinApp एक्सटेंशन कस्टम `winapp` डीबग टाइप से इसे पूरी तरह बदल देता है।

अपने `launch.json` में यह जोड़ें:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

F5 दबाएं। एक्सटेंशन आपका बिल्ड आउटपुट और मैनिफेस्ट ढूंढता है, `winapp run` के जरिए आपके ऐप को पैकेज ID देता है, और डीबगर अटैच करता है। .NET ऐप्स के लिए `coreclr` (C# Dev Kit जरूरी), C/C++ के लिए `cppvsdbg`, Node/Electron के लिए बिल्ट-इन डीबगर।

`preLaunchTask` सेट करके हर F5 से पहले प्रोजेक्ट अपने आप बिल्ड हो सकता है — Visual Studio जैसा ही बिल्ड-एंड-लॉन्च फ्लो, बस VS Code में।

## कमांड पैलेट में सब कुछ

`Ctrl+Shift+P` खोलें, `WinApp` टाइप करें, और पूरा टूलकिट मिलता है:

- **Initialize Project** — Windows SDK और/या Windows App SDK के साथ प्रोजेक्ट कॉन्फ़िगर करें
- **Run Application** — पैकेज ID के साथ लूज-लेआउट पैकेज्ड ऐप के रूप में लॉन्च करें
- **Create MSIX Package** — सर्टिफिकेट और रनटाइम विकल्पों के साथ ऐप पैकेज करें
- **Update Manifest Assets** — एक सोर्स इमेज से सभी जरूरी ऐप आइकन ऑटो-जेनरेट करें
- **Generate / Install Certificate** — डेवलपमेंट सर्टिफिकेट मैनेजमेंट
- **Sign Package** — MSIX या एग्जीक्यूटेबल साइन करें
- **Run SDK Tool** — `makeappx`, `signtool`, `mt`, या `makepri` सीधे चलाएं

WinApp CLI इंस्टॉल करने की भी जरूरत नहीं। यह एक्सटेंशन के साथ बंडल है।

## कई फ्रेमवर्क के साथ काम करता है

यह सिर्फ .NET WPF/WinUI टूल नहीं है। एक्सटेंशन इनके साथ काम करता है:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

यह विस्तार जानबूझकर है। VS Code वेब और क्रॉस-प्लेटफॉर्म डेवलपर्स का घर है। अगर आप Tauri या Electron ऐप बना रहे हैं जिसे Windows पैकेजिंग की जरूरत है, तो यह एक्सटेंशन Visual Studio अपनाए बिना आपको कवर करता है।

## .NET डेवलपर्स के लिए क्यों महत्वपूर्ण है

मैं VS Code में बहुत काम करता हूं — यहीं Markdown लिखता हूं, कॉन्फ़िग मैनेज करता हूं, छोटे प्रोजेक्ट एडिट करता हूं और टर्मिनल चलाता हूं। लेकिन .NET Windows डेस्कटॉप काम के लिए, जैसे ही पैकेजिंग की जरूरत पड़ती थी, Visual Studio ही एकमात्र विकल्प था।

यह एक्सटेंशन उस गैप को भरता है। अब VS Code से बाहर निकले बिना पूरा .NET Windows डेस्कटॉप डेवलपमेंट साइकल हो सकता है — एडिट, बिल्ड, पैकेज ID के साथ रन, डीबग, पैकेज, साइन। यह काम की गुणवत्ता में सच्चा सुधार है।

## शुरू करें

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

या एक्सटेंशन व्यू (`Ctrl+Shift+X`) में **WinApp** खोजें।

आवश्यकताएं:
- Windows 10 या बाद का
- VS Code 1.109.0 या बाद का
- आपके ऐप की भाषा के लिए डीबगर एक्सटेंशन

अधिक जानकारी के लिए [Chiara Mooney की पूरी घोषणा](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) पढ़ें।

## निष्कर्ष

WinApp VS Code एक्सटेंशन उन .NET Windows डेस्कटॉप डेवलपर्स के लिए एक स्वागत योग्य जोड़ है जो VS Code में रहते हैं लेकिन पैकेजिंग काम के लिए Visual Studio जाना पड़ता था। F5 से पैकेज ID, कमांड पैलेट से MSIX पैकेजिंग, बिल्ट-इन सर्टिफिकेट मैनेजमेंट — यही सही फीचर सेट है।

अपने अगले WPF या WinUI प्रोजेक्ट पर इसे आज़माएं। जो परेशानी आप झेलते रहे, वह अब काफी कम हो गई है।
