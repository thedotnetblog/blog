---
title: "SQL MCP Server — الطريقة الصحيحة لمنح وكلاء الذكاء الاصطناعي وصولاً للقاعدة البيانات"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server من Data API builder يمنح وكلاء الذكاء الاصطناعي وصولاً آمناً وحتمياً للبيانات دون كشف المخططات أو الاعتماد على NL2SQL."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "sql-mcp-server-data-api-builder" >}}).*

لنكن صادقين: معظم خوادم MCP لقواعد البيانات المتاحة اليوم مخيفة. تأخذ استعلاماً بلغة طبيعية، تولّد SQL أثناء التشغيل، وتشغّله على بيانات إنتاجك.

قدّم فريق Azure SQL للتو [SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/)، ويتخذ نهجاً مختلفاً جوهرياً.

## لماذا لا NL2SQL؟

النماذج غير حتمية. يستخدم SQL MCP Server نهج **NL2DAB**. يعمل الوكيل مع طبقة تجريد الكيانات في Data API builder لإنتاج T-SQL دقيق بشكل حتمي.

## سبعة أدوات، لا سبعمائة

يعرض SQL MCP Server سبعة أدوات DML بالضبط:

- `describe_entities` — اكتشف الكيانات المتاحة
- `create_record` — أدرج صفوفاً
- `read_records` — استعلم الجداول والمشاهدات
- `update_record` — عدّل الصفوف
- `delete_record` — احذف الصفوف
- `execute_entity` — شغّل الإجراءات المخزنة
- `aggregate_records` — استعلامات التجميع

## البدء في ثلاثة أوامر

```bash
dab init   --database-type mssql   --connection-string "@env('sql_connection_string')"

dab add Customers   --source dbo.Customers   --permissions "anonymous:*"

dab start
```

## قصة الأمان متينة

RBAC في كل طبقة، تكامل Azure Key Vault، Microsoft Entra + OAuth مخصص.

راجع [المنشور الكامل](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) و[التوثيق](https://aka.ms/sql/mcp).
