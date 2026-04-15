---
title: ".NET Abril 2026 Servicing — Patches de segurança que você deve aplicar hoje"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "A atualização de servicing de abril de 2026 corrige 6 CVEs no .NET 10, .NET 9, .NET 8 e .NET Framework — incluindo duas vulnerabilidades de execução remota de código."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}}).*

As [atualizações de servicing de abril de 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) para .NET e .NET Framework já estão disponíveis, e esta inclui correções de segurança que você vai querer aplicar logo. Seis CVEs corrigidos, incluindo duas vulnerabilidades de execução remota de código (RCE).

## O que foi corrigido

Aqui vai o resumo rápido:

| CVE | Tipo | Afeta |
|-----|------|-------|
| CVE-2026-26171 | Bypass de recurso de segurança | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Execução remota de código** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Execução remota de código** | .NET 10, 9, 8 |
| CVE-2026-32203 | Negação de serviço | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Negação de serviço | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Negação de serviço | .NET Framework 2.0–4.8.1 |

Os dois CVEs de RCE (CVE-2026-32178 e CVE-2026-33116) afetam a maior gama de versões do .NET e devem ser a prioridade.

## Versões atualizadas

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

Todas estão disponíveis pelos canais habituais — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), imagens de contêineres no MCR e gerenciadores de pacotes Linux.

## O que fazer

Atualize seus projetos e pipelines de CI/CD para as últimas versões corrigidas. Se você está rodando contêineres, baixe as imagens mais recentes. Se está no .NET Framework, confira as [notas de versão do .NET Framework](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) para os patches correspondentes.

Para quem está rodando .NET 10 em produção (é a versão atual), 10.0.6 é uma atualização obrigatória. O mesmo vale para .NET 9.0.15 e .NET 8.0.26 se você está nessas versões LTS. Duas vulnerabilidades de RCE não são algo que se adia.
