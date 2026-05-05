---
title: "Azure MCP Server الآن .mcpb — ثبّته بدون أي Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server متاح الآن كـ MCP Bundle (.mcpb) — نزّله، اسحبه إلى Claude Desktop وانتهى الأمر. لا Node.js ولا Python ولا .NET مطلوبة."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*تمت ترجمة هذا المقال تلقائيًا. للاطلاع على النسخة الأصلية، [انقر هنا]({{< ref "index.md" >}}).*

هل تعرف ما الذي كان مزعجًا في إعداد خوادم MCP؟ كنت بحاجة إلى runtime. Node.js لنسخة npm، وPython لـ pip/uvx، و.NET SDK لمتغير dotnet.

[غيّر Azure MCP Server كل ذلك للتو](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). أصبح متاحًا الآن كـ `.mcpb` — MCP Bundle — والإعداد بالسحب والإفلات.

## ما هو MCP Bundle؟

فكّر فيه كامتداد VS Code (`.vsix`) أو امتداد متصفح (`.crx`)، ولكن لخوادم MCP. ملف `.mcpb` هو أرشيف ZIP مكتفٍ بذاته يتضمن الملف الثنائي للخادم وجميع تبعياته.

## كيفية التثبيت

**1. نزّل الحزمة لمنصتك**

انتقل إلى [صفحة GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) ونزّل ملف `.mcpb` لنظام تشغيلك ومعماريتك.

**2. ثبّت في Claude Desktop**

الطريقة الأسهل: اسحب ملف `.mcpb` وأفلته في نافذة Claude Desktop بينما تكون على صفحة إعدادات الامتدادات (`☰ → ملف → الإعدادات → الامتدادات`). راجع تفاصيل الخادم، انقر تثبيت، وأكّد.

**3. المصادقة على Azure**

```bash
az login
```

هذا كل شيء. يستخدم Azure MCP Server بيانات اعتماد Azure الموجودة لديك.

## للبدء

- **التنزيل**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **المستودع**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **التوثيق**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

اطلع على [المقال الكامل](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
