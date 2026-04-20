---
title: "C# 15 يحصل على أنواع Union — وهي بالضبط ما كنا نطلبه"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 يقدم الكلمة المفتاحية `union` — unions مميزة مفروضة من المترجم مع مطابقة أنماط شاملة. إليك كيف تبدو ولماذا تهم وكيف تجربها اليوم."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

هذا ما كنت أنتظره. C# 15 يقدم الكلمة المفتاحية `union` — unions مميزة حقيقية مع مطابقة أنماط شاملة مفروضة من المترجم.

نشر Bill Wagner [التعمق الكامل](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/).

## المشكلة التي تحلها unions

قبل C# 15، كان إرجاع "أحد أنواع محتملة متعددة" من دالة دائماً تسوية. لم تحصل أبداً على ما تريده فعلاً: مجموعة مغلقة من الأنواع حيث يضمن المترجم أنك تعاملت مع كل حالة.

## الصياغة بسيطة بشكل جميل

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

وهنا السحر — يفرض المترجم المطابقة الشاملة:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

لا حاجة لـ `_`. إذا أضفت لاحقاً نوعاً رابعاً إلى union، فكل تعبير switch لا يتعامل معه ينتج تحذيراً.

## أين يصبح عملياً

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

الآن كل مستهلك مضطر للتعامل مع النجاح والخطأ وفشل التحقق.

## جربها اليوم

أنواع union متاحة في .NET 11 Preview 2. راجع [مرجع اللغة الكامل](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union).
