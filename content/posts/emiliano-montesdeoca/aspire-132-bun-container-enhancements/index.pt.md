---
title: "Aspire 13.2: Suporte a Bun, Melhores Contêineres e Menos Fricção no Debug"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 adiciona suporte de primeira classe ao Bun para apps Vite, corrige confiabilidade do Yarn e traz melhorias em contêineres que tornam o comportamento local mais previsível."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Esta postagem foi traduzida automaticamente. Para a versão original, [clique aqui](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/).*

Se você vem construindo backends .NET com frontends JavaScript no Aspire, a 13.2 é o tipo de atualização que melhora seu dia silenciosamente.

## Bun é Agora Cidadão de Primeira Classe

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

Se sua equipe já usa Bun, o Aspire não te força mais a nadar contra a corrente.

## Yarn Ficou Mais Confiável

Usuários do Yarn recebem menos falhas misteriosas com `withYarn()` e `addViteApp()`.

## Melhorias em Contêineres

`ImagePullPolicy.Never` para usar a imagem local sem ir ao registry. PostgreSQL 18+ com volumes de dados agora funciona corretamente.

## Melhorias de Debug

- `DebuggerDisplayAttribute` em tipos core
- Mensagens de erro melhores para `WaitFor`
- `BeforeResourceStartedEvent` disparado no momento certo

Post original de David Pine: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
