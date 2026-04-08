---
title: "SQL MCP Server — A forma certa de dar acesso a bancos de dados para agentes de IA"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server do Data API builder dá aos agentes de IA acesso seguro e determinístico a bancos de dados sem expor esquemas ou depender de NL2SQL. RBAC, cache, suporte multi-banco — tudo incluído."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "sql-mcp-server-data-api-builder.md" >}}).*

Vamos ser honestos: a maioria dos servidores MCP de banco de dados disponíveis hoje são assustadores. Eles pegam uma consulta em linguagem natural, geram SQL na hora e executam contra seus dados de produção. O que poderia dar errado? (Tudo. Tudo poderia dar errado.)

O time do Azure SQL acabou de [apresentar o SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), e ele adota uma abordagem fundamentalmente diferente. Construído como uma funcionalidade do Data API builder (DAB) 2.0, dá aos agentes de IA acesso estruturado e determinístico a operações de banco de dados — sem NL2SQL, sem expor seu esquema, e com RBAC completo em cada etapa.

## Por que não NL2SQL?

Essa é a decisão de design mais interessante. Modelos não são determinísticos, e consultas complexas são as mais propensas a produzir erros sutis. As consultas exatas que os usuários esperam que a IA gere são também as que precisam de mais escrutínio quando produzidas de forma não determinística.

Em vez disso, o SQL MCP Server usa uma abordagem **NL2DAB**. O agente trabalha com a camada de abstração de entidades do Data API builder e seu construtor de consultas integrado para produzir T-SQL preciso e bem formado de maneira determinística. Mesmo resultado para o usuário, mas sem o risco de JOINs alucinados ou exposição acidental de dados.

## Sete ferramentas, não setecentas

O SQL MCP Server expõe exatamente sete ferramentas DML, independentemente do tamanho do banco de dados:

- `describe_entities` — descobrir entidades e operações disponíveis
- `create_record` — inserir linhas
- `read_records` — consultar tabelas e views
- `update_record` — modificar linhas
- `delete_record` — remover linhas
- `execute_entity` — executar stored procedures
- `aggregate_records` — consultas de agregação

Isso é inteligente porque janelas de contexto são o espaço de pensamento do agente. Inundá-las com centenas de definições de ferramentas deixa menos espaço para raciocínio. Sete ferramentas fixas mantêm o agente focado em *pensar* em vez de *navegar*.

Cada ferramenta pode ser habilitada ou desabilitada individualmente:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Começando em três comandos

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Isso é um SQL MCP Server rodando e expondo sua tabela Customers. A camada de abstração de entidades significa que você pode criar aliases para nomes e colunas, limitar campos por papel, e controlar exatamente o que os agentes veem — sem expor detalhes internos do esquema.

## A história de segurança é sólida

É aqui que a maturidade do Data API builder compensa:

- **RBAC em cada camada** — cada entidade define quais papéis podem ler, criar, atualizar ou deletar, e quais campos são visíveis
- **Integração com Azure Key Vault** — strings de conexão e segredos gerenciados com segurança
- **Microsoft Entra + OAuth personalizado** — autenticação de nível de produção
- **Content Security Policy** — agentes interagem através de um contrato controlado, não SQL cru

A abstração de esquema é particularmente importante. Seus nomes internos de tabelas e colunas nunca são expostos ao agente. Você define entidades, aliases e descrições que fazem sentido para a interação com IA — não seu diagrama ERD do banco de dados.

## Multi-banco e multi-protocolo

O SQL MCP Server suporta Microsoft SQL, PostgreSQL, Azure Cosmos DB e MySQL. E como é uma funcionalidade do DAB, você obtém endpoints REST, GraphQL e MCP simultaneamente da mesma configuração. Mesmas definições de entidades, mesmas regras RBAC, mesma segurança — nos três protocolos.

A auto-configuração no DAB 2.0 pode até inspecionar seu banco de dados e construir a configuração dinamicamente, se você estiver confortável com menos abstração para prototipagem rápida.

## Minha opinião

É assim que o acesso empresarial a bancos de dados para agentes de IA deveria funcionar. Não "ei LLM, escreve SQL pra mim e YOLO contra produção." Em vez disso: uma camada de entidades bem definida, geração determinística de consultas, RBAC em cada etapa, cache, monitoramento e telemetria. É chato da melhor maneira possível.

Para desenvolvedores .NET, a história de integração é limpa — DAB é uma ferramenta .NET, o MCP Server roda como contêiner, e funciona com Azure SQL, que a maioria de nós já está usando. Se você está construindo agentes de IA que precisam de acesso a dados, comece aqui.

## Finalizando

SQL MCP Server é gratuito, open-source e roda em qualquer lugar. É a abordagem prescritiva da Microsoft para dar aos agentes de IA acesso seguro a bancos de dados. Confira o [post completo](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) e a [documentação](https://aka.ms/sql/mcp) para começar.
