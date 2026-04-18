---
title: "O RFT do Foundry ficou mais barato e inteligente — Veja o que mudou"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "A Microsoft Foundry lançou três atualizações de RFT este mês: treinamento global para o4-mini, novos avaliadores de modelo GPT-4.1 e um guia de boas práticas que vai te poupar horas de debugging."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Se você está desenvolvendo aplicações .NET que dependem de modelos fine-tunados, as atualizações do Foundry deste mês merecem sua atenção. O Reinforcement Fine-Tuning ficou mais acessível e significativamente mais barato.

Os detalhes completos estão no [anúncio oficial](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), mas aqui vai o resumo prático.

## Treinamento Global para o4-mini

o4-mini é o modelo preferido para cargas de trabalho pesadas em raciocínio e agentes. A grande novidade: agora você pode iniciar jobs de fine-tuning a partir de mais de 13 regiões Azure com taxas de treinamento por token mais baixas em comparação com o treinamento Standard. Mesma infraestrutura, mesma qualidade, maior alcance.

Se sua equipe está distribuída geograficamente, isso importa. Você não está mais preso a um punhado de regiões para treinar.

Aqui está a chamada da API REST para iniciar um job de treinamento global:

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

Essa flag `trainingType: globalstandard` é a diferença chave.

## Novos Avaliadores de Modelo: Família GPT-4.1

Avaliadores definem o sinal de recompensa contra o qual seu modelo otimiza. Até agora, avaliadores baseados em modelo eram limitados a um conjunto menor de modelos. Agora você tem três novas opções: GPT-4.1, GPT-4.1-mini e GPT-4.1-nano.

Quando você deve usar avaliadores de modelo em vez de determinísticos? Quando a saída da sua tarefa é aberta, quando você precisa de pontuação parcial em múltiplas dimensões, ou quando está construindo workflows com agentes onde a correção das chamadas de ferramentas depende do contexto semântico.

A questão é que a estratégia de níveis é prática:

- **GPT-4.1-nano** para iterações iniciais. Baixo custo, ciclos de feedback rápidos.
- **GPT-4.1-mini** quando sua rubrica de avaliação estiver estável e você precisar de maior fidelidade.
- **GPT-4.1** para avaliação em produção ou rubricas complexas onde cada decisão de pontuação conta.

Você pode até misturar tipos de avaliadores em um único job de RFT. Use string-match para a dimensão de "resposta correta" e um avaliador de modelo para avaliar a qualidade do raciocínio. Essa flexibilidade é honestamente o que torna isso útil para cargas de trabalho reais.

## A Pegadinha do Formato de Dados do RFT

Isso confunde muita gente. O formato de dados do RFT é diferente do SFT. A última mensagem em cada linha deve ter o papel User ou Developer — não Assistant. A resposta esperada vai em uma chave de nível superior como `reference_answer` que o avaliador referencia diretamente.

Se você estava fazendo supervised fine-tuning e quer mudar para RFT, precisa reestruturar seus dados de treinamento. Não pule essa etapa ou seus jobs vão falhar silenciosamente.

## Por Que Isso Importa para Desenvolvedores .NET

Se você está chamando modelos fine-tunados nas suas aplicações .NET através do SDK Azure OpenAI, treinamento mais barato significa que você pode iterar de forma mais agressiva. As opções de avaliadores de modelo significam que você pode fazer fine-tuning para tarefas com nuances — não apenas cenários de correspondência exata. E o guia de boas práticas no [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) vai te poupar tempo real de debugging.

Comece pequeno. Dez a cem amostras. Avaliador simples. Valide o ciclo. Depois escale.
