---
title: "Revisar pull requests dentro do Visual Studio é exatamente o tipo de redução de atrito que eu gosto"
date: 2026-06-21
author: "Emiliano Montesdeoca"
description: "O Visual Studio agora pode revisar pull requests de ponta a ponta sem sair do IDE. Pode soar incremental, mas para equipes que passam o dia inteiro no Visual Studio, isso remove muito context switching desnecessário."
tags:
  - Visual Studio
  - Git
  - Pull Requests
  - Productivity
  - Developer Experience
---

> *Este artigo foi traduzido automaticamente. Leia o original [aqui]({{< ref "visual-studio-pull-request-review-inside-the-ide.md" >}}).* 

O navegador roubou por tempo demais uma parte grande demais do workflow de code review.

Por isso fico muito feliz em ver o Visual Studio avançando mais rumo à **revisão end-to-end de pull requests dentro do IDE**.

Este é um daqueles recursos que talvez não gere manchetes enormes, mas que pode melhorar de forma real o desenvolvimento diário.

## O valor principal é simples: menos context switching

Quando o seu loop de review vive em parte no IDE e em parte no navegador, o atrito se acumula:

- abra o PR em outro lugar
- inspecione as mudanças em uma ferramenta
- volte para a solution para investigar melhor
- troque outra vez para comentar ou aprovar

Isso não é catastrófico. É só ineficiente.

Se o Visual Studio permitir abrir, inspecionar, comentar, aprovar e fazer merge no mesmo ambiente de trabalho, isso é um ganho real de produtividade.

## A opção de "review sem checkout" é especialmente boa

Uma parte que eu particularmente gosto é a possibilidade de revisar sem fazer checkout do branch do PR.

Isso pode parecer pequeno, mas é perfeito para:

- passadas rápidas de review
- pedidos de feedback interrompidos
- manter seu branch atual e o estado local intactos

Esse é exatamente o tipo de flexibilidade que boas ferramentas de code review precisam.

## Minha opinião

Isso não é um recurso revolucionário.

É algo melhor: algo prático.

Para equipes que passam a maior parte do dia no Visual Studio, um suporte mais forte a PR review significa menos interrupções no workflow e um caminho mais suave da inspeção à ação.

Na minha visão, essa é uma melhoria que vale a pena.

Publicação original: [Revise pull requests sem sair do Visual Studio](https://devblogs.microsoft.com/visualstudio/review-pull-requests-without-leaving-visual-studio/)