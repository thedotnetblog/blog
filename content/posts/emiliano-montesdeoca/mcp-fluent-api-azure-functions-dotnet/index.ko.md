---
title: "MCP Apps에 Fluent API 도입 — .NET에서 3단계로 풍부한 AI 도구 UI 구축"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Azure Functions의 MCP Apps용 새로운 Fluent 구성 API를 사용하면 몇 줄의 코드만으로 모든 .NET MCP 도구를 뷰, 권한, CSP 정책이 포함된 완전한 앱으로 변환할 수 있습니다."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}})에서 확인하세요.*

MCP 도구는 AI 에이전트에게 기능을 부여하는 데 훌륭합니다. 하지만 도구가 사용자에게 무언가를 보여줘야 한다면요? 대시보드, 폼, 인터랙티브 시각화 같은 것들이요. 바로 여기서 MCP Apps가 등장하며, 이제 훨씬 더 쉽게 만들 수 있게 되었습니다.

Azure SDK 팀의 Lilian Kasem이 .NET Azure Functions의 MCP Apps를 위한 [새로운 Fluent 구성 API를 발표](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)했습니다. 왜 처음부터 이렇게 간단하지 않았을까 싶은 그런 개발자 경험 개선입니다.

## MCP Apps란?

MCP Apps는 Model Context Protocol을 확장하여 도구가 자체 UI 뷰, 정적 에셋, 보안 제어를 가질 수 있게 합니다. 단순히 텍스트를 반환하는 대신 MCP 도구가 완전한 HTML 경험을 렌더링할 수 있습니다 — 인터랙티브 대시보드, 데이터 시각화, 구성 폼 — 모두 AI 에이전트가 호출 가능하고 MCP 클라이언트를 통해 사용자에게 표시됩니다.

문제는 이 모든 것을 수동으로 연결하려면 MCP 스펙을 깊이 이해해야 했다는 것입니다: `ui://` URI, 특수 MIME 타입, 도구와 리소스 간의 메타데이터 조정. 어렵지는 않지만 번거로웠습니다.

## Fluent API 3단계

**1단계: 함수를 정의합니다.** 표준 Azure Functions MCP 도구:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**2단계: MCP App으로 승격시킵니다.** 프로그램 시작 시:

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**3단계: HTML 뷰를 추가합니다.** 필요한 UI로 `assets/hello-app.html`을 생성합니다.

끝입니다. Fluent API가 MCP 프로토콜의 모든 배관 작업을 처리합니다 — 합성 리소스 함수 생성, 올바른 MIME 타입 설정, 도구와 뷰를 연결하는 메타데이터 주입.

## API 설계가 훌륭합니다

특히 마음에 드는 점 몇 가지:

**뷰 소스가 유연합니다.** 디스크의 파일에서 HTML을 제공하거나, 독립 배포를 위해 리소스를 어셈블리에 직접 포함할 수 있습니다:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP가 조합 가능합니다.** 최소 권한 원칙에 따라 앱에 필요한 출처를 명시적으로 허용합니다. `WithCsp`를 여러 번 호출하면 출처가 누적됩니다:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**가시성 제어.** 도구를 LLM에만 표시, 호스트 UI에만 표시, 또는 둘 다에 표시할 수 있습니다. UI만 렌더링하고 모델에서 호출되지 않아야 하는 도구를 원하시나요? 간단합니다:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## 시작하기

프리뷰 패키지를 추가합니다:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

이미 Azure Functions로 MCP 도구를 만들고 있다면 패키지 업데이트만 하면 됩니다. 개념이 처음이라면 [MCP Apps 빠른 시작](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp)이 가장 좋은 출발점입니다.

## 마무리

MCP Apps는 AI 도구 분야에서 가장 흥미로운 발전 중 하나입니다 — 단순히 *무언가를 하는* 것이 아니라 사용자에게 *무언가를 보여줄 수 있는* 도구. Fluent API는 프로토콜 복잡성을 제거하고 중요한 것에 집중하게 해줍니다: 도구의 로직과 UI.

완전한 API 리퍼런스와 예제는 [전체 게시물](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/)을 읽어보세요.
