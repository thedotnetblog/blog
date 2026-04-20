---
title: "Bookmark Studio يضيف التنقل القائم على الفتحات والمشاركة إلى إشارات Visual Studio المرجعية"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "إضافة Bookmark Studio الجديدة من Mads Kristensen تضيف تنقلاً بلوحة المفاتيح عبر الفتحات، ومدير الإشارات المرجعية، والألوان، والتسميات، وإمكانيات التصدير/المشاركة."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "bookmark-studio-visual-studio-extension" >}}).*

كانت الإشارات المرجعية في Visual Studio دائماً... مقبولة. تضع إشارة، تتنقل إلى التالية، تنسى أي منها ما هو.

Mads Kristensen [أصدر Bookmark Studio](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/) — إضافة تجريبية تملأ الثغرات التي ربما صادفتها إذا كنت تستخدم الإشارات بانتظام.

## التنقل القائم على الفتحات

الإضافة الأساسية: يمكن الآن تعيين الإشارات إلى الفتحات 1–9 والقفز إليها مباشرة بـ `Alt+Shift+1` إلى `Alt+Shift+9`. يحول هذا الإشارات من "لدي بعض الإشارات في مكان ما" إلى "الفتحة 3 هي وحدة التحكم بالـ API، الفتحة 5 هي طبقة الخدمة."

## مدير الإشارات المرجعية

نافذة أداة جديدة تعرض جميع إشاراتك في مكان واحد مع التصفية حسب الاسم والملف والموقع واللون والفتحة.

## التنظيم بالتسميات والألوان والمجلدات

يمكن للإشارات اختيارياً أن تمتلك تسميات وألواناً وتُجمَّع في مجلدات. جميع البيانات الوصفية مخزَّنة لكل حل.

## التصدير والمشاركة

يتيح Bookmark Studio تصدير الإشارات كنص عادي أو Markdown أو CSV:
- تضمين مسارات الإشارات في أوصاف pull requests
- مشاركة مسارات التحقيق مع زملاء الفريق

احصل عليه من [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio).
