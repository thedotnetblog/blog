---
title: "Microsoft Foundry Junho de 2026: De Lançamentos de Recursos a uma Plataforma de Agentes Governada"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "As atualizações do Foundry em junho sinalizam uma transição de plataforma: distribuição, ferramentas, memória, observabilidade e otimização estão convergindo em um stack de operações de agentes pronto para empresas."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

A leva de junho de 2026 do Foundry não é apenas mais um resumo mensal. Ela marca uma transição de maturidade, de "construir agentes legais" para "operar agentes como sistemas corporativos governados". Essa distinção importa mais do que qualquer recurso isolado.

Fonte original: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Três atualizações definem a mudança. Primeiro, a publicação de agentes no Microsoft 365 Copilot e no Teams chegou ao GA, o que move a distribuição de projetos de integração customizados para uma faixa de implantação opinativa. Segundo, os Toolboxes ganharam controles mais fortes de descoberta e execução, incluindo busca de ferramentas e rotinas. Terceiro, observabilidade mais otimização se tornaram um loop fechado deliberado, não uma reflexão tardia.

Minha opinião: este é o padrão mais importante do lançamento. Tracing, avaliação, otimização e rollout controlado formam o modelo operacional mínimo viável para sistemas não determinísticos. Se você só tem uma dessas peças, você tem telemetria ou ajuste fino, não governança.

O Claude GA dentro do Foundry também é estratégico, mas não principalmente pela qualidade do modelo. O valor maior é a integração corporativa: autenticação Entra, RBAC, continuidade de cobrança e alinhamento de políticas. Equipes migrando de endpoints diretos de modelo para o Foundry deveriam enquadrar isso como consolidação operacional, não apenas troca de provedor.

Os agentes Autopilot são promissores, mas as organizações deveriam abordá-los com escolhas arquiteturais sóbrias. A colaboração em espaço compartilhado no Teams pode destravar produtividade, mas ela aumenta rapidamente a complexidade de identidade, permissão e responsabilização. Comece com escopos delimitados e checkpoints rígidos de aprovação antes de uma implantação ampla.

Recomendações práticas:

Se você já está em piloto, priorize instrumentação antes da expansão de capacidades. Conecte o tracing GenAI primeiro. Depois estabeleça suítes de avaliadores vinculadas a resultados de negócio, não métricas genéricas de modelo. Somente depois disso você deveria rodar loops de otimizador e workflows de promoção.

Para agentes pesados em toolbox, habilite a busca de ferramentas cedo para reduzir o ruído de contexto e o risco de seleção errada de ferramenta à medida que os catálogos crescem. Para agentes com memória habilitada, defina TTL e política de retenção antecipadamente. Memória sem controles de ciclo de vida se torna dívida de conformidade.

A conclusão mais opinativa que posso tirar é esta: o Foundry agora é menos sobre "qual modelo eu escolho?" e mais sobre "consigo rodar o comportamento do agente como um ciclo de vida gerenciado?" Equipes que responderem bem à segunda pergunta vão se adaptar facilmente à rotatividade de modelos. Equipes fixadas em rankings de modelo vão continuar reconstruindo stacks frágeis a cada trimestre.

O lançamento de junho deixa uma coisa clara. O Foundry está se tornando uma plataforma de operações para sistemas de IA, não apenas um kit de ferramentas de desenvolvimento. Esse é um produto mais difícil de construir, e muito mais valioso de adotar.
