---
title: "SQL MCP Server Azure App Service पर — बिना कंटेनर के"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server अब Docker या Kubernetes के बिना Azure App Service पर चल सकता है। SQL डेटाबेस से कनेक्ट होने वाले AI एजेंट बनाने वाले .NET डेवलपर्स के लिए इसका क्या मतलब है।"
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

सच बताऊं तो: जब भी किसी ट्यूटोरियल में "कंटेनर आवश्यक है" देखता हूं, मन में एक आह-सी आती है। कंटेनर बेहतरीन हैं — जब तक टीम के पास कंटेनर स्ट्रैटेजी न हो, और तब एक सरल-सी दिखने वाली फीचर अचानक अनपेक्षित ऑर्केस्ट्रेशन जटिलता में फंस जाती है।

इसीलिए यह ध्यान खींचता है। SQL MCP Server अब Azure App Service पर चल सकता है — बिना Docker के, बिना Kubernetes के, सिर्फ उसी Data API Builder (DAB) कॉन्फिग फाइल के साथ जो MCP, REST और GraphQL के जरिए आपका SQL डेटाबेस एक्सपोज़ करती है।

## SQL MCP Server क्या है?

अगर आप अभी परिचित नहीं हैं तो संक्षिप्त परिचय। SQL MCP Server आपके AI एजेंट और SQL डेटाबेस के बीच में बैठता है। एजेंट को सीधे डेटाबेस एक्सेस देने (जो बहुत बुरा विचार है) की बजाय, यह आपकी टेबल और व्यू को एक एब्स्ट्रैक्शन लेयर के रूप में एक्सपोज़ करता है — निर्धारित परमिशन के साथ एंटिटी।

[Data API Builder](https://learn.microsoft.com/hi-in/azure/data-api-builder/) पर बना है, यानी एक ही कॉन्फिग फाइल MCP *और* REST *और* GraphQL सब एक साथ मैनेज करती है। एजेंट MCP एंडपॉइंट से बात करता है। ट्रेडिशनल एप्लिकेशन REST या GraphQL से बात करती है। एक ही कॉन्फिग, एक ही रनटाइम, अलग-अलग सरफेस।

यह वाकई उपयोगी है — दो अलग API लेयर बनाए रखने की जरूरत नहीं।

## कंटेनर की समस्या (और समाधान)

SQL MCP Server का मूल डिप्लॉयमेंट मॉडल कंटेनर इस्तेमाल करता था। कई टीमों के लिए यह ठीक काम करता है — लेकिन सभी के लिए नहीं। कई .NET टीमें Azure App Service या VM पर स्टैंडर्डाइज़ हैं। सिर्फ एक SQL एंडपॉइंट एक्सपोज़ करने के लिए कंटेनर रनटाइम की जरूरत पड़ना अनचाहा घर्षण है।

नया वॉकथ्रू दिखाता है कि कंटेनर पूरी तरह स्किप कैसे करें। सब कुछ `dab start` कमांड से चलता है, App Service पर एक स्टैंडर्ड .NET 8 वेब प्रोसेस के रूप में होस्ट किया जाता है।

```bash
# Data API Builder इंस्टॉल करें
dotnet tool install microsoft.dataapibuilder --prerelease -g

# कॉन्फिग इनिशियलाइज़ करें
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# एंटिटी जोड़ें
dab add products --source dbo.products --permissions "authenticated:*"

# App Service ऑथेंटिकेशन प्रोवाइडर कॉन्फिगर करें
dab configure --runtime.host.authentication.provider AppService

# सर्वर शुरू करें
dab start
```

इस पॉइंट पर आपके पास `/mcp` पर MCP है, उसी प्रोसेस से REST और GraphQL है, और कुछ भी कंटेनर में नहीं चल रहा।

## शेयर्ड API की बिना ऑथेंटिकेशन

यह वो हिस्सा है जो मुझे सबसे ज्यादा पसंद है। App Service पर डिप्लॉय करते समय Microsoft Entra ID को ऑथेंटिकेशन प्रोवाइडर के रूप में कॉन्फिगर करते हैं। कॉन्फिग फाइलों में कोई शेयर्ड सीक्रेट नहीं, कोई API की रोटेट नहीं करनी।

कनेक्शन स्ट्रिंग App Service एनवायरनमेंट वेरिएबल में रहती है (`dab-config.json` में नहीं), और MCP एंडपॉइंट प्लेटफॉर्म ऑथेंटिकेशन से सुरक्षित है। अगर आपके Azure वर्कलोड पहले से Entra ID के साथ अलाइन हैं, तो यह स्वाभाविक रूप से फिट होता है।

लोकल डेवलपमेंट के लिए `Simulator` मोड और STDIO ट्रांसपोर्ट पर स्विच करें। डिप्लॉयमेंट से पहले `AppService` मोड पर वापस आएं। क्लीन और स्पष्ट।

## App Service पर डिप्लॉय करें

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

फिर अपनी टीम द्वारा पहले से इस्तेमाल किए जाने वाले कोड डिप्लॉयमेंट मेथड का इस्तेमाल करके DAB प्रोजेक्ट डिप्लॉय करें। मुख्य बात: यह **कोड** डिप्लॉयमेंट है, कंटेनर डिप्लॉयमेंट नहीं।

## .NET डेवलपर्स के लिए क्यों मायने रखता है

अगर आप .NET में AI एजेंट बना रहे हैं, तो जल्दी या बाद में एजेंट को डेटाबेस से बात करनी होगी। SQL MCP Server इसे करने का एक स्ट्रक्चर्ड तरीका देता है — रॉ कनेक्शन स्ट्रिंग एक्सपोज़ किए बिना।

[ओरिजिनल ब्लॉग पोस्ट](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) और [GitHub सैंपल रिपॉजिटरी](https://github.com/Azure-Samples/SQL-MCP-NoContainer) में पूरा वॉकथ्रू देखें।

## निष्कर्ष

App Service पर SQL MCP Server उन .NET टीमों के लिए एक व्यावहारिक विकल्प है जो बिना कंटेनर स्ट्रैटेजी के एजेंटों को स्ट्रक्चर्ड SQL डेटा एक्सेस देना चाहती हैं। इसे आज़माएं — आपके एजेंट क्लीन API सरफेस की सराहना करेंगे।
