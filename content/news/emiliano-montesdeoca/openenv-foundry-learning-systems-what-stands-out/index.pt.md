---
title: "OpenEnv e Foundry empurram a conversa além dos agentes estáticos"
date: 2026-06-18
author: "Emiliano Montesdeoca"
description: "A nova história de OpenEnv e Foundry vai muito além dos chavões de reinforcement learning. Na verdade, ela aponta para sistemas de agentes que podem ser avaliados, otimizados e melhorados ao longo do tempo com base em resultados reais de negócio."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Reinforcement Learning
  - Azure
---

> *Este artigo foi traduzido automaticamente. Leia o original [aqui]({{< ref "openenv-foundry-learning-systems-what-stands-out.md" >}}).* 

A maioria das conversas sobre agentes ainda para na inferência.

O modelo consegue responder ao prompt? Consegue chamar a ferramenta? Consegue concluir a tarefa uma vez?

A nova discussão **OpenEnv + Foundry** é interessante porque tenta levar a conversa para um lugar mais ambicioso: **como construir um sistema de agentes que realmente melhora com o tempo?**

Essa é uma pergunta muito melhor.

## A mudança central é sair das respostas e entrar nos loops de aprendizado

O post da Foundry enquadra o problema em torno de ambientes, evals, rubrics, otimização e post-training.

Dá para resumir tudo isso em uma frase:

**o objetivo já não é apenas executar um agente, mas ter um loop que meça e melhore o agente em relação aos seus resultados reais.**

É nisso que eu acho que os desenvolvedores devem prestar atenção.

Porque, quando você enxerga assim, o ativo duradouro não é só o modelo ou o prompt. É o sistema ao redor:

- o ambiente em que ele atua
- a rubric que o avalia
- os traces que explicam o que aconteceu
- o optimizer que melhora a configuração

Essa é uma forma de pensar muito mais pronta para a empresa.

## Por que isso importa mesmo se você não faz pesquisa em RL

Sejamos honestos: termos como OpenEnv, post-training e world-modeling podem fazer muitos desenvolvedores desligarem na hora.

Mas o takeaway prático é mais simples do que a terminologia.

Mesmo que você nunca toque diretamente um loop de treinamento, esse trabalho molda a história da plataforma para o desenvolvimento futuro de agentes:

- avaliações passam a ser first-class
- otimização deixa de ser ocasional e vira contínua
- ambientes se tornam ativos reutilizáveis
- um comportamento melhor do agente vira algo mensurável, não apenas "parece melhor nas demos"

Isso é um grande avanço.

## Minha opinião

O mais inteligente neste anúncio não é um detalhe específico de pesquisa.

É o framing.

A Microsoft está claramente tentando mover o ecossistema da engenharia de prompts estáticos para **sistemas de agentes orientados a resultados**. Sistemas que podem ser avaliados, ajustados, governados e melhorados gradualmente.

É aí que está o valor sério da plataforma.

E se você está construindo agentes hoje, mesmo na camada de aplicação, vale acompanhar para onde isso está indo.

Publicação original: [Sistemas de aprendizado orientados a resultados: RL empresarial com OpenEnv e Foundry](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)