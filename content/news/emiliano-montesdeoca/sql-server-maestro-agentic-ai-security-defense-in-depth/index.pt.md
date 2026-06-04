---
title: "MAESTRO, Defesa em Profundidade e Por Que o SQL Server Agora é uma Fronteira de Segurança para IA"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "A IA agêntica introduz ameaças para as quais os modelos STRIDE tradicionais não foram projetados. Veja como o Microsoft SQL se mapeia ao framework MAESTRO para fornecer uma fronteira de execução governada."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Os modelos de ameaças de segurança são construídos sobre suposições sobre quem ou o que está fazendo as solicitações. O STRIDE assume atores humanos interagindo com sistemas através de interfaces definidas. Os agentes de IA não funcionam dessa forma.

## O STRIDE Não Foi Projetado para Agentes de IA

Os sistemas agênticos operam de forma autônoma, encadeiam ferramentas por meio de chamadas de API, tomam decisões sobre quais dados recuperar e quais ações executar, e podem receber instruções de várias fontes — prompts do usuário, resultados de ferramentas, dados recuperados. O modelo de ameaças STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) não captura adequadamente vetores de ataque específicos de agentes como injeção de prompt, envenenamento de contexto ou abuso de ferramentas.

A Cloud Security Alliance publicou o framework MAESTRO especificamente para o risco de agentes de IA.

## O Framework MAESTRO

O MAESTRO organiza o risco de IA agêntica em sete camadas:

1. **Foundation Models** — os LLMs subjacentes e suas vulnerabilidades de treinamento
2. **Data Operations** — recuperação, armazenamento e manipulação de dados
3. **Agent Frameworks** — o middleware de orquestração e coordenação de agentes
4. **Deployment & Infrastructure** — onde os agentes são executados e como são configurados
5. **Evaluation & Observability** — monitoramento do comportamento dos agentes ao longo do tempo
6. **Security & Compliance** — controles de acesso, auditoria e conformidade regulatória
7. **Agent Ecosystem** — como os agentes interagem entre si e com ferramentas externas

Cada camada tem vetores de ataque específicos que os controles de segurança tradicionais não abordam diretamente.

## Microsoft SQL Como Fronteira de Execução Governada

O SQL Server 2025 se mapeia para as camadas do MAESTRO de maneiras concretas:

**Camada Data Operations**: `AI_GENERATE_EMBEDDINGS` integrado ao T-SQL mantém as operações vetoriais dentro da fronteira governada do banco de dados. Os dados não precisam sair para o serviço de modelo para o processamento de embeddings.

**Camadas Security & Compliance**: A segurança no nível de linha (RLS) e o mascaramento dinâmico de dados (DDM) se aplicam independentemente de como a solicitação chegou — seja de um usuário humano ou de um agente de IA. O agente não pode contornar controles que são impostos pelo próprio banco de dados.

**Camada Agent Frameworks**: Os procedimentos armazenados servem como fronteiras de ferramentas. Em vez de dar aos agentes acesso SQL arbitrário, você define as operações permitidas como procedimentos e as expõe como ferramentas de agente. As consultas parametrizadas evitam injeção no nível de execução.

**Camada Evaluation & Observability**: O log de auditoria e o Query Store capturam o que cada agente realmente executou — não apenas o que foi solicitado a fazer. Essa rastreabilidade é crítica para investigações de incidentes em sistemas agênticos onde a atribuição é complexa.

## Defesa em Profundidade para IA Agêntica

O princípio permanece o mesmo que na segurança tradicional: nenhum controle único é suficiente. O que muda é quais controles mais importam para os agentes:

**Reduzir o raio de impacto**: as fronteiras de ferramentas de procedimentos armazenados significam que um agente comprometido só pode executar operações predefinidas. Ele não pode pivotar para consultas arbitrárias.

**Observabilidade**: você deve ser capaz de responder "o que exatamente esse agente fez?" após um incidente. Os sistemas de IA agêntica sem rastreabilidade no nível do banco de dados têm pontos cegos que o log de aplicação não cobre.

**Execução restrita**: parametrização, RLS e DDM são ativos de segurança independentemente de o chamador ser humano. Não os enfraqueça para acomodar agentes.

**Responsabilidade**: o log de auditoria do SQL Server cria um registro de quem (qual agente, usando quais credenciais) executou o quê em que momento. Isso importa quando os sistemas agênticos tomam ações com consequências reais no mundo.

O SQL Server 2025 não foi construído para resolver o risco agêntico de forma abstrata — foi construído para ser um banco de dados relacional. Mas a governança que torna um banco de dados empresarial confiável se revela ser exatamente o que torna segura uma fronteira de execução de agentes.

Post original: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
