---
title: "MCP Apps ganham uma API fluente — Construa interfaces ricas para ferramentas de IA em .NET em três passos"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "A nova API de configuração fluente para MCP Apps no Azure Functions permite transformar qualquer ferramenta MCP .NET em uma app completa com views, permissões e políticas CSP em poucas linhas de código."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}}).*

Ferramentas MCP são ótimas para dar capacidades aos agentes de IA. Mas e se a sua ferramenta precisa mostrar algo ao usuário — um dashboard, um formulário, uma visualização interativa? É aí que entram as MCP Apps, e elas ficaram muito mais fáceis de construir.

Lilian Kasem da equipe do Azure SDK [apresentou a nova API de configuração fluente](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) para MCP Apps no Azure Functions com .NET, e é o tipo de melhoria na experiência do desenvolvedor que faz a gente se perguntar por que não era sempre assim tão simples.

## O que são MCP Apps?

MCP Apps estendem o Model Context Protocol permitindo que as ferramentas carreguem suas próprias views de UI, assets estáticos e controles de segurança. Em vez de apenas retornar texto, sua ferramenta MCP pode renderizar experiências HTML completas — dashboards interativos, visualizações de dados, formulários de configuração — tudo invocável por agentes de IA e apresentado aos usuários pelos clientes MCP.

O problema era que conectar tudo isso manualmente exigia conhecer a especificação MCP a fundo: URIs `ui://`, tipos MIME especiais, coordenação de metadados entre ferramentas e recursos. Não era difícil, mas trabalhoso.

## A API fluente em três passos

**Passo 1: Defina sua função.** Uma ferramenta MCP padrão do Azure Functions:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Passo 2: Promova-a a MCP App.** No startup do seu programa:

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

**Passo 3: Adicione sua view HTML.** Crie `assets/hello-app.html` com a interface que você precisa.

É isso. A API fluente cuida de toda a encanação do protocolo MCP — gera a função de recurso sintético, define o tipo MIME correto e injeta os metadados que conectam sua ferramenta à sua view.

## A superfície da API é bem projetada

Algumas coisas que eu realmente gosto:

**As fontes de views são flexíveis.** Você pode servir HTML a partir de arquivos no disco, ou embutir recursos diretamente no seu assembly para deploys independentes:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**O CSP é componível.** Você permite explicitamente as origens que sua app precisa, seguindo princípios de menor privilégio. Chame `WithCsp` várias vezes e as origens se acumulam:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Controle de visibilidade.** Você pode tornar uma ferramenta visível apenas para o LLM, apenas para a UI do host, ou ambos. Quer uma ferramenta que só renderiza UI e não deve ser chamada pelo modelo? Fácil:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Primeiros passos

Adicione o pacote preview:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Se você já está construindo ferramentas MCP com Azure Functions, isso é apenas uma atualização de pacote. O [quickstart de MCP Apps](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) é o melhor lugar para começar se você é novo no conceito.

## Finalizando

MCP Apps são um dos desenvolvimentos mais empolgantes no espaço de ferramentas de IA — ferramentas que não apenas *fazem coisas*, mas podem *mostrar coisas* aos usuários. A API fluente remove a complexidade do protocolo e permite que você se concentre no que importa: a lógica da sua ferramenta e sua interface.

Leia o [post completo](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) para a referência completa da API e exemplos.
