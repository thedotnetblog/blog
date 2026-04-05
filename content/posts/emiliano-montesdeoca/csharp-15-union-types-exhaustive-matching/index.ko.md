---
title: "C# 15에 유니온 타입 도입 — 우리가 원하던 바로 그것"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15가 union 키워드를 도입합니다 — 컴파일러가 강제하는 판별 공용체와 완전한 패턴 매칭. 어떤 모습인지, 왜 중요한지, 그리고 오늘 바로 시도하는 방법을 알아봅니다."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *이 글은 자동 번역되었습니다. 원문을 보시려면 [여기를 클릭하세요]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}}).*

바로 이것을 기다려왔습니다. C# 15가 `union` 키워드를 도입했습니다 — 컴파일러가 강제하는 완전한 패턴 매칭을 갖춘 진정한 판별 공용체입니다. F#의 판별 공용체나 Rust의 enum을 부러워한 적이 있다면, 이것이 왜 중요한지 정확히 알 것입니다.

Bill Wagner가 .NET 블로그에 [심층 분석을 게시했는데](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/), 솔직히? 디자인이 깔끔하고, 실용적이며, 매우 C#답습니다. 실제로 무엇이 있는지, 그리고 왜 첫눈에 보이는 것보다 더 큰 의미가 있는지 보여드리겠습니다.

## 유니온이 해결하는 문제

C# 15 이전에는 메서드에서 "여러 가능한 타입 중 하나"를 반환하는 것이 항상 타협이었습니다:

- **`object`** — 제약 없음, 컴파일러 도움 없음, 어디서나 방어적 캐스팅
- **마커 인터페이스** — 더 낫지만, 누구나 구현 가능. 컴파일러는 집합이 완전하다고 판단할 수 없음
- **추상 기본 클래스** — 같은 문제, 게다가 타입들이 공통 조상이 필요함

이 중 어느 것도 실제로 원하는 것을 제공하지 못합니다: 컴파일러가 모든 케이스를 처리했음을 보장하는 닫힌 타입 집합. 유니온 타입이 바로 그것을 합니다.

## 구문은 아름다울 정도로 간결합니다

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

한 줄. `Pet`은 `Cat`, `Dog`, 또는 `Bird`를 담을 수 있습니다. 암시적 변환이 자동으로 생성됩니다:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

그리고 여기가 마법입니다 — 컴파일러가 완전한 매칭을 강제합니다:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

디스카드 `_`가 필요 없습니다. 컴파일러는 이 switch가 모든 가능한 케이스를 커버한다는 것을 알고 있습니다. 나중에 유니온에 네 번째 타입을 추가하면, 그것을 처리하지 않는 모든 switch 식이 경고를 생성합니다. 누락된 케이스가 런타임이 아니라 빌드 시점에 잡힙니다.

## 실용적으로 빛나는 곳

`Pet` 예제는 귀엽지만, 여기서부터가 유니온이 실제 코드에서 진짜로 빛나는 부분입니다.

### 다양한 형태를 반환하는 API 응답

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

이제 모든 소비자가 성공, 오류, 유효성 검증 실패를 처리하도록 강제됩니다. "에러 케이스 체크를 깜빡했다" 버그는 더 이상 없습니다.

### 단일 값 또는 컬렉션

`OneOrMore<T>` 패턴은 유니온이 헬퍼 메서드를 가진 본문을 가질 수 있음을 보여줍니다:

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

호출자는 편리한 형태를 전달합니다:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### 관련 없는 타입들의 합성

이것이 전통적 계층 구조에 대한 킬러 기능입니다. 공통점이 전혀 없는 타입들을 유니온할 수 있습니다 — `string`과 `Exception`, `int`와 `IEnumerable<T>`. 공통 조상이 필요 없습니다.

## 기존 라이브러리를 위한 커스텀 유니온

똑똑한 디자인 선택이 있습니다: 기본 패턴(케이스 타입에 대한 public 생성자와 `Value` 프로퍼티)을 따르기만 하면, `[Union]` 어트리뷰트가 있는 모든 클래스나 구조체가 유니온 타입으로 인식됩니다. 이미 유니온과 유사한 타입을 제공하는 OneOf 같은 라이브러리들이 내부를 재작성하지 않고도 컴파일러 지원에 옵트인할 수 있습니다.

값 타입을 사용하는 성능에 민감한 시나리오에서는 라이브러리가 `HasValue`와 `TryGetValue` 메서드로 박싱 없는 접근 패턴을 구현할 수 있습니다.

## 더 큰 그림

유니온 타입은 C#에 오고 있는 더 넓은 완전성 이야기의 일부입니다:

- **유니온 타입** — 닫힌 타입 집합에 대한 완전한 매칭 (지금 프리뷰에서 사용 가능)
- **닫힌 계층 구조** — `closed` 수정자가 정의 어셈블리 외부의 파생 클래스를 방지 (제안됨)
- **닫힌 enum** — 선언된 멤버 이외의 값 생성을 방지 (제안됨)

이 세 가지 기능이 합쳐지면, C#은 모든 주류 언어 중 가장 포괄적인 타입 안전 패턴 매칭 시스템 중 하나를 갖게 될 것입니다.

## 오늘 바로 시도해보세요

유니온 타입은 .NET 11 Preview 2에서 사용 가능합니다:

1. [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)를 설치
2. 프로젝트에서 `net11.0`을 타깃으로 설정
3. `<LangVersion>preview</LangVersion>`을 설정

한 가지 주의사항: Preview 2에서는 런타임에 아직 포함되어 있지 않으므로 프로젝트에서 `UnionAttribute`와 `IUnion`을 선언해야 합니다. docs 레포에서 [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs)를 가져오거나, 다음을 추가하세요:

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

## 마무리

유니온 타입은 그것 없이 어떻게 지냈는지 의아하게 만드는 기능 중 하나입니다. 컴파일러가 강제하는 완전한 매칭, 깔끔한 구문, 제네릭 지원, 기존 패턴 매칭과의 통합 — 우리가 요청해온 모든 것이 C#의 방식으로 구현되었습니다.

.NET 11 Preview 2에서 시도하고, 이것저것 부숴보고, [GitHub에서 피드백을 공유하세요](https://github.com/dotnet/csharplang/discussions/9663). 이것은 프리뷰이며, C# 팀은 적극적으로 듣고 있습니다. 여러분의 엣지 케이스와 디자인 피드백이 최종 릴리스를 형성할 것입니다.

전체 언어 참조는 [유니온 타입 문서](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union)와 [기능 사양](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions)을 확인하세요.
