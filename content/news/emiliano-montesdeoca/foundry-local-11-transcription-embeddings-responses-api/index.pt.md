---
title: "Foundry Local 1.1: Transcrição em Tempo Real, Embeddings e a API de Respostas"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 adiciona transcrição ao vivo do microfone, embeddings de texto e suporte à API de Respostas — tudo a correr localmente sem dependência da cloud, sem latência de rede, sem custo por token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 provou o conceito: executar modelos de IA localmente no Windows, macOS (Apple Silicon) e Linux x64 com um SDK amigável para desenvolvedores. A versão 1.1 adiciona três capacidades que cobrem muitos casos de uso reais em produção.

## Transcrição de Áudio em Directo

A nova funcionalidade mais significativa: streaming de voz para texto em tempo real diretamente do microfone. Legendas, interfaces de voz, transcrição de reuniões, ferramentas de acessibilidade — tudo a correr localmente sem qualquer dependência da cloud.

A API é baseada em sessões e transmite resultados à medida que chegam, com marcadores `is_final` para distinguir texto intermédio do finalizado. Disponível para todos os bindings de linguagem: JavaScript, C#, Python e Rust.

Carrega um modelo de voz em streaming do catálogo, cria uma sessão com definições de áudio (frequência de amostragem, canais, idioma), inicia-a, envia blocos de áudio PCM em bruto e consome o stream assíncrono de resultados. O post tem exemplos completos em Python e C#.

## Embeddings de Texto

Pesquisa semântica, pipelines RAG, clustering, correspondência de similaridade — tudo isto requer embeddings. Foundry Local 1.1 adiciona suporte para modelos de embedding para que possas gerar vetores localmente a partir do mesmo SDK, sem enviar dados para um endpoint na cloud.

Para aplicações onde a residência de dados é importante ou onde processas conteúdo sensível, a geração local de embeddings é uma capacidade significativa.

## API de Respostas

O Foundry Local suporta agora a [API de Respostas](https://platform.openai.com/docs/api-reference/responses) — a interface estruturada concebida para interações agênticas. Isto adiciona:

- **Chamada de ferramentas** — permite que modelos a correr localmente invoquem ferramentas que defines
- **Entrada multimodal visão-linguagem** — passa imagem + texto a modelos com capacidade de visão
- Compatível com a forma padrão de API, pelo que agentes existentes que apontam para a API de Respostas da OpenAI funcionam contra modelos locais

## Melhorias no Tamanho do Pacote

Duas alterações reduzem o tamanho do pacote JavaScript:
- A camada FFI `koffi` foi substituída por um addon C Node-API personalizado
- O fornecedor de execução WebGPU é distribuído como plugin separado, pelo que as aplicações que não precisam de aceleração GPU não pagam o custo de tamanho

O SDK C# agora aponta para versões de framework inferiores para compatibilidade .NET mais ampla.

## Por Que Importa

As três capacidades juntas — transcrição, embeddings, chamada de ferramentas — cobrem os blocos de construção fundamentais de muitas aplicações de IA. Executá-los localmente significa:
- Sem internet necessária
- Sem custos por token
- Sem dados a sair da máquina
- Latência consistente independentemente das condições de rede

Foundry Local é a escolha certa para cenários de edge, cargas de trabalho sensíveis à privacidade, aplicações offline, ou qualquer coisa onde se queira evitar a dependência da cloud durante o desenvolvimento.

Post original: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
