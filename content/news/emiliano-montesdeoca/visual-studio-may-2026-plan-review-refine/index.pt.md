---
title: "A atualização de maio do Visual Studio é, na verdade, sobre ter mais controle entre ideia e mudança"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "A atualização de maio do Visual Studio adiciona o Plan agent, melhorias na gestão de skills, visibilidade da janela de contexto e experiências de diff resumido multi-arquivo mais fortes. O tema comum é um melhor controle sobre o inner loop assistido por IA."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

> *Este artigo foi traduzido automaticamente. Leia o original [aqui]({{< ref "visual-studio-may-2026-plan-review-refine.md" >}}).* 

A coisa mais interessante na atualização de maio do Visual Studio não é um recurso isolado.

É a direção compartilhada.

Esse release continua melhorando o espaço entre:

- uma ideia
- um plano
- uma mudança gerada
- uma review
- um resultado refinado

Essa é a parte do desenvolvimento assistido por IA que determina se o workflow parece confiável ou caótico.

## A lista de recursos é variada, mas a intenção é consistente

No papel, esse release inclui uma mistura de coisas:

- o novo Plan agent
- melhorias na gestão de skills
- visibilidade da janela de contexto
- diff resumido multi-arquivo
- limpeza do workflow relacionado ao Copilot
- atualizações de MSVC no lado do C++

Isso pode parecer um conjunto aleatório.

Eu não acho que seja.

O fio condutor é bem claro: **o Visual Studio está tentando dar aos desenvolvedores mais controle sobre o trabalho assistido por IA sem os desacelerar.**

Esse é exatamente o trade-off certo a buscar.

## O Plan agent é o centro filosófico desse release

Mesmo que os outros recursos importem, continuo achando que o Plan agent é a parte mais reveladora desta atualização.

Ele deixa explícito algo que muitos de nós sentimos ao usar coding agents:

começar rápido nem sempre é o mesmo que avançar de forma eficaz.

O release reforça isso ao tornar planning, review e implementação controlada uma sequência mais natural.

Isso é saudável.

## O trabalho de diff multi-arquivo é silenciosamente uma grande melhoria

Também acho que o diff resumido multi-arquivo merece mais crédito do que provavelmente vai receber.

Quando agents alteram vários arquivos de uma vez, a experiência de review vira o produto.

Se revisar as mudanças parece bagunçado, os desenvolvedores confiam menos no workflow.

Se revisar as mudanças parece coerente, os desenvolvedores têm mais chance de continuar usando a ferramenta.

É por isso que uma visualização unificada de resumo importa tanto. Ela reduz o custo cognitivo de dizer sim ou não ao trabalho gerado.

## O indicador da janela de contexto é uma adição mais inteligente do que parece

Também gosto do indicador de uso de contexto.

Pode parecer um detalhe pequeno, mas ele resolve um problema muito real de workflow de IA: não saber quando a ferramenta está prestes a começar a esquecer a parte anterior da conversa.

Tornar isso visível é uma boa decisão de design.

Não expande magicamente o contexto do modelo. Mas torna o limite observável, e isso muitas vezes é a melhor alternativa seguinte.

## Minha opinião

Essa atualização é, na verdade, sobre dar aos desenvolvedores mais visibilidade e controle sobre o loop assistido por IA.

Não mais novidade.
Não mais caos.
Mais controle.

Esse é exatamente o lugar certo para investir se o objetivo for fazer as ferramentas de IA parecerem mais confiáveis dentro de um workflow sério de IDE.

Publicação original: [Atualização de maio do Visual Studio — planejar, revisar, refinar](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)