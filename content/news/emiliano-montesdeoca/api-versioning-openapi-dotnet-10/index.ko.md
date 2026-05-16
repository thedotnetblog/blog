---
title: ".NET 10에서 API 버전 관리와 OpenAPI 결합하기"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10은 .NET 10과 Microsoft.AspNetCore.OpenApi를 모두 공식 지원하는 첫 번째 버전으로, API 버전별로 개별 OpenAPI 문서를 생성합니다."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*이 게시물은 자동으로 번역되었습니다. 원본 버전은 [여기를 클릭하세요]({{< ref "index.md" >}}).*

[.NET 10에서 API 버전 관리와 OpenAPI 결합하기](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — Microsoft MVP Sander ten Brinke의 게스트 포스트 — 는 새 패키지 `Asp.Versioning` v10을 설명합니다. 이는 .NET 10과 .NET 9에서 Swashbuckle을 기본값으로 대체한 내장 라이브러리 `Microsoft.AspNetCore.OpenApi`를 위해 특별히 설계된 첫 번째 버전입니다.

## Asp.Versioning v10: 새로운 OpenAPI 스택을 위해 설계

기존 `Asp.Versioning` v8.x는 암묵적 롤포워드를 통해 .NET 10에서 계속 작동하지만, v10은 `Microsoft.AspNetCore.OpenApi`를 위해 특별히 설계된 첫 번째 버전입니다. 핵심 설정은 `AddApiVersioning`을 `AddApiExplorer`와 체이닝하고, 노출하려는 각 버전마다 별도의 `AddOpenApi`를 호출하는 것입니다:

```csharp
builder.Services.AddApiVersioning(options => {
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
})
.AddApiExplorer(options => {
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

builder.Services.AddOpenApi("v1");
builder.Services.AddOpenApi("v2");
```

이렇게 하면 `/openapi/v1.json`과 `/openapi/v2.json`에 각각 별도의 문서가 생성됩니다.

## 버전 관리 전략: URL 경로, 쿼리 문자열, 헤더, 미디어 타입

패키지는 네 가지 전략을 지원합니다. URL 경로 버전 관리(`/api/v1/resource`)는 공개 API에서 가장 일반적입니다. 쿼리 문자열(`?version=1.0`)과 커스텀 헤더(`X-API-Version`)는 내부 서비스에서 많이 사용됩니다. `Accept` 헤더를 통한 미디어 타입 버전 관리는 GitHub이 REST API에서 사용하는 방식입니다.

## Minimal APIs와 Controller 모두 지원

Minimal APIs의 경우, 버전 세트를 만들고 각 라우트를 특정 버전에 매핑합니다:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Controller의 경우 클래스 및 액션 수준에 `[ApiVersion("1.0")]`과 `[MapToApiVersion("1.0")]` 속성을 적용합니다.

## SwaggerUI와 Scalar는 즉시 작동

`Swashbuckle.AspNetCore.SwaggerUI`와 `Scalar.AspNetCore` 모두 원활하게 통합됩니다 — 버전별 문서 URL을 가리키기만 하면 추가 설정 없이 버전 인식 UI를 얻을 수 있습니다.

## 코드 예제는 .NET 10 파일 기반 앱 사용

아티클의 예제는 C# 14 / .NET 10의 새로운 파일 기반 앱 기능을 사용합니다: 프로젝트 파일 없이 `dotnet <파일명>.cs`로 단일 `.cs` 파일을 실행합니다. 스니펫이 독립적이고 로컬에서 쉽게 시도할 수 있습니다.

## 마무리

.NET 10을 사용 중이고 서드파티 미들웨어 없이 깔끔한 버전 관리된 OpenAPI 계약을 원한다면, `Asp.Versioning` v10이 공식적인 방법입니다.

전체 게시물 읽기: [.NET 10에서 API 버전 관리와 OpenAPI 결합하기](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
