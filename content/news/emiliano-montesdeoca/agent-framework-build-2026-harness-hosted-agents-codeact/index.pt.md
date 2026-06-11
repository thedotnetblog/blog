---
title: "Agent Harness, Hosted Agents e CodeAct: esta é a atualização do Agent Framework em que eu me concentraria"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "O anúncio do Agent Framework no Build 2026 está cheio de conteúdo, mas os fios mais importantes são o modelo de harness, os hosted agents no Foundry e o CodeAct para reduzir a sobrecarga de orquestração."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

O grande anúncio do Agent Framework no Build cobre bastante coisa, mas três temas se destacam de imediato para mim:

- **o harness se tornando uma parte mais central da história de runtime**
- **os hosted agents no Foundry oferecendo um caminho para produção**
- **o CodeAct reduzindo a sobrecarga de orquestração em várias etapas**

Esses são os pontos que eu manteria no radar.

## O harness está se tornando o verdadeiro centro de gravidade

O post de origem descreve o harness como a camada em que o raciocínio do modelo encontra a execução real.

Essa é a descrição certa, e também o motivo pelo qual acho que essa parte importa mais do que muitos itens individuais de funcionalidade.

No momento em que um agente precisa de:

- acesso a arquivos
- execução de shell
- modos de planejamento
- to-dos
- memória de sessão
- fluxos de aprovação

você já não está falando apenas de um prompt com um modelo.

Você está falando de comportamento em runtime.

É aí que os frameworks ou ficam realmente úteis, ou viram brinquedos.

E o Microsoft Agent Framework claramente está tentando se tornar mais útil exatamente nessa camada.

## Hosted agents são onde a história do local para a produção fica real

Eu também acho que a parte de hosted agents é uma das mais estrategicamente importantes do anúncio.

O post de origem diz explicitamente que é a forma mais fácil de dar a esse agente um lar em produção.

Essa frase importa porque a maioria dos frameworks de agentes ainda é muito mais forte em experimentação local do que em implantação operacional.

Se os hosted agents do Foundry tornarem muito mais fácil passar do desenvolvimento local para:

- escalabilidade
- observabilidade
- identidade gerenciada
- gerenciamento de sessão
- versionamento

então isso fecha uma das maiores lacunas do ecossistema de agentes atual.

Isso seria uma melhoria significativa.

## CodeAct é a ideia técnica mais empolgante da atualização

Se eu tivesse que escolher o conceito técnico mais interessante do post, provavelmente escolheria o CodeAct.

O problema que ele tenta resolver é muito real: fluxos de agentes em várias etapas ficam caros demais porque o próprio loop de orquestração consome turnos demais do modelo.

Então, quando o post de origem mostra um resultado como este:

- 52.4% mais rápido
- 63.9% menos tokens

isso chama minha atenção imediatamente.

Claro, são números de benchmark ligados a uma carga de trabalho representativa, não uma lei universal. Mas a ideia mais ampla continua muito convincente.

Se o modelo conseguir comprimir uma cadeia de chamadas de ferramenta em uma forma de execução mais eficiente, a economia dos sistemas de agentes pode mudar bastante.

## O que eu acho que os desenvolvedores deveriam realmente tirar desta atualização

A lição importante não é a quantidade de recursos lançados.

A lição é que o framework está ficando mais forte justamente nas áreas de que as aplicações reais mais precisam:

- runtime shell
- caminho de implantação
- eficiência de execução
- padrões operacionais embutidos

Esse é o tipo de sinal de maturidade que eu valorizo muito mais do que mais uma checklist superficial de recursos de IA.

## Minha visão

Esta atualização importa porque não está apenas adicionando mais superfície.

Ela está fortalecendo a história de runtime e implantação em torno dos agentes de maneiras que devem importar para aplicações reais, especialmente para equipes que querem passar de experimentos locais para sistemas que realmente possam executar e manter.

É aí que o framework fica mais convincente.

E, se eu estivesse acompanhando esse lançamento de perto, harness, hosted agents e CodeAct seriam de longe os pontos que mais chamariam minha atenção.

Post original: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
