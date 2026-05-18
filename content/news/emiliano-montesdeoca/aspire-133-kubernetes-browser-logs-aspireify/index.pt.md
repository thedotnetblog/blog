---
title: "Aspire 13.3: Suporte ao Kubernetes, Logs do Navegador e a Skill Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Cinco semanas após o 13.2, o Aspire 13.3 chega com 45 novos recursos, incluindo implantação AKS de primeira classe, uma skill de integração assistida por IA, captura de logs do navegador e resultados de comandos estruturados."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Cinco semanas não é muito tempo para um lançamento, mas o Aspire 13.3 não parece assim. Os itens principais são significativos: implantação de Kubernetes e AKS de primeira classe com Helm, uma skill de integração assistida por agente chamada Aspireify, captura de logs do navegador diretamente no dashboard e resultados de comandos estruturados. Além disso, 45 novos recursos, 134 melhorias e 93 correções de bugs.

Vamos aos destaques.

## Aspireify: Integração Assistida por Agente

Adicionar o Aspire a um projeto existente parece simples — coloque um AppHost, pronto. Na prática, envolve muita arqueologia: quais portas importam, quais variáveis de ambiente são dependências reais, quais serviços do Docker Compose devem ser mapeados para integrações do Aspire.

A nova **skill Aspireify** fornece ao seu agente de código um fluxo de trabalho guiado exatamente para isso. Quando `aspire init` cria um AppHost esqueleto, a skill Aspireify ajuda o agente a inspecionar o repositório, entender como já funciona e conectar o AppHost para se adaptar ao aplicativo — não o contrário.

A postura padrão é "minimizar alterações no seu código." Se o seu aplicativo já lê `DATABASE_URL`, o agente mapeia isso com `WithEnvironment()` em vez de pedir que você reescreva sua configuração. Se uma porta está codificada de forma fixa, a skill indica ao agente quando preservá-la.

Este é o tipo de tooling de IA que realmente economiza tempo em vez de gerar mais trabalho para revisar.

## Implantação de Kubernetes e AKS de Primeira Classe

Esta estava na lista de desejos há algum tempo. O Aspire 13.3 inclui **suporte de implantação de Kubernetes e AKS de primeira classe com Helm**. Agora você pode direcionar o AKS como destino de implantação diretamente das ferramentas do Aspire.

Para equipes que já executam cargas de trabalho de produção no AKS, isso fecha uma lacuna significativa. Seu modelo de aplicativo Aspire agora tem um caminho limpo do desenvolvimento local ao Kubernetes sem a necessidade de escrever manualmente charts Helm.

## Logs do Navegador no Dashboard

Esta é uma daquelas funcionalidades que parecem pequenas até você estar depurando um problema de frontend.

A nova API `WithBrowserLogs()` anexa um recurso de navegador rastreado a qualquer recurso capaz de endpoints. O Aspire lança o Chromium usando um pipe CDP privado e transmite logs do console, solicitações de rede e erros diretamente no fluxo de logs do recurso:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

O AppHost TypeScript suporta o mesmo:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Erros de console, solicitações de rede com falha, exceções do lado do cliente — tudo visível no mesmo dashboard onde você já está observando traces e métricas. Sem necessidade de trocar de aba para o DevTools do navegador para as coisas básicas.

## Resultados de Comandos Estruturados

Os comandos de recursos receberam uma atualização significativa. Até agora, os comandos retornavam sucesso/falha. Agora eles retornam resultados estruturados: texto, JSON ou markdown que flui pelo modelo, pela interface do dashboard, pela CLI e pelas ferramentas MCP.

O dashboard une tudo isso com um novo centro de notificações no cabeçalho. Os resultados dos comandos aparecem como notificações com carimbo de data/hora com renderização de markdown e uma ação "Ver resposta".

Isso torna os comandos de recursos verdadeiramente combináveis. Uma integração agora pode expor um comando que retorna uma saída significativa — como uma URL de túnel — em vez de simplesmente alterar o estado em algum lugar.

## Conclusão

O Aspire 13.3 vale a atualização mesmo que seja apenas pelo suporte ao Kubernetes. Os logs do navegador e os resultados de comandos estruturados parecem o tipo de melhorias de qualidade de vida que se acumulam rapidamente em um fluxo de trabalho de desenvolvimento diário.

Notas de versão completas: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
