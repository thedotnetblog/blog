---
title: "Combinando versionamento de API com OpenAPI no .NET 10"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 é a primeira versão com suporte oficial para .NET 10 e Microsoft.AspNetCore.OpenApi, gerando documentos OpenAPI separados por versão de API."
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[Combinando versionamento de API com OpenAPI no .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — artigo convidado do Microsoft MVP Sander ten Brinke — apresenta o novo pacote `Asp.Versioning` v10, a primeira versão projetada especificamente para .NET 10 e a biblioteca integrada `Microsoft.AspNetCore.OpenApi` que substituiu o Swashbuckle como padrão no .NET 9.

## Asp.Versioning v10: projetado para o novo stack de OpenAPI

O `Asp.Versioning` v8.x anterior ainda funciona no .NET 10 via roll-forward implícito, mas o v10 é a primeira versão projetada especificamente para o `Microsoft.AspNetCore.OpenApi`. A configuração central é uma chamada a `AddApiVersioning` encadeada com `AddApiExplorer`, mais uma chamada separada a `AddOpenApi` para cada versão que você deseja expor:

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

Isso gera documentos separados em `/openapi/v1.json` e `/openapi/v2.json`.

## Estratégias de versionamento: caminho URL, query string, cabeçalho, media type

O pacote suporta quatro estratégias. O versionamento por caminho URL (`/api/v1/resource`) é o mais comum para APIs públicas. A query string (`?version=1.0`) e o cabeçalho personalizado (`X-API-Version`) são populares em serviços internos. O versionamento por media type via cabeçalho `Accept` é o que o GitHub usa na sua REST API.

## Compatível com Minimal APIs e Controllers

Para Minimal APIs, você cria um conjunto de versões e mapeia cada rota para uma versão específica:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Para Controllers, aplicam-se os atributos `[ApiVersion("1.0")]` e `[MapToApiVersion("1.0")]` no nível de classe e ação.

## SwaggerUI e Scalar funcionam imediatamente

Tanto `Swashbuckle.AspNetCore.SwaggerUI` quanto `Scalar.AspNetCore` se integram sem problemas — basta apontá-los para as URLs de documentos por versão e você obtém uma UI com suporte a versões sem configuração adicional.

## Os exemplos de código usam apps baseadas em arquivo do .NET 10

Os exemplos do artigo usam o novo recurso de apps baseadas em arquivo do C# 14 / .NET 10: executa-se um único arquivo `.cs` com `dotnet <nomeArquivo>.cs`, sem arquivo de projeto. Os trechos de código são autocontidos e fáceis de experimentar localmente.

## Conclusão

Se você usa .NET 10 e quer contratos OpenAPI versionados e limpos sem adicionar middleware de terceiros, `Asp.Versioning` v10 é o caminho oficial.

Leia o artigo completo: [Combinando versionamento de API com OpenAPI no .NET 10](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
