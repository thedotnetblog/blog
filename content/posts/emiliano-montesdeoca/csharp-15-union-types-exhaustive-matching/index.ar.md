---
title: "C# 15 يحصل على أنواع الاتحاد — وهي بالضبط ما كنا نطلبه"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "يُقدّم C# 15 الكلمة المفتاحية union — أنواع اتحاد مُميَّزة يُطبّقها المُحوِّل مع مطابقة أنماط شاملة. إليك شكلها ولماذا تهم وكيف تجربها اليوم."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *تمت ترجمة هذا المقال تلقائياً. للنسخة الأصلية، [انقر هنا]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

هذه هي الميزة التي كنت أنتظرها. يُقدّم C# 15 الكلمة المفتاحية `union` — أنواع اتحاد مُميَّزة حقيقية مع مطابقة أنماط شاملة يُطبّقها المُحوِّل. إذا سبق لك أن حسدت F# على أنواع اتحادها المُميَّزة أو Rust على تعداداته، فأنت تعرف تمامًا لماذا يهم هذا.

نشر Bill Wagner [التعمق الكامل](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) على مدونة .NET، وصراحةً؟ التصميم نظيف وعملي ويتماشى تمامًا مع أسلوب C#. دعني أقودك عبر ما هو موجود فعليًا ولماذا هو أمر أكبر مما قد يبدو للوهلة الأولى.

## المشكلة التي تحلها أنواع الاتحاد

قبل C# 15، كانت إعادة "أحد الأنواع الممكنة المتعددة" من دالة دائمًا تنازلًا:

- **`object`** — لا قيود، لا مساعدة من المُحوِّل، تحويل دفاعي في كل مكان
- **واجهات التمييز** — أفضل، لكن يمكن لأي شخص تنفيذها. لا يمكن للمُحوِّل أبدًا اعتبار المجموعة مكتملة
- **الفئات الأساسية المجردة** — نفس المشكلة، بالإضافة إلى أن الأنواع تحتاج إلى سلف مشترك

لا شيء من هذه يمنحك ما تريده فعلًا: مجموعة مغلقة من الأنواع حيث يضمن المُحوِّل أنك تعاملت مع كل حالة. هذا ما تفعله أنواع الاتحاد.

## الصيغة بسيطة بشكل جميل

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

سطر واحد. يمكن لـ `Pet` أن يحمل `Cat` أو `Dog` أو `Bird`. تُولَّد التحويلات الضمنية تلقائيًا:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

وهنا يكمن السحر — يُطبّق المُحوِّل المطابقة الشاملة:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

لا حاجة لـ `_` للتجاهل. يعلم المُحوِّل أن هذا التعبير يغطي كل حالة ممكنة. إذا أضفت لاحقًا نوعًا رابعًا إلى الاتحاد، فكل تعبير switch لا يتعامل معه يُنتج تحذيرًا. الحالات المفقودة تُكتشف في وقت البناء لا في وقت التشغيل.

## أين يُصبح هذا عمليًا

مثال `Pet` لطيف، لكن إليك أين تتألق الاتحادات فعلًا في الكود الحقيقي.

### استجابات API التي تُعيد أشكالًا مختلفة

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

الآن كل مستهلك مُجبر على التعامل مع النجاح والخطأ وفشل التحقق. لا مزيد من أخطاء "نسيت التحقق من حالة الخطأ".

### قيمة واحدة أو مجموعة

يُظهر نمط `OneOrMore<T>` كيف يمكن لاتحادات أن تحتوي على جسم مع دوال مساعدة:

```csharp
public union OneOrMore<T>(T, IEnumerable<T>)
{
    public IEnumerable<T> AsEnumerable() => Value switch
    {
        T single => [single],
        IEnumerable<T> multiple => multiple,
        null => []
    };
}
```

المستدعون يمررون الشكل الذي يناسبهم:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### تكوين أنواع غير مترابطة

هذه هي الميزة القاتلة على التسلسلات الهرمية التقليدية. يمكنك توحيد أنواع ليس بينها أي قاسم مشترك — `string` و`Exception`، `int` و`IEnumerable<T>`. لا حاجة لسلف مشترك.

## اتحادات مخصصة للمكتبات الموجودة

إليك خيار تصميمي ذكي: أي فئة أو بنية بسمة `[Union]` تُعترف بها كنوع اتحاد، طالما تتبع النمط الأساسي (مُنشئات عامة لأنواع الحالة وخاصية `Value`). المكتبات مثل OneOf التي تُقدم بالفعل أنواعًا شبيهة بالاتحاد يمكنها الاشتراك في دعم المُحوِّل دون إعادة كتابة بنيتها الداخلية.

بالنسبة للسيناريوهات الحساسة للأداء مع أنواع القيمة، يمكن للمكتبات تنفيذ نمط وصول غير ملاكم مع دوال `HasValue` و`TryGetValue`.

## الصورة الأكبر

أنواع الاتحاد هي جزء من قصة شمولية أوسع قادمة إلى C#:

- **أنواع الاتحاد** — مطابقة شاملة على مجموعة مغلقة من الأنواع (متاحة الآن في المعاينة)
- **التسلسلات الهرمية المغلقة** — المُعدِّل `closed` يمنع الفئات المشتقة خارج التجميع المُعرِّف (مقترح)
- **التعدادات المغلقة** — تمنع إنشاء قيم بخلاف الأعضاء المُعلَّن عنهم (مقترح)

معًا، ستمنح هذه الميزات الثلاث C# أحد أنظمة مطابقة الأنماط الآمنة للنوع الأكثر شمولًا في أي لغة رئيسية.

## جرّبها اليوم

أنواع الاتحاد متاحة في .NET 11 Preview 2:

1. ثبّت [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)
2. استهدف `net11.0` في مشروعك
3. اضبط `<LangVersion>preview</LangVersion>`

تحفظ واحد: في Preview 2، ستحتاج إلى تعريف `UnionAttribute` و`IUnion` في مشروعك لأنهما ليسا في وقت التشغيل بعد. احصل على [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) من مستودع المستندات، أو أضف هذا:

```csharp
namespace System.Runtime.CompilerServices
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Struct,
        AllowMultiple = false)]
    public sealed class UnionAttribute : Attribute;

    public interface IUnion
    {
        object? Value { get; }
    }
}
```

## خلاصة

أنواع الاتحاد هي إحدى تلك الميزات التي تجعلك تتساءل كيف اجتزنا بدونها. مطابقة شاملة يُطبّقها المُحوِّل، وصيغة نظيفة، ودعم للأنماط العامة، وتكامل مع مطابقة الأنماط الموجودة — إنها كل ما كنا نطلبه، منجزًا بأسلوب C#.

جرّبها في .NET 11 Preview 2، اختبر حدودها، و[شارك ملاحظاتك على GitHub](https://github.com/dotnet/csharplang/discussions/9663). هذه نسخة معاينة، وفريق C# يستمع بنشاط. حالاتك الحدية وملاحظاتك التصميمية ستشكّل الإصدار النهائي.

للمرجع الكامل للغة، راجع [مستندات أنواع الاتحاد](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) و[مواصفات الميزة](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
