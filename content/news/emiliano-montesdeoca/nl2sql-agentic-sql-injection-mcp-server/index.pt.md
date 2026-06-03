---
title: "NL2SQL é a Injeção SQL da Era Agêntica"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Antes de deixar um agente consultar seu banco de dados com linguagem natural, leia isto. NL2SQL parece simples até você pensar sobre completude do esquema, indeterminismo e o que o SQL MCP Server realmente resolve."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Há uma versão do argumento NL2SQL que soa perfeita: os usuários fazem perguntas em linguagem natural, os agentes geram SQL, os dados voltam. Menos telas, menos consultas, menos código. Simples.

Então você pensa por mais cinco minutos.

## Os Problemas sobre os quais Ninguém Fala na Demo

**Os esquemas não foram projetados para explicar as coisas.** Nomes de tabelas crípticos, nomes de colunas inconsistentes, relacionamentos tecnicamente válidos que são semanticamente inválidos sem predicados adicionais — isso é normal para bancos de dados empresariais. Não são bugs, são simplesmente a história acumulada das mudanças de negócio. Mas quando você pede a um modelo que infira intenção de um esquema que não foi projetado para comunicar intenção, o modelo tentará de qualquer forma. Não desistirá. Gerará sua melhor consulta possível e retornará resultados com confiança.

**Os modelos não são determinísticos.** Faça a mesma pergunta sobre o mesmo banco de dados duas vezes e você pode obter SQL diferente. O modelo está calculando probabilidades, e ligeiras variações no contexto geram saídas diferentes. Você não pode testar seu caminho para uma garantia de que o agente sempre gera a consulta correta.

**A revisão do usuário não escala.** "Apenas revise cada consulta antes da execução" soa seguro. Mas assume que os usuários são especialistas tanto no modelo de dados quanto em SQL — exatamente as pessoas que não precisavam da interface de linguagem natural. Também introduz sobrecarga cognitiva e uma nova classe de viés de confirmação, onde usuários sobrecarregados pela complexidade da consulta aprovam consultas inválidas em vez de investigá-las.

**E então há injeção.** No desenvolvimento SQL tradicional, a parametrização resolveu a injeção porque a entrada do usuário preenchia parâmetros, não a estrutura SQL. Com NL2SQL, o modelo gera o SQL em si. O prompt, o contexto do esquema, o histórico de conversação e os dados recuperados influenciam o que é executado. Se alguém elabora um prompt que muda o que o modelo gera, isso é injeção — não no nível do parâmetro, mas no nível de geração de consultas. E ao contrário de eliminar uma tabela (óbvio, recuperável), a injeção NL2SQL produz consultas que retornam resultados incorretos sem nenhum erro visível. Decisões de negócio são tomadas com dados errados.

## O que o SQL MCP Server Realmente Resolve

É aqui que o artigo faz seu ponto prático mais útil. Em vez de dar a um agente acesso arbitrário ao esquema e esperar o melhor, o SQL MCP Server expõe uma **superfície de API curada** construída sobre o [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

A diferença importa: o agente não gera SQL. Ele chama endpoints nomeados que retornam formas de resultado predefinidas. O SQL é escrito uma vez, por um desenvolvedor, e é determinístico. O não-determinismo do agente é limitado a escolher *qual* endpoint chamar, não a construir consultas arbitrárias.

Isso é análogo ao que a parametrização fez para a injeção SQL no modelo de aplicativo tradicional — você remove a capacidade de construir consultas arbitrárias a partir de entrada não confiável.

## A Pergunta Certa

O artigo não diz "nunca use NL2SQL." Ele diz: seja deliberado sobre *onde* você o aplica e *o que* você expõe. Para análise exploratória em um ambiente controlado, com um esquema limitado e acesso somente leitura, NL2SQL pode estar bem. Para sistemas de produção onde decisões de negócio dependem dos resultados, uma camada de API curada é significativamente mais segura.

Honestidade: alguns problemas são genuinamente melhor resolvidos com consultas estruturadas atrás de endpoints nomeados do que com linguagem natural para SQL. O SQL MCP Server te dá essa opção sem abandonar completamente a interface agêntica.

Post original: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
