---
title: "SQL Server 2025 كقاعدة بيانات جاهزة للوكلاء: الأمان والنسخ الاحتياطي وMCP في محرك واحد"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "الجزء الأخير من سلسلة Polyglot Tax يتناول مشاكل الإنتاج الصعبة: سياسة Row-Level Security موحّدة عبر البيانات العلائقية وJSON والرسوم البيانية والمتجهات، مع مسارات تدقيق مشفّرة وتكامل MCP يجعلان SQL Server 2025 جاهزًا للوكلاء فعلاً."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
dir: rtl
---

*تمت ترجمة هذه المقالة تلقائيًا. للنسخة الأصلية، [انقر هنا](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

لقد تابعت سلسلة Polyglot Tax من Aditya Badramraju باهتمام كبير. الأجزاء 1-3 قدّمت حجة مقنعة لصالح SQL Server 2025 كقاعدة بيانات متعددة النماذج بحق — JSON والرسوم البيانية والمتجهات والبيانات العلائقية كلها في محرك واحد مع مخطط استعلام موحّد. الجزء الرابع يختم السلسلة بالجزء الذي يحدد فعلاً ما إذا كنت ستثق بهذه البنية في الإنتاج.

الخلاصة: قصة الإنتاج قوية.

## نموذج أمان واحد لكل نماذج البيانات

هذه هي المشكلة مع البنى متعددة اللغات: عندما يسألك المدقق "أثبت أن Tenant A لا يستطيع رؤية بيانات Tenant B"، عليك الإجابة عن هذا السؤال لكل قاعدة بيانات على حدة. خمس قواعد بيانات، خمس نماذج أمان، خمس براهين.

مع SQL Server 2025، يمكنك تعريف سياسة Row-Level Security واحدة تغطي كل نماذج البيانات:

```sql
CREATE FUNCTION dbo.fn_TenantFilter(@TenantID INT)
RETURNS TABLE WITH SCHEMABINDING
AS RETURN SELECT 1 AS fn_result
WHERE @TenantID = CAST(SESSION_CONTEXT(N'TenantID') AS INT);

CREATE SECURITY POLICY TenantIsolation
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Customers,     -- Relational
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Events,        -- JSON data
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Relationships, -- Graph edges
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Embeddings     -- Vector data
WITH (STATE = ON);
```

من تلك اللحظة، أي استعلام — joins علائقية، استعلامات مسارات JSON، اجتيازات الرسوم البيانية، بحث تشابه المتجهات — يُفلتر تلقائيًا حسب tenant. المحرك يحقن الشرط في خطة التنفيذ قبل أن تغادر أي بيانات التخزين. الشيفرة التي تستدعيه لا تحتاج إلى `WHERE TenantID = @id` في كل مكان. تختبر السياسة مرة واحدة.

تتراصف الطبقات كذلك: Dynamic Data Masking للأعمدة التي لا ينبغي أن ترى قيمها الكاملة بعض الأدوار، وAlways Encrypted للتشفير من طرف إلى طرف (حتى مسؤولو قواعد البيانات لا يستطيعون قراءتها)، والإجراءات المخزنة كحدّ للامتيازات بحيث لا تستدعي الوكلاء إلا ما كشفته لهم صراحة.

هذا هو الجزء من البنية الذي يهم أكثر في SaaS الخاضع للامتثال. سياسة واحدة، وبُرهان واحد.

## نسخ احتياطي موحّد = استعادة ذرّية

أمر واحد، كل نماذج البيانات، ونقطة زمنية متسقة:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

في stack متعدد اللغات، تعني استعادة نقطة زمنية عبر خمس قواعد بيانات تنسيق خمس عمليات استعادة والأمل في أن تتطابق الطوابع الزمنية في حدود ثانية أو ثانيتين. بالنسبة للبيانات المالية، هذا التفاوت غير مقبول. مع قاعدة بيانات واحدة، وسجل معاملات واحد، واستعادة واحدة — الاسترداد ذرّي بحكم التعريف.

## جداول Ledger لمسارات تدقيق لا يمكن العبث بها

في القطاعات المنظمة، أنت تحتاج إلى أكثر من "لدينا سجلات". أنت تحتاج إلى دليل مشفّر على أن تلك السجلات لم تُعدّل:

```sql
CREATE TABLE FinancialTransactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT NOT NULL,
    Amount MONEY NOT NULL,
    TransactionType NVARCHAR(20),
    TransactionDate DATETIME2 DEFAULT SYSUTCDATETIME()
)
WITH (SYSTEM_VERSIONING = ON, LEDGER = ON);
```

كل عملية insert وupdate وdelete تُhashed تشفيريًا داخل بنية شبيهة بالبلوكشين. يمكنك أن تثبت للمدقق — رياضيًا — أن صفًا لم يتم العبث به منذ كتابته. في stack متعدد اللغات، هذه القدرة لا تتوفر بشكل موحّد عبر قواعد البيانات كلها.

## تكامل MCP: وكلاء بلا middleware مكتوب يدويًا

السلسلة كانت تتجه إلى هذا: SQL Server 2025 يدعم SQL MCP Server مباشرة، وهذا يعني أن وكلاءك يمكنهم استدعاء قاعدة البيانات عبر نداءات أدوات طبيعية دون أن تكتب middleware لكل عملية.

ادمج ذلك مع الإجراءات المخزنة كحد للامتيازات وRow-Level Security المطبقة على مستوى المحرك، وستحصل على نموذج حيث:

1. يستدعي الوكيل أداة، مثل "احصل على سياق العميل للحساب 12345"
2. يترجم MCP ذلك إلى الإجراء المخزن الذي حددته
3. يفرض محرك SQL عزل tenant وإخفاء الأعمدة تلقائيًا
4. يحصل الوكيل على البيانات المسموح له برؤيتها فقط

لا توجد طبقة middleware. لا يوجد خطر حقن استعلامات عشوائية. المحرك هو من يتولى التفويض، وليس الوكيل.

## لماذا يهم هذا لمطوري .NET

إذا كنت تبني خدمات .NET وSQL Server هو مخزن البيانات الأساسي لديك، فهذه الرسالة من السلسلة هي: لست بحاجة إلى إضافة Redis للتخزين المؤقت، أو قاعدة بيانات رسومية للعلاقات، أو مخزن متجهات للتمثيلات — SQL Server 2025 يتولى كل ذلك، مع اتساق تشغيلي أفضل من stack متعدد اللغات وأمان موحّد يمكن تدقيقه فعلاً.

تكامل MCP يعني أن وكلاء Semantic Kernel أو سير عمل Microsoft Agent Framework يمكنهم التفاعل مع طبقة البيانات لديك عبر SQL MCP Server نفسه، وبنفس ضمانات الأمان التي ستفرضها على الاستعلامات البشرية.

## الختام

سلسلة Polyglot Tax تستحق القراءة من البداية إلى النهاية. الأجزاء 1-3 تثبت قصة مخطط الاستعلام. الجزء 4 يثبت قصة الإنتاج. بالنسبة لمطوري .NET الذين يبنون تطبيقات agent-first أو AI-augmented على Azure SQL، تستحق هذه البنية اعتبارًا جديًا.

المقال الأصلي بقلم Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).