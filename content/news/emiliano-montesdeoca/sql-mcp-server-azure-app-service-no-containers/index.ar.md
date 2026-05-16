---
title: "خادم SQL MCP على Azure App Service — بدون حاويات"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "يمكن لخادم SQL MCP الآن العمل على Azure App Service بدون Docker أو Kubernetes. ماذا يعني ذلك لمطوري .NET الذين يبنون وكلاء ذكاء اصطناعي تتواصل مع قواعد بيانات SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
dir: rtl
---

*تمت ترجمة هذه المقالة تلقائياً. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

لأكن صريحاً: في كل مرة أرى "يتطلب حاوية" في برنامج تعليمي، يخرج مني تنهيدة صغيرة. الحاويات رائعة — حتى لا يكون لدى فريقك استراتيجية للحاويات، وفجأة تصطدم ميزة بدت بسيطة بتعقيد تنسيق غير متوقع لم يخطط له أحد.

لهذا السبب استرعى هذا انتباهي. يمكن لخادم SQL MCP الآن العمل على Azure App Service — بدون Docker، بدون Kubernetes، فقط مع نفس ملف تكوين Data API Builder (DAB) الذي يكشف قاعدة بيانات SQL الخاصة بك عبر MCP وREST وGraphQL.

## ما هو خادم SQL MCP؟

مقدمة سريعة إن لم تكن على دراية بعد. يجلس خادم SQL MCP بين وكيل الذكاء الاصطناعي وقاعدة بيانات SQL. بدلاً من منح الوكيل وصولاً مباشراً إلى قاعدة البيانات (فكرة سيئة جداً)، يكشف جداولك ومشاهداتك كطبقة تجريد — كيانات بأذونات محددة.

مبني على [Data API Builder](https://learn.microsoft.com/ar-sa/azure/data-api-builder/)، مما يعني أن ملف تكوين واحد يدير MCP *و* REST *و* GraphQL في آنٍ واحد. يتحدث وكيلك مع نقطة نهاية MCP. يتحدث تطبيقك التقليدي مع REST أو GraphQL. نفس التكوين، نفس بيئة التشغيل، واجهات مختلفة.

هذا مفيد حقاً — لا داعي للحفاظ على طبقتي API منفصلتين.

## مشكلة الحاوية (والحل)

استخدم نموذج النشر الأصلي لخادم SQL MCP الحاويات. يعمل بشكل جيد في كثير من الفرق — لكن ليس في جميعها. تعتمد كثير من فرق .NET معياراً على Azure App Service أو الأجهزة الافتراضية. إلزام بيئة تشغيل حاويات فقط لكشف نقطة نهاية SQL يضيف احتكاكاً لم يطلبه أحد.

يُظهر الإرشاد الجديد كيفية تخطي الحاوية تماماً. كل شيء يعمل بأمر `dab start`، مستضافاً على App Service كعملية ويب .NET 8 قياسية.

```bash
# تثبيت Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# تهيئة التكوين
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# إضافة كيان
dab add products --source dbo.products --permissions "authenticated:*"

# تكوين موفر مصادقة App Service
dab configure --runtime.host.authentication.provider AppService

# تشغيل الخادم
dab start
```

عند هذه النقطة لديك MCP على `/mcp`، وREST وGraphQL من نفس العملية — ولا شيء يعمل في حاوية.

## المصادقة بدون مفاتيح API مشتركة

هذا هو الجزء الذي أقدّره أكثر. عند النشر على App Service، تقوم بتكوين Microsoft Entra ID كموفر مصادقة. لا أسرار مشتركة في ملفات التكوين، ولا مفاتيح API للتدوير.

تبقى سلسلة الاتصال في متغيرات بيئة App Service (وليس في `dab-config.json`)، ونقطة نهاية MCP محمية بمصادقة المنصة. إذا كانت أحمال عمل Azure لديك متوافقة بالفعل مع Entra ID، فهذا يندمج بشكل طبيعي.

للتطوير المحلي، انتقل إلى وضع `Simulator` ونقل STDIO. عُد إلى وضع `AppService` قبل النشر. نظيف وصريح.

## النشر على App Service

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

ثم انشر مشروع DAB الخاص بك باستخدام أسلوب نشر الكود الذي يستخدمه فريقك بالفعل. التفصيل الرئيسي: هذا نشر **كود**، وليس نشر حاوية.

## لماذا يهم مطوري .NET

إذا كنت تبني وكلاء ذكاء اصطناعي في .NET، فإن وكيلك سيحتاج في نهاية المطاف إلى التواصل مع قاعدة بيانات. يمنحك خادم SQL MCP طريقة منظمة للقيام بذلك دون الكشف عن سلاسل الاتصال الخام.

راجع الإرشاد الكامل في [المقالة الأصلية](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) و[مستودع العينات على GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## الخلاصة

خادم SQL MCP على App Service خيار عملي لفرق .NET التي تريد منح وكلائها وصولاً منظماً إلى بيانات SQL بدون استراتيجية حاويات. جرّبه — سيقدّر وكلاؤك واجهة API النظيفة.
