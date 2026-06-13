---
title: "O novo Plan agent no Visual Studio resolve um problema muito real de workflow de IA"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "O novo Plan agent do Visual Studio importa porque cria uma etapa estruturada de planejamento antes da implementação, que é exatamente o que recursos maiores e refatorações costumam precisar."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Este artigo foi traduzido automaticamente. Leia o original [aqui]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

Um dos workflows de programação com IA mais frustrantes é quando a implementação começa rápido demais.

O código pode até estar tecnicamente certo, mas está resolvendo a versão errada do problema que você tinha em mente.

Você queria uma refatoração. Virou um rewrite.
Você queria uma melhoria com escopo definido. Tocou metade do projeto.
Você queria discutir opções. Foi direto para mudanças em arquivos.

É por isso que o novo **Plan agent** no Visual Studio é uma adição tão útil.

## Isso resolve um problema real de workflow, não apenas um problema cosmético

A publicação original descreve uma situação muito familiar: "**O código não está errado... ele só não é o que você queria.**"

Essa frase é perfeita.

Porque o ponto fraco de muito desenvolvimento assistido por IA não é se o modelo consegue produzir código. O problema é se o workflow cria espaço suficiente para combinar a forma pretendida do trabalho antes de começar a implementação.

Isso importa especialmente para:

- recursos grandes
- codebases desconhecidas
- refatorações não triviais
- mudanças sensíveis à arquitetura
- trabalho que precisa de review do time antes de começar a editar

Nessas situações, pular direto para a implementação costuma ser o movimento errado.

## Planejamento não é overhead quando a tarefa é real

Acho que os times às vezes subestimam quanto tempo perdem quando começam a implementar cedo demais.

Se o agent:

- tocar nos arquivos errados
- escolher a abordagem errada
- ignorar uma restrição importante
- deixar passar um edge case necessário

então o começo "rápido" vira, no fim, um workflow mais lento no geral.

Por isso eu gosto desse recurso.

Ele cria espaço para:

- perguntas de esclarecimento
- elaboração do plano
- editar o plano diretamente
- compartilhar o plano antes de começarem as mudanças de código

Isso não é burocracia. Muitas vezes é apenas boa engenharia.

## O arquivo de plano em markdown é uma escolha inteligente

Um detalhe que eu gosto especialmente é que cada plano é salvo em `.copilot/plans/plan-{title}.md`.

Isso torna a etapa de planejamento tangível.

Quer dizer que o plano não fica preso dentro de um transcript de chat. Ele vira algo que você pode:

- revisar
- editar
- versionar mentalmente
- discutir com o time
- passar para a implementação de forma mais deliberada

Isso faz o recurso parecer muito mais sério do que um simples preâmbulo temporário antes da geração de código.

## É aqui que os workflows de IA começam a respeitar o processo do time

Acho que esse é um dos sinais mais fortes de que essas ferramentas estão amadurecendo.

Os melhores workflows de IA para desenvolvedores não são os que eliminam todas as etapas intermediárias. São os que melhoram as etapas intermediárias certas.

E planejamento é uma dessas etapas.

Se o plano é forte, implementar fica mais fácil.
Se o plano é fraco, a implementação fica barulhenta.

Esse recurso reconhece isso diretamente.

## Minha opinião

Isso não é só uma gentileza de IA.

É uma melhoria de workflow.

E, para recursos reais e refatorações reais, é exatamente o tipo de melhoria que pode economizar muito churn desnecessário, ruído de review e rework do tipo "isso não é o que eu quis dizer".

Acho que cada vez mais experiências com agents vão acabar precisando de algo assim.

O Visual Studio chegou lá antes, de um jeito que parece útil.

Publicação original: [Planeje antes de construir: apresentando o Plan agent no Visual Studio](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)