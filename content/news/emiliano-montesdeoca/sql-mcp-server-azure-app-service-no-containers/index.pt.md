---
title: "SQL MCP Server no Azure App Service — Sem Contêineres"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "O SQL MCP Server agora pode rodar no Azure App Service sem Docker ou Kubernetes. O que isso significa para desenvolvedores .NET construindo agentes de IA que falam com bancos de dados SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Vou ser honesto contigo: toda vez que vejo "requer um contêiner" em um tutorial, uma pequena parte de mim suspira. Contêineres são ótimos — até que a sua equipe não tem uma estratégia de contêineres, e de repente uma funcionalidade que parecia simples fica bloqueada por sobrecarga de orquestração que ninguém planejou.

Por isso esse aqui chamou minha atenção. O SQL MCP Server agora pode rodar no Azure App Service — sem Docker, sem Kubernetes, apenas com a mesma configuração do Data API Builder (DAB) que expõe seu banco de dados SQL via MCP, REST e GraphQL.

## O que é o SQL MCP Server?

Contexto rápido se você ainda não o conhece. O SQL MCP Server fica entre o seu agente de IA e o seu banco de dados SQL. Em vez de dar ao agente acesso direto ao banco (o que seria uma péssima ideia), ele expõe suas tabelas e views como uma camada de abstração — entidades com permissões definidas.

É construído sobre o [Data API Builder](https://learn.microsoft.com/pt-br/azure/data-api-builder/), o que significa que um único arquivo de configuração gerencia MCP *e* REST *e* GraphQL simultaneamente. Seu agente fala com o endpoint MCP. Sua aplicação tradicional fala com REST ou GraphQL. Mesma config, mesmo runtime, superfícies diferentes.

Isso é genuinamente útil. Você não mantém duas camadas de API separadas.

## O Problema do Contêiner (e a Solução)

O modelo de deployment original do SQL MCP Server usava contêineres. Funciona bem em muitas equipes — mas não em todas. Muitas equipes .NET padronizam no Azure App Service ou VMs. Exigir um runtime de contêiner apenas para expor um endpoint SQL adiciona fricção que ninguém pediu.

O novo tutorial mostra como pular o contêiner completamente. Tudo funciona com um comando `dab start`, hospedado no App Service como um processo web .NET 8 padrão.

```bash
# Instalar Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Inicializar a configuração
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Adicionar uma entidade
dab add products --source dbo.products --permissions "authenticated:*"

# Configurar o provedor de auth do App Service
dab configure --runtime.host.authentication.provider AppService

# Iniciar o servidor
dab start
```

Neste ponto você tem MCP em `/mcp`, REST e GraphQL do mesmo processo, e nada rodando em contêiner.

## Autenticação Sem Chaves de API Compartilhadas

Essa é a parte que mais aprecio. Ao fazer o deploy no App Service, você configura o Microsoft Entra ID como provedor de autenticação. Sem segredos compartilhados em arquivos de configuração, sem chaves de API para rotacionar.

A string de conexão fica em uma variável de ambiente do App Service (não no `dab-config.json`), e o endpoint MCP é protegido pela autenticação da plataforma. Se você já está alinhado com o Entra ID em suas cargas de trabalho Azure, isso se encaixa naturalmente.

Para desenvolvimento local, você muda para o modo `Simulator` e transporte STDIO. Volta para o modo `AppService` antes do deploy. Limpo e explícito.

## Deploy no App Service

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Depois você faz o deploy do seu projeto DAB usando o método de deployment de código que sua equipe já usa. O detalhe importante: é um deployment de **código**, não de contêiner.

## Por que Isso Importa para Desenvolvedores .NET

Se você está construindo agentes de IA em .NET, eventualmente seu agente precisará falar com um banco de dados. O SQL MCP Server te dá uma maneira estruturada de fazer isso sem expor strings de conexão brutas.

Confira o tutorial completo no [post original](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) e o [repositório de exemplo no GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Conclusão

O SQL MCP Server no App Service é uma opção pragmática sólida para equipes .NET que querem dar aos seus agentes acesso estruturado a dados SQL sem uma estratégia de contêineres. Experimente — seus agentes vão apreciar a superfície de API limpa.
