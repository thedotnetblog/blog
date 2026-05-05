---
title: "GPT-5.5 Chegou ao Azure Foundry — O que Desenvolvedores .NET Precisam Saber"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 está disponível para todos no Microsoft Foundry. A progressão do GPT-5 ao 5.5, o que realmente melhorou e como começar a usá-lo nos seus agentes hoje."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

A Microsoft acaba de anunciar que [GPT-5.5 está geralmente disponível no Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Se você tem construído agentes no Azure, esta é a atualização que você estava esperando.

## A progressão do GPT-5

- **GPT-5**: unificou raciocínio e velocidade em um único sistema
- **GPT-5.4**: raciocínio multi-etapas mais sólido, capacidades agênticas para empresas
- **GPT-5.5**: raciocínio de contexto longo mais profundo, execução agêntica mais confiável, maior eficiência de tokens

## O que realmente mudou

**Codificação agêntica aprimorada**: GPT-5.5 mantém contexto em grandes bases de código, diagnostica falhas arquiteturais e antecipa requisitos de testes. O modelo raciocina sobre *o que mais* uma correção afeta antes de agir.

**Eficiência de tokens**: Saídas de maior qualidade com menos tokens e menos tentativas. Custo e latência diretamente menores em produção.

**Análise de contexto longo**: Lida com documentos extensos e históricos multi-sessão sem perder o fio.

## Preços

| Modelo | Entrada ($/M tokens) | Entrada em cache | Saída ($/M tokens) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5,00 | $0,50 | $30,00 |
| GPT-5.5 Pro | $30,00 | $3,00 | $180,00 |

## Por que o Foundry importa

O Foundry Agent Service permite definir agentes em YAML ou conectá-los com Microsoft Agent Framework, GitHub Copilot SDK, LangGraph ou OpenAI Agents SDK — e executá-los como agentes hospedados isolados com sistema de arquivos persistente, identidade Microsoft Entra e preços de escala a zero.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Você é um assistente útil.", name: "MeuAgente");
```

Veja o [anúncio completo](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) para todos os detalhes.
