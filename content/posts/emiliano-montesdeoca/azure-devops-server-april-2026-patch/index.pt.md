---
title: "Azure DevOps Server Patch Abril 2026 — Correção na Conclusão de PRs e Atualizações de Segurança"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server recebe o Patch 3 com uma correção para falhas na conclusão de PRs, validação aprimorada no logout e restauração das conexões PAT com GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "azure-devops-server-april-2026-patch.md" >}}).*

Aviso rápido para equipes que rodam Azure DevOps Server auto-hospedado: a Microsoft lançou o [Patch 3 de abril 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) com três correções direcionadas.

## O que foi corrigido

- **Falhas na conclusão de pull requests** — uma exceção de referência nula durante o auto-completamento de work items podia causar falhas nos merges de PRs. Se você encontrou erros aleatórios na conclusão de PRs, essa é provavelmente a causa
- **Validação de redirecionamento no logout** — validação aprimorada durante o logout para prevenir possíveis redirecionamentos maliciosos. Essa é uma correção de segurança que vale a pena aplicar logo
- **Conexões PAT com GitHub Enterprise Server** — a criação de conexões por Personal Access Token com o GitHub Enterprise Server estava quebrada, agora foi restaurada

## Como atualizar

Baixe o [Patch 3](https://aka.ms/devopsserverpatch3) e execute o instalador. Para verificar se o patch foi aplicado:

```bash
<patch-installer>.exe CheckInstall
```

Se você roda Azure DevOps Server on-premises, a Microsoft recomenda fortemente manter-se no patch mais recente tanto por segurança quanto por confiabilidade. Confira as [notas de versão](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) para todos os detalhes.
