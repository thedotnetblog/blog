---
title: "Removendo o Trabalho Repetitivo de Migração com Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape conduz a migração de um deployment real do AWS Terraform para Azure Bicep — extraindo a intenção do deployment e remapeando a arquitetura em vez de fazer uma conversão sintática 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — um passo a passo do Git-Ape (ferramenta git de engenharia de plataformas agêntica) migrando um repositório Terraform real da AWS para o Azure, com foco na extração de intenção em vez de conversão linha por linha.

## A entrada: contoso-migration

A fonte é um projeto Terraform real (`contoso-migration`) que implanta um aplicativo Next.js na AWS — EC2 para computação, ALB para balanceamento de carga, S3 para artefatos e chaves IAM para identidade. Custo: ~$34/mês. O objetivo não é reproduzir a mesma infraestrutura no Azure; é descobrir o que o deployment está realmente tentando fazer e reconstruí-lo com serviços nativos do Azure.

## Passo 1: Validação e autenticação

O Git-Ape começa validando todas as ferramentas CLI necessárias — `az`, `aws`, `gh`, `jq`, `git` — e confirmando as sessões de autenticação ativas antes de tocar em qualquer coisa. Sem execuções parciais.

## Passo 2: Extração de intenção

O agente lê todo o repositório fonte pela API do GitHub e extrai a intenção do deployment: runtime (Node.js), tipo de computação, padrão de ingress, tratamento de artefatos, modelo de identidade, rede e monitoramento. Este é o passo-chave — está construindo um modelo semântico do que o deployment faz, não quais palavras-chave do Terraform ele usa.

## Passo 3: Mapeamento de serviços

Os serviços AWS são mapeados para equivalentes do Azure:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Balanceamento de carga integrado do App Service
- Funções/chaves IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Passo 4: Agente crítico

Antes de gerar a saída, um agente crítico é executado e detecta dois problemas bloqueantes:

1. **Anti-padrão de build no startup** — o Terraform original estava executando `npm install && npm run build` no EC2 na inicialização. Solução: construir no CI, implantar um artefato pronto.
2. **Blob Storage desnecessário** — o S3 era usado para staging de artefatos que poderia ser eliminado com CI/CD adequado. O agente crítico o removeu completamente.

## Passo 5: Saída gerada

O resultado são ~80 linhas de Bicep em vez das 200+ linhas originais de Terraform. O agente criou um novo repositório GitHub com `infra/main.bicep` e `.github/workflows/deploy.yml` e removeu todos os arquivos específicos da AWS.

## Comparação de postura de segurança

A migração também produziu uma melhoria significativa de segurança:

| AWS original | Saída Azure |
|---|---|
| Somente HTTP | Somente HTTPS, TLS 1.2 |
| SSH aberto para 0.0.0.0/0 | Sem exposição SSH |
| Chaves de acesso IAM | OIDC + Managed Identity |
| Sem monitoramento | Application Insights |

Custo: ~$13/mês vs os $34/mês originais.

## O que o diferencia de um conversor de sintaxe

O passo do agente crítico é o que separa isso de uma tradução mecânica. Ele detectou padrões que teriam funcionado na AWS mas seriam incorretos no Azure — e os corrigiu em vez de replicá-los. A saída não é "AWS em sintaxe Azure"; é um deployment nativo do Azure que atinge o mesmo objetivo de forma mais limpa.

Veja o [guia completo](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) para o rastreamento completo do agente e arquivos gerados.
