---
title: "VS Code 1.128 Faz uma Aposta Clara: A Janela de Agentes Está se Tornando a Nova Superfície de Trabalho"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 transforma fluxos de trabalho de agente de novidade em ergonomia diária com sessões multi-chat, suporte GA a visão e controles mais profundos de host/session."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 é um lançamento significativo não por causa de um recurso matador, mas porque várias mudanças se alinham em torno de uma única direção: o desenvolvimento agent-first dentro do editor está se tornando estruturado, paralelo e operacionalmente gerenciável.

Fonte original: https://code.visualstudio.com/updates/v1_128

O destaque é o comportamento multi-chat mais rico em sessões de host de agente, incluindo peer chats, forks e turnos concorrentes sob uma única sessão pai. Isso é exatamente o que desenvolvedores experientes precisam ao explorar implementações alternativas ou dividir tarefas em caminhos de verificação. Isso espelha o trabalho real de engenharia, que raramente é linear.

Minha opinião: este é o primeiro lançamento do VS Code onde a janela de agentes parece menos um painel de chat e mais uma superfície de orquestração de espaço de trabalho.

Chats rápidos sem um espaço de trabalho selecionado também importam mais do que parecem. Eles reduzem o atrito para perguntas conceituais ou arquiteturais, mantendo sessões vinculadas a projetos distintas. Essa separação pode reduzir a desordem e preservar a integridade do contexto para fluxos de trabalho de modificação de código.

O Copilot Vision atingindo o GA é outro ponto de inflexão. Uma vez que imagens e PDFs são entradas normais para chat, tarefas intensivas em documentação e UI se tornam significativamente mais fluidas. As equipes devem agora pensar em contexto multimodal como capacidade padrão, não um complemento avançado.

Há também implicações práticas de plataforma. Suporte BYOK em cenários de host de agente, parâmetros de amostragem de modelo configuráveis e padrões de modelo utilitário indicam maturidade crescente para governança de modelos empresariais. Organizações com requisitos estritos de provedor podem agora moldar o comportamento com controle mais fino em vez de padrões únicos.

Recomendações para equipes que adotam 1.128:

Defina convenções para ramificação e nomenclatura de chat em sessões multi-chat para que a exploração paralela não se torne ruído conversacional. Incentive os desenvolvedores a manter um chat para implementação e um para testes ou análise de falhas. Use chats rápidos intencionalmente para perguntas não relacionadas ao repositório.

Se você executa endpoints BYOK, estabeleça perfis básicos de temperatura/top_p por classe de carga de trabalho e documente exceções. Decida também se os fluxos utilitários devem ser executados em modelos fornecidos pelo Copilot ou BYOK para evitar lacunas silenciosas acidentais de comportamento.

Finalmente, considere atalhos de nível de SO estrategicamente. Ser capaz de acionar comandos do VS Code em todo o sistema pode melhorar o fluxo para usuários avançados, mas a proliferação não gerenciada de atalhos pode prejudicar a consistência entre equipes.

VS Code 1.128 não apenas adiciona recursos. Ele aperta a mecânica da colaboração de agentes em loops reais de desenvolvimento. Os editores que vencerem no próximo ciclo serão aqueles que tratarem as interações com agentes como primitivas de fluxo de trabalho de primeira classe, não experimentos de barra lateral. Este lançamento mostra que o VS Code entende essa corrida.