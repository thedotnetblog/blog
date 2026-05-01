---
title: "SQL Server 2025 आपकी agent-ready डेटाबेस के रूप में: सुरक्षा, बैकअप और MCP एक ही इंजन में"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Polyglot Tax सीरीज़ का अंतिम भाग production की कठिन समस्याओं पर बात करता है: relational, JSON, graph और vector डेटा पर unified Row-Level Security, साथ ही cryptographic audit trails और MCP integration जो SQL Server 2025 को सच में agent-ready बनाते हैं।"
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*यह पोस्ट स्वचालित रूप से अनुवादित है। मूल संस्करण के लिए, [यहाँ क्लिक करें](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

मैंने Aditya Badramraju की Polyglot Tax सीरीज़ को बहुत रुचि से फॉलो किया है। भाग 1-3 ने SQL Server 2025 के लिए एक बहुत मजबूत मामला बनाया था — एक ही engine में JSON, graph, vector और relational डेटा, unified query planner के साथ। भाग 4 उस कहानी को उस हिस्से तक ले जाता है जो वाकई तय करता है कि आप इस architecture पर production में भरोसा करेंगे या नहीं।

संकेत: production कहानी मजबूत है।

## सभी Data Models के लिए एक Security Model

Polyglot stacks के साथ यही समस्या है: जब auditor पूछता है, "साबित करो कि Tenant A, Tenant B का डेटा नहीं देख सकता", तो आपको यह सवाल हर database के लिए अलग-अलग जवाब देना पड़ता है। पाँच databases, पाँच security models, पाँच proofs.

SQL Server 2025 के साथ, आप एक ही Row-Level Security policy परिभाषित करते हैं और वह सभी data models पर लागू हो जाती है:

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

उस बिंदु से आगे, हर query — relational joins, JSON path queries, graph traversals, vector similarity searches — अपने आप tenant के हिसाब से filter हो जाती है। engine execution plan में predicate inject कर देता है, storage से कोई data बाहर जाने से पहले। आपके calling code को हर जगह `WHERE TenantID = @id` लिखने की जरूरत नहीं रहती। आप policy एक बार test करते हैं।

layers आगे भी compose होती हैं: उन columns के लिए Dynamic Data Masking जिन्हें कुछ roles को पूरा value नहीं दिखाना चाहिए, end-to-end encryption के लिए Always Encrypted (DBAs भी data नहीं पढ़ सकते), और stored procedures को permission boundary की तरह इस्तेमाल करना ताकि agents सिर्फ वही call करें जो आपने explicitly expose किया है।

यह architecture का वह हिस्सा है जो compliance-heavy SaaS के लिए सबसे ज्यादा मायने रखता है। एक policy, एक proof.

## Unified Backup = Atomic Recovery

एक statement, सभी data models, consistent point in time:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

Polyglot stack में, पाँच databases के लिए point-in-time recovery का मतलब पाँच restore operations को coordinate करना और उम्मीद करना होता है कि timestamps एक-दो सेकंड के भीतर मिल जाएँ। financial data के लिए वह दो सेकंड का फर्क स्वीकार्य नहीं है। एक database, एक transaction log, एक restore — recovery definition से atomic है।

## Tamper-Evident Audit Trails के लिए Ledger Tables

regulated industries के लिए, "हमारे पास logs हैं" इतना काफी नहीं है। आपको cryptographic proof चाहिए कि उन logs के साथ छेड़छाड़ नहीं हुई:

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

हर insert, update और delete को cryptographically hash करके blockchain-style structure में दर्ज किया जाता है। आप auditor को mathematically साबित कर सकते हैं कि row लिखे जाने के बाद से उसमें छेड़छाड़ नहीं हुई है। polyglot stack में, यह capability आपकी सभी databases में uniformly मौजूद नहीं होती।

## MCP Integration: बिना Hand-Coded Middleware के Agents

सीरीज़ यहीं तक जा रही थी: SQL Server 2025 सीधे SQL MCP Server support करता है, जिसका मतलब है कि आपके agents natural-language tool calls के जरिए database को call कर सकते हैं, बिना हर operation के लिए middleware लिखे।

इसे stored procedures as the permission boundary और engine-level Row-Level Security के साथ जोड़ें, और आपके पास ऐसा model है जहाँ:

1. Agent एक tool call करता है, जैसे "account 12345 के लिए customer context प्राप्त करो"
2. MCP उसे आपके defined stored procedure में translate करता है
3. SQL engine tenant isolation और column masking को automatically enforce करता है
4. Agent को सिर्फ वही data मिलता है जिसे देखने की अनुमति है

कोई middleware layer नहीं। ad-hoc query injection का risk नहीं। authorization agent नहीं, engine संभालता है।

## यह .NET Developers के लिए क्यों मायने रखता है

अगर आप .NET services बना रहे हैं और SQL Server आपका primary store है, तो इस सीरीज़ का संदेश है: आपको caching के लिए Redis, relationships के लिए graph database, या embeddings के लिए vector store जोड़ने की जरूरत नहीं है — SQL Server 2025 यह सब संभालता है, और polyglot stack से बेहतर operational consistency के साथ, plus ऐसी unified security जो सच में auditable है।

MCP integration का मतलब है कि आपके Semantic Kernel agents या Microsoft Agent Framework workflows उसी SQL MCP Server के जरिए data tier से interact कर सकते हैं, उसी security guarantees के साथ जिन्हें आप human queries पर भी लागू करेंगे।

## समापन

Polyglot Tax सीरीज़ शुरू से अंत तक पढ़ने लायक है। भाग 1-3 query planner की कहानी साबित करते हैं। भाग 4 production की कहानी साबित करता है। .NET developers के लिए जो Azure SQL पर agent-first या AI-augmented applications बना रहे हैं, यह architecture गंभीर विचार के लायक है।

Aditya Badramraju का मूल post: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).