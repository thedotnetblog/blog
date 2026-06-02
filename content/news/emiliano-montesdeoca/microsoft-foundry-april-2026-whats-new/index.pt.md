---
title: "Microsoft Foundry Abril 2026: Foundry Local GA, GPT-5.5, CodeAct com Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "O resumo de abril do Foundry é denso: Foundry Local atinge GA, GPT-5.5 chega, Agent Framework recebe rastreamento OpenTelemetry, CodeAct executa Python em micro-VMs Hyperlight, e o Painel de Monitoramento de Agentes está disponível."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Um mês movimentado para o Microsoft Foundry. Estes são os anúncios mais importantes.

## Foundry Local está Geralmente Disponível

Foundry Local — o runtime de IA local multiplataforma da Microsoft — passa de preview para GA no Windows, macOS (Apple Silicon) e Linux x64. Inferência de modelos locais pronta para produção com um SDK amigável para desenvolvedores. A versão 1.1 adiciona suporte a transcrição, embeddings e API Responses.

## GPT-5.5

O mais recente modelo da família GPT-5 está agora disponível no Foundry. Cota padrão para assinaturas Tier 5 e Tier 6. Se você trabalhou com variantes anteriores do GPT-5, vale a pena avaliar para seus casos de uso.

## Rastreamento do Agent Framework no Foundry

Dois recursos de rastreamento são lançados em preview este mês:

**Rastreamento do Microsoft Agent Framework** — Os agentes MAF agora podem emitir rastreamentos OpenTelemetry no Foundry. Depure o comportamento dos agentes, rastreie a execução em múltiplas etapas, exponha latência e erros nas chamadas de ferramentas. Isso preenche uma lacuna real: saber *o que seu agente realmente fez* na produção, não apenas o que retornou.

**Rastreamento de agentes hospedados** — Sessões, chamadas de ferramentas e etapas de execução de agentes hospedados também aparecem nos rastreamentos do Foundry. A mesma história de observabilidade estendida ao nível hospedado.

## CodeAct com Hyperlight (Alpha)

Esta é a adição tecnicamente mais interessante: Agent Framework agora pode executar código Python dentro de micro-máquinas virtuais [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct é o padrão onde um agente gera e executa código Python como ferramenta. A preocupação óbvia é a segurança — você está executando código gerado pelo modelo. As micro-VMs do Hyperlight fornecem isolamento em nível de processo com tempo de inicialização próximo ao nativo, tornando a execução de código em sandbox prática sem a sobrecarga de contêineres ou VMs completos.

Para fluxos de trabalho agênticos onde a execução de código é necessária, isso é uma melhoria significativa de segurança em relação à execução de código no processo host.

## Painel de Monitoramento de Agentes (Preview)

Um painel de operações unificado combinando uso de tokens, latência, taxa de sucesso de execução e pontuações de avaliadores em uma única visualização. A distinção dos painéis de observabilidade regulares: inclui resultados de avaliação junto com métricas operacionais, para que você possa correlacionar "o agente está mais lento" com "as pontuações do avaliador caíram" — ou confirmar que não estão relacionados.

## Avaliadores Personalizados de Avaliação Contínua (Preview)

Agora você pode trazer seus próprios avaliadores baseados em código ou prompt para pipelines de avaliação contínua. Anteriormente, a avaliação contínua estava limitada a avaliadores integrados. Os avaliadores personalizados permitem que você aplique critérios de qualidade específicos da equipe em seu loop de monitoramento de produção.

## Inventário de Agentes no Plano de Controle

A visualização Operate do Plano de Controle do Foundry agora mostra todos os agentes suportados em uma assinatura: agentes Foundry, Azure SRE Agent, loops de agentes do Logic Apps e agentes personalizados registrados. Uma visualização para entender o que está implantado e onde.

Postagem original: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
