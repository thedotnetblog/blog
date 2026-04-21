---
title: "azd + GitHub Copilot: AI-सहायता से प्रोजेक्ट सेटअप और स्मार्ट एरर समाधान"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI अब GitHub Copilot के साथ इंटीग्रेट होता है — टर्मिनल छोड़े बिना प्रोजेक्ट इंफ्रास्ट्रक्चर जनरेट करें और डिप्लॉयमेंट एरर ठीक करें।"
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल अंग्रेजी संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

क्या आप उस पल को जानते हैं जब आप Azure पर एक मौजूदा ऐप डिप्लॉय करना चाहते हैं और एक खाली `azure.yaml` देखकर सोचते हैं कि Express API के लिए Container Apps या App Service में से क्या चुनें? वह पल अब बहुत छोटा हो गया है।

Azure Developer CLI (`azd`) अब GitHub Copilot के साथ दो तरीकों से इंटीग्रेट होता है: `azd init` के दौरान AI-असिस्टेड प्रोजेक्ट स्कैफोल्डिंग, और डिप्लॉयमेंट फेल होने पर इंटेलिजेंट एरर ट्रबलशूटिंग। दोनों फीचर पूरी तरह टर्मिनल में रहते हैं।

## azd init में Copilot के साथ सेटअप

`azd init` चलाने पर अब "Set up with GitHub Copilot (Preview)" विकल्प मिलता है। इसे चुनें और Copilot आपके कोडबेस का विश्लेषण करके `azure.yaml`, इंफ्रास्ट्रक्चर टेम्प्लेट और Bicep मॉड्यूल जनरेट करता है — आपके असली कोड के आधार पर।

```
azd init
# चुनें: "Set up with GitHub Copilot (Preview)"
```

आवश्यकताएँ:

- **azd 1.23.11 या नया** — `azd version` से जाँचें या `azd update` से अपडेट करें
- **सक्रिय GitHub Copilot सब्सक्रिप्शन** (Individual, Business या Enterprise)
- **GitHub CLI (`gh`)** — जरूरत पड़ने पर `azd` लॉगिन माँगेगा

यह दोनों दिशाओं में काम करता है। नए प्रोजेक्ट के लिए? Copilot शुरू से सही Azure सर्विस कॉन्फिगर करने में मदद करता है। मौजूदा ऐप डिप्लॉय करना है? Copilot को उस पर पॉइंट करें — कोड रिस्ट्रक्चर किए बिना कॉन्फिगरेशन जनरेट हो जाएगी।

### असल में क्या होता है

मान लीजिए आपके पास PostgreSQL डिपेंडेंसी वाला Node.js Express API है। Container Apps या App Service में मैन्युअली फैसला करने और Bicep लिखने की बजाय, Copilot आपका स्टैक डिटेक्ट करके जनरेट करता है:

- सही `language`, `host` और `build` सेटिंग वाला `azure.yaml`
- Azure Container Apps के लिए Bicep मॉड्यूल
- Azure Database for PostgreSQL के लिए Bicep मॉड्यूल

और कुछ भी बदलने से पहले प्री-फ्लाइट चेक चलाता है — git वर्किंग डायरेक्टरी साफ है या नहीं, MCP सर्वर टूल कंसेंट। आपको पता होता है कि क्या बदलेगा।

## Copilot से एरर ट्रबलशूटिंग

डिप्लॉयमेंट एरर अपरिहार्य हैं। गुम पैरामीटर, परमिशन इश्यू, SKU उपलब्धता — और एरर मैसेज वह नहीं बताता जो आप जानना चाहते हैं: *कैसे ठीक करें*।

बिना Copilot: एरर कॉपी करें → डॉक्स सर्च करें → Stack Overflow के तीन अप्रासंगिक जवाब पढ़ें → `az` CLI कमांड चलाएँ → दोबारा कोशिश करें। Copilot के साथ यह लूप टूट जाता है। कोई भी `azd` कमांड फेल होने पर तुरंत चार विकल्प मिलते हैं:

- **Explain** — क्या गलत हुआ, सरल भाषा में
- **Guidance** — ठीक करने के लिए स्टेप-बाय-स्टेप निर्देश
- **Diagnose and Guide** — पूर्ण विश्लेषण + Copilot फिक्स लागू करता है (आपकी मंजूरी से) + वैकल्पिक रिट्राई
- **Skip** — खुद संभालें

मुख्य बात: Copilot के पास आपके प्रोजेक्ट, फेल कमांड और एरर डिटेल का संदर्भ पहले से है। सुझाव *आपकी स्थिति* के लिए विशिष्ट हैं।

### डिफ़ॉल्ट व्यवहार सेट करें

हमेशा एक ही विकल्प चुनते हैं? इंटरेक्टिव प्रॉम्प्ट स्किप करें:

```
azd config set copilot.errorHandling.category troubleshoot
```

मान: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`। ऑटो-फिक्स और रिट्राई भी चालू कर सकते हैं:

```
azd config set copilot.errorHandling.fix allow
```

कभी भी इंटरेक्टिव मोड पर वापस:

```
azd config unset copilot.errorHandling.category
```

## निष्कर्ष

`azd update` से नवीनतम संस्करण लें और अगले प्रोजेक्ट में `azd init` आज़माएँ।

[मूल घोषणा यहाँ पढ़ें](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/)।
