---
title: "يمكن لـ Azure SQL الآن توليد التضمينات — في T-SQL النقي، دون حاجة لطبقة التطبيق"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS و CREATE EXTERNAL MODEL متاحان الآن بشكل عام في Azure SQL Database و Managed Instance. خطوط أنابيب RAG مبنية بالكامل في T-SQL، دون الحاجة لنقل البيانات."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

إذا سبق لك بناء خط أنابيب RAG، فأنت تعرف ضريبة خط الأنابيب: بياناتك تعيش في SQL، لكن لتوليد التضمينات تحتاج إلى استخراجها، واستدعاء واجهة برمجة تطبيقات التضمين، والتعامل مع المعالجة الدفعية وحدود المعدل، وتخزين النتائج في مكان ما يدعم البحث المتجه. غالباً في قاعدة بيانات مختلفة تماماً.

أزال Azure SQL معظم ذلك للتو بميزتين أصبحتا متاحتين بشكل عام: `CREATE EXTERNAL MODEL` و `AI_GENERATE_EMBEDDINGS`.

## ما الذي تفعلانه

تعمل هاتان الميزتان لـ T-SQL كخط أنابيب متكامل:

**`CREATE EXTERNAL MODEL`** — يسجل نقطة نهاية نموذج ذكاء اصطناعي خارجي ككائن قاعدة بيانات مسمى. تحدد الموقع وتنسيق واجهة برمجة التطبيقات ونوع النموذج وبيانات الاعتماد مرة واحدة. أعد استخدامها في أي مكان.

**`AI_GENERATE_EMBEDDINGS`** — دالة T-SQL قياسية تستدعي النموذج المسجل وتعيد مصفوفة JSON من القيم المتجهة. تعمل في عبارات SELECT وINSERT وUPDATE وMERGE.

معاً يشكلان خط أنابيب تضمين شامل دون مغادرة محرك SQL.

## سير العمل الكامل

```sql
-- الخطوة 1: سجل مزود التضمين مرة واحدة
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- الخطوة 2: توليد التضمينات مضمنة في T-SQL
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- الخطوة 3: البحث بالمسافة المتجهة
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

هذا هو خط الأنابيب بالكامل: البيانات في SQL، والتضمينات المولدة في SQL، والبحث عن التشابه في SQL. لا طبقة تنسيق، ولا ETL، ولا قاعدة بيانات متجهة منفصلة.

## تنسيقات واجهة برمجة التطبيقات والخيارات المدعومة

في الإصدار العام، يدعم `API_FORMAT` كلاً من **Azure OpenAI** و**OpenAI**. `MODEL_TYPE` محدد بـ `EMBEDDINGS` في الوقت الحالي. يتيح لك JSON `PARAMETERS` تعيين الإعدادات الافتراضية على مستوى النموذج بما في ذلك عدد المحاولات:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

تستخدم المصادقة بيانات اعتماد قاعدة البيانات، لذا تبقى الأسرار خارج كود التطبيق.

## ما الذي يتيحه هذا لتطبيقات .NET

بالنسبة لمطوري .NET الذين يبنون ميزات الذكاء الاصطناعي على بيانات SQL الموجودة، هذا أمر مهم. لا تحتاج إلى:

- استخراج البيانات إلى مخزن وسيط للتضمينات
- إدارة خط أنابيب تضمين خارجي
- إعداد قاعدة بيانات متجهة منفصلة (رغم أنه يمكنك استخدام Azure AI Search إذا أردت مخزناً متجهاً كامل الميزات)
- تغيير طبقة الوصول إلى البيانات في تطبيقك

يمكنك إضافة البحث الدلالي إلى تطبيقات SQL الموجودة بشكل تدريجي، باستخدام أدوات T-SQL نفسها التي لديك بالفعل.

## الخلاصة

أصبحت أنماط RAG على بيانات SQL أبسط بشكل كبير. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL` يعني أن تطبيق SQL الموجود لديك يمكنه اكتساب قدرات البحث المتجه دون إضافة بنية تحتية جديدة.

كلتا الميزتين متاحتان اليوم بشكل عام في Azure SQL Database و Azure SQL Managed Instance.

المنشور الأصلي: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
