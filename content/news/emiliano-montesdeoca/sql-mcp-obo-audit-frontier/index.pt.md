---
title: "A Verdadeira Fronteira para SQL Agêntico: Auditabilidade com OBO no SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "Autenticação On-Behalf-Of no Data API builder mais SQL MCP Server é um grande marco de governança porque o Azure SQL finalmente consegue auditar o humano por trás de uma ação de agente."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Há uma verdade dolorosa em projetos corporativos de IA: muitas equipes se obcecam pela qualidade do modelo e ignoram a responsabilização. Quando um agente escreve ou lê dados de produção, a primeira pergunta na revisão de um incidente não é "a resposta foi boa?" É "quem realmente fez isso?"

Fonte original: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

É por isso que o suporte a OBO no Data API builder 2.0 com o SQL MCP Server é uma questão maior do que parece à primeira vista. As abordagens de usuário/senha e identidade gerenciada ainda funcionam operacionalmente, mas ambas colapsam a identidade no limite do serviço. Os logs mostram a aplicação ou o middleware, não a origem da solicitação humana. Isso é aceitável para automação simples. Não é aceitável para fluxos de trabalho agênticos regulados.

Com o OBO, o SQL autentica o contexto do usuário delegado, não a identidade do host da ferramenta. Isso dá a você um modelo de auditoria fundamentalmente melhor: principal do usuário, ação, contexto da instrução e identificador da aplicação de camada intermediária, tudo junto. Você obtém rastreabilidade sem perder a superfície de controle das ferramentas MCP e das permissões de entidade do DAB.

Minha opinião é firme aqui: se seu agente pode tocar dados sensíveis do SQL, o OBO deveria ser sua arquitetura padrão, não uma tarefa opcional de blindagem. A configuração é mais trabalhosa, mas a dívida de identidade sempre é paga depois, geralmente durante incidentes de segurança, auditorias de conformidade ou escalonamentos executivos.

Orientação prática de implementação:

Comece validando o fluxo de identidade com uma view mínima de "WhoAmI" e verificações automatizadas em testes de integração. Se o principal do SQL não corresponder ao usuário autenticado, pare e corrija antes de publicar. Em seguida, conecte consultas do Log Analytics para SQLSecurityAuditEvents aos dashboards do seu SOC e alerte sobre ações de alto risco iniciadas por caminhos OBO. Por fim, alinhe RBAC e permissões do DAB para que identidade no nível do usuário e autorização no nível da ação permaneçam consistentes de ponta a ponta.

Um ponto de design sutil, mas importante, no anúncio é o comportamento de cache. O DAB bloqueia explicitamente o cache de resposta quando a autenticação delegada pelo usuário está habilitada. Essa troca está correta. Truques de performance que podem vazar resultados com escopo de usuário não valem a pena em ambientes multi-tenant ou regulados.

SQL MCP Server mais OBO é o começo de um padrão maduro: agentes como operadores controlados, usuários como principais responsáveis, planos de dados como sistemas auditáveis. Se sua arquitetura não consegue responder "quem fez isso" com confiança, ela não está pronta para produção em IA, não importa quão polida seja a demo.
