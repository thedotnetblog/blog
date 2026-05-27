---
title: "O pruning de pacotes NuGet no .NET 10 é o tipo de melhoria que se sente em todo lado"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "O novo pruning de pacotes NuGet no .NET 10 reduz relatórios de vulnerabilidades falsos positivos, simplifica o grafo de restore e melhora o desempenho do restore. É uma dessas mudanças de plataforma que tornam o trabalho diário melhor em silêncio."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Algumas melhorias de plataforma são entusiasmantes porque abrem novos cenários.

Outras são entusiasmantes porque tornam os workflows existentes menos ruidosos, menos frágeis e menos irritantes.

**O pruning de pacotes NuGet no .NET 10** pertence claramente à segunda categoria, e digo isso como elogio.

## Porque isto importa

Se alguma vez lidou com ruído de vulnerabilidades transitivas, grafos de restore desnecessariamente grandes ou pacotes que tecnicamente estão presentes mas que não são realmente relevantes para o runtime usado pela sua app, esta mudança atinge um ponto de dor real.

O pruning ajuda ao remover do grafo efetivo de dependências os pacotes fornecidos pela plataforma quando o runtime já os disponibiliza.

Isso significa:

- menos relatórios de vulnerabilidades falsos positivos
- grafos de dependências transitivas mais limpos
- menos overhead de restore
- resultados de auditoria mais acionáveis

## A minha opinião

Este é exatamente o tipo de melhoria do .NET de que gosto.

Melhora os defaults, reduz a carga mental e melhora tanto a qualidade do sinal de segurança como o comportamento diário do tooling.

Isso é uma vitória, mesmo que nunca apareça num slide de keynote.

Artigo original: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
