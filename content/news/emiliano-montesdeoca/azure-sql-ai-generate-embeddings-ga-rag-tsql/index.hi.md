---
title: "Azure SQL अब एम्बेडिंग जेनरेट कर सकता है — शुद्ध T-SQL में, कोई ऐप लेयर नहीं"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS और CREATE EXTERNAL MODEL अब Azure SQL Database और Managed Instance में GA हैं। पूरी तरह से T-SQL में बनी RAG पाइपलाइन, कोई डेटा मूवमेंट आवश्यक नहीं।"
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

यदि आपने कभी RAG पाइपलाइन बनाई है, तो आप पाइपलाइन टैक्स जानते हैं: आपका डेटा SQL में रहता है, लेकिन एम्बेडिंग जेनरेट करने के लिए आपको इसे निकालना होगा, एम्बेडिंग API को कॉल करना होगा, बैचिंग और रेट लिमिट को हैंडल करना होगा, और परिणामों को कहीं वेक्टर-सर्चेबल स्टोर करना होगा। अक्सर एक बिल्कुल अलग डेटाबेस में।

Azure SQL ने दो फीचर्स के साथ उसमें से अधिकांश को हटा दिया है जो अब आम तौर पर उपलब्ध हैं: `CREATE EXTERNAL MODEL` और `AI_GENERATE_EMBEDDINGS`।

## वे क्या करते हैं

ये दो T-SQL फीचर एक एकीकृत पाइपलाइन के रूप में काम करते हैं:

**`CREATE EXTERNAL MODEL`** — एक बाहरी AI मॉडल एंडपॉइंट को एक नामित डेटाबेस ऑब्जेक्ट के रूप में पंजीकृत करता है। आप स्थान, API फॉर्मेट, मॉडल टाइप और क्रेडेंशियल एक बार सेट करते हैं। हर जगह पुनः उपयोग करें।

**`AI_GENERATE_EMBEDDINGS`** — एक स्केलर T-SQL फ़ंक्शन जो पंजीकृत मॉडल को कॉल करता है और वेक्टर मानों का JSON ऐरे लौटाता है। SELECT, INSERT, UPDATE और MERGE स्टेटमेंट में काम करता है।

साथ मिलकर वे SQL इंजन को छोड़े बिना एंड-टू-एंड एम्बेडिंग पाइपलाइन बनाते हैं।

## पूर्ण वर्कफ़्लो

```sql
-- चरण 1: एम्बेडिंग प्रदाता को एक बार पंजीकृत करें
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- चरण 2: T-SQL में इनलाइन एम्बेडिंग जेनरेट करें
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- चरण 3: वेक्टर दूरी से खोजें
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

यही पूरी पाइपलाइन है: SQL में डेटा, SQL में जेनरेट की गई एम्बेडिंग, SQL में समानता खोज। कोई ऑर्केस्ट्रेशन लेयर नहीं, कोई ETL नहीं, कोई अलग वेक्टर डेटाबेस नहीं।

## समर्थित API फॉर्मेट और विकल्प

GA में `API_FORMAT` **Azure OpenAI** और **OpenAI** को सपोर्ट करता है। `MODEL_TYPE` अभी के लिए `EMBEDDINGS` तक सीमित है। `PARAMETERS` JSON आपको मॉडल-स्तरीय डिफ़ॉल्ट सेट करने देता है जिसमें रिट्री काउंट शामिल है:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

ऑथेंटिकेशन डेटाबेस क्रेडेंशियल का उपयोग करता है, इसलिए सीक्रेट आपके एप्लिकेशन कोड के बाहर रहते हैं।

## यह .NET एप्लिकेशन के लिए क्या सक्षम करता है

मौजूदा SQL डेटा पर AI फीचर बनाने वाले .NET डेवलपर्स के लिए यह महत्वपूर्ण है। आपको इनकी जरूरत नहीं:

- एम्बेडिंग के लिए डेटा को इंटरमीडिएट स्टोर में निकालना
- एक बाहरी एम्बेडिंग पाइपलाइन प्रबंधित करना
- एक अलग वेक्टर डेटाबेस सेट करना (हालाँकि यदि आप पूर्ण-विशेषताओं वाला वेक्टर स्टोर चाहते हैं तो Azure AI Search का उपयोग कर सकते हैं)
- अपने एप्लिकेशन की डेटा एक्सेस लेयर बदलना

आप मौजूदा SQL एप्लिकेशन में धीरे-धीरे सिमेंटिक सर्च जोड़ सकते हैं, उन्हीं T-SQL टूल्स का उपयोग करके जो आपके पास पहले से हैं।

## निष्कर्ष

SQL डेटा पर RAG पैटर्न नाटकीय रूप से सरल हो गए हैं। `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` का मतलब है कि आपका मौजूदा SQL एप्लिकेशन नई इन्फ्रास्ट्रक्चर जोड़े बिना वेक्टर सर्च क्षमताएं प्राप्त कर सकता है।

दोनों फीचर आज Azure SQL Database और Azure SQL Managed Instance में GA हैं।

मूल पोस्ट: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
