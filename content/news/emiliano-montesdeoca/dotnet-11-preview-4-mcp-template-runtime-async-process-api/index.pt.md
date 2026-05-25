---
title: ".NET 11 Preview 4: Template de Servidor MCP, Bibliotecas Runtime-Async, API de Processos"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 está disponível. Os destaques: o template do servidor MCP no SDK, bibliotecas de runtime compiladas com runtime-async, dotnet watch para mobile e uma expansão significativa da API de Processos."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 está disponível. Cada versão de uma preview principal do .NET adiciona uma longa lista de itens envolvendo runtime, SDK, bibliotecas, ASP.NET Core, MAUI, C# e Entity Framework. Em vez de repetir a lista completa, aqui estão as coisas que chamaram minha atenção.

## O Template de Servidor MCP Chega ao SDK do .NET

O item mais interessante: um template de projeto de servidor MCP agora está incluído no SDK. Isso significa que `dotnet new mcp-server` (ou qualquer nome que o comando venha a ter) funciona diretamente. Para quem está construindo ferramentas MCP em .NET, isso reduz consideravelmente a fricção inicial. A integração MCP na cadeia de ferramentas da plataforma sinaliza a direção que o ecossistema está tomando.

## Bibliotecas de Runtime Compiladas com Runtime-Async

O próprio runtime agora compila suas bibliotecas padrão usando o recurso runtime-async. É uma mudança interna que afeta o desempenho — as máquinas de estado async no runtime ficam mais eficientes. A importância aqui não está em mudanças visíveis na API; é que runtime-async está maduro o suficiente para ser usado com a própria BCL, o que é um sinal significativo sobre a maturidade do recurso.

## Otimizações de JIT e Intrínsecos de Hardware

O Preview 4 continua o trabalho no JIT. Melhorias nos intrínsecos de hardware e na geração de código chegam aqui — os detalhes estão nas notas de versão do runtime. Esse tipo de mudança geralmente melhora o throughput em loops de cálculo intenso sem nenhuma mudança no seu código.

## Expansão da API de Processos

Uma atualização importante para `System.Diagnostics.Process` chega no Preview 4:

- `Process.RunAndCaptureTextAsync` — iniciar um processo, capturar stdout/stderr, aguardar a saída, tudo em uma única chamada sem risco de deadlock
- `KillOnParentExit` — acoplamento leve de ciclo de vida entre processos pai e filho
- APIs baseadas em `SafeProcessHandle` mais compatíveis com o trimmer

Se você já escreveu código repetitivo para capturar a saída de um processo sem causar deadlocks (leitura async de stdout *e* stderr simultaneamente), `RunAndCaptureTextAsync` é a API que faltava.

## dotnet watch para Android e iOS

`dotnet watch` agora suporta seleção de dispositivo para projetos .NET MAUI Android e iOS. Iteração mais rápida em mobile sem gerenciar manualmente as conexões de dispositivos no ciclo de build.

## APIs de Compressão Baseadas em Span

Novas APIs de encoder/decoder Deflate, ZLib e GZip baseadas em span chegam às bibliotecas. Menos alocações ao lidar com dados comprimidos — relevante se você está fazendo processamento de dados de alto throughput.

## Experimente

[Baixar .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — é uma preview, não pronta para produção, mas vale a pena executar nos seus projetos para detectar problemas cedo antes do ciclo de RC.

Post original: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
