---
title: "FIDES é o tipo de história de segurança determinística para agentes que eu quero ver mais"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "As novas capacidades de FIDES no Agent Framework importam porque movem a defesa contra prompt injection para longe de heurísticas e em direção a uma política aplicável baseada em conteúdo rotulado e verificações de middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Defesas contra prompt injection muitas vezes parecem estar apoiadas em terreno instável.

Você adiciona um system prompt mais forte. Você adiciona um filtro. Você cria algumas allowlists. E espera que a próxima entrada estranha não quebre as suposições.

É por isso que **FIDES** é interessante.

A parte forte da história é que ela move a segurança para algo mais determinístico:

- rótulos no conteúdo
- propagação dos rótulos ao longo do workflow
- aplicação via middleware antes que ferramentas privilegiadas sejam executadas
- limites claros de política sobre o que o contexto não confiável pode influenciar

## O artigo original é direto do jeito certo

Ele começa dizendo que prompt injection é "**o risco número 1 no OWASP LLM Top 10**".

Ótimo.

Gosto desse tipo de franqueza aqui, porque equipes demais ainda tratam a segurança de agentes como se fosse uma preocupação futura, e não um problema atual de design de runtime.

E o artigo segue com um contraste prático forte: a maioria das defesas atuais é heurística, enquanto FIDES tenta levar o sistema para a política e a aplicação.

Esse é exatamente o movimento certo.

## O que o torna mais convincente que outro whitepaper de segurança

Muitos textos sobre segurança de IA permanecem abstratos.

Este artigo faz algo melhor. Ele percorre um exemplo muito concreto: um agente de triagem de issues do GitHub, um body de issue malicioso, uma leitura de arquivo privilegiada e uma tentativa de vazamento de comentário público.

Isso é útil porque ancora toda a discussão em um workflow real.

E, uma vez que você vê esse cenário, o valor dos controles determinísticos fica muito mais fácil de entender.

## A ideia central não é "torne o modelo mais inteligente"

O mais importante aqui é que FIDES não pede ao modelo que se torne magicamente melhor em detectar ataques.

Ele está mudando o contrato de runtime.

Isso significa:

- o conteúdo recebe rótulos
- os rótulos se propagam
- as ferramentas declaram o que aceitam
- o middleware bloqueia caminhos inseguros antes da execução

Essa é uma abordagem muito mais saudável.

Porque, uma vez que o agente pode chamar ferramentas com consequências reais, a segurança não pode depender apenas de o modelo estar tendo um bom dia ou não.

## Minha opinião

Esse é exatamente o tipo de direção em segurança de agentes que eu quero ver mais.

Não "confie no modelo para ignorar instruções ruins", mas "construa a cerca de política dentro do runtime".

Isso é um modelo muito mais saudável.

E, se os frameworks de agentes quiserem ser levados a sério em produção, vão precisar de mais histórias como esta.

Post original: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)