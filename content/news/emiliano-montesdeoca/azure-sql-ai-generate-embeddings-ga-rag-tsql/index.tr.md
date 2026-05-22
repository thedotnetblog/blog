---
title: "Azure SQL Artık Gömme Vektörleri Üretebilir — Saf T-SQL'de, Uygulama Katmanı Gerekmez"
date: 2026-05-22
author: "Emiliano Montesdeoca"
description: "AI_GENERATE_EMBEDDINGS ve CREATE EXTERNAL MODEL artık Azure SQL Database ve Managed Instance'da GA olarak mevcut. Veri taşıma gerektirmeden tamamen T-SQL'de oluşturulmuş RAG ardışık düzenleri."
tags:
  - Azure SQL
  - AI
  - RAG
  - Vector Search
  - T-SQL
  - .NET
---

Daha önce bir RAG ardışık düzeni oluşturduysanız, ardışık düzen vergisini biliyorsunuzdur: verileriniz SQL'de yaşıyor, ancak gömme vektörleri oluşturmak için verileri ayıklamanız, gömme API'sini çağırmanız, toplu işleme ve hız sınırlarını yönetmeniz ve sonuçları vektör araması destekleyen bir yerde depolamanız gerekir. Genellikle tamamen farklı bir veritabanında.

Azure SQL, şimdi genel kullanıma sunulan iki özellik ile bunun büyük bölümünü ortadan kaldırdı: `CREATE EXTERNAL MODEL` ve `AI_GENERATE_EMBEDDINGS`.

## Ne Yaparlar

Bu iki T-SQL özelliği entegre bir ardışık düzen olarak çalışır:

**`CREATE EXTERNAL MODEL`** — harici bir AI modeli uç noktasını adlandırılmış bir veritabanı nesnesi olarak kaydeder. Konum, API formatı, model türü ve kimlik bilgilerini bir kez ayarlarsınız. Her yerde yeniden kullanın.

**`AI_GENERATE_EMBEDDINGS`** — kayıtlı modeli çağıran ve vektör değerlerinin JSON dizisini döndüren skaler bir T-SQL işlevidir. SELECT, INSERT, UPDATE ve MERGE deyimlerinde çalışır.

Birlikte, SQL motorundan çıkmadan uçtan uca bir gömme ardışık düzeni oluştururlar.

## Tam İş Akışı

```sql
-- Adım 1: Gömme sağlayıcınızı bir kez kaydedin
CREATE EXTERNAL MODEL MyEmbeddingModel
WITH (
    LOCATION = 'https://your-aoai-resource.openai.azure.com/',
    API_FORMAT = 'Azure OpenAI',
    MODEL_TYPE = EMBEDDINGS,
    MODEL = 'text-embedding-ada-002'
);

-- Adım 2: T-SQL'de satır içi gömme vektörleri oluşturun
UPDATE docs
SET embedding = AI_GENERATE_EMBEDDINGS(content USE MODEL MyEmbeddingModel)
FROM documents AS docs;

-- Adım 3: Vektör mesafesiyle arayın
SELECT TOP 10 id, content
FROM documents
ORDER BY VECTOR_DISTANCE('cosine', embedding, 
    AI_GENERATE_EMBEDDINGS(@query USE MODEL MyEmbeddingModel));
```

Ardışık düzenin tamamı budur: SQL'deki veriler, SQL'de oluşturulan gömme vektörleri, SQL'de benzerlik araması. Düzenleme katmanı yok, ETL yok, ayrı vektör veritabanı yok.

## Desteklenen API Formatları ve Seçenekler

GA'da `API_FORMAT` **Azure OpenAI** ve **OpenAI**'yi destekler. `MODEL_TYPE` şimdilik `EMBEDDINGS` olarak kilitlidir. `PARAMETERS` JSON, yeniden deneme sayısı dahil model düzeyinde varsayılanlar ayarlamanıza olanak tanır:

```sql
PARAMETERS = '{"sql_rest_options":{"retry_count":3}}'
```

Kimlik doğrulama veritabanı kimlik bilgilerini kullanır, bu nedenle sırlar uygulama kodunuzun dışında kalır.

## Bu .NET Uygulamaları İçin Ne Sağlar

Mevcut SQL verileri üzerinde AI özellikleri oluşturan .NET geliştiricileri için bu önemlidir. Şunları yapmanız gerekmez:

- Gömme işlemi için verileri ara depoya çıkarmak
- Harici bir gömme ardışık düzenini yönetmek
- Ayrı bir vektör veritabanı kurmak (tam özellikli bir vektör deposu istiyorsanız Azure AI Search kullanabilirsiniz)
- Uygulamanızın veri erişim katmanını değiştirmek

Halihazırda sahip olduğunuz aynı T-SQL araçlarını kullanarak mevcut SQL uygulamalarına artımlı olarak semantik arama ekleyebilirsiniz.

## Sonuç

SQL verileri üzerindeki RAG desenleri dramatik biçimde basitleşti. `AI_GENERATE_EMBEDDINGS` + `CREATE EXTERNAL MODEL`, mevcut SQL uygulamanızın yeni altyapı eklemeden vektör arama yetenekleri kazanabileceği anlamına gelir.

Her iki özellik de bugün Azure SQL Database ve Azure SQL Managed Instance'da GA olarak sunulmaktadır.

Orijinal gönderi: [Generate Embeddings Function and External Model Object Support Are Now Generally Available in Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-embeddings-function-and-external-model-object-support-are-now-generally-available-in-azure-sql/)
