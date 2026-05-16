---
title: "Atualizações do Azure Developer CLI (azd) de abril de 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "o azd lançou cinco versões em abril de 2026, com destaque para o suporte a hooks em múltiplos idiomas para Python, JavaScript, TypeScript e .NET — mais a pré-visualização pública de azd update, verificações prévias de cota de IA e mais."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[O Azure Developer CLI (azd) lançou cinco versões em abril de 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14 a 1.24.2), com o grande tema sendo hooks que agora executam em Python, JavaScript, TypeScript e .NET — não apenas em Bash e PowerShell.

## Hooks em múltiplos idiomas no azure.yaml

Os hooks agora podem apontar para arquivos `.py`, `.js`, `.ts` ou `.cs` além de scripts shell. Cada linguagem obtém resolução automática de dependências:

- **Python** — detecta `requirements.txt` ou `pyproject.toml`, cria um virtualenv e instala dependências antes da execução. Configure o nome do ambiente com `virtualEnvName`.
- **JavaScript / TypeScript** — detecta `package.json` e executa `npm install` automaticamente. TypeScript é executado via `npx tsx` sem etapa de compilação. Escolha seu gerenciador de pacotes com o bloco de configuração `packageManager`.
- **.NET** — executa arquivos `.cs` com `dotnet run`. Scripts de arquivo único são suportados no .NET 10+. Configure o framework de destino através do bloco `configuration/framework`.

Isso significa que as equipes que já trabalham em uma dessas linguagens não precisam mais manter um hook Bash ou PowerShell separado apenas para conectar eventos do ciclo de vida de provisionamento.

## azd update entra em pré-visualização pública

`azd update` está agora em pré-visualização pública em todas as plataformas. Um único comando gerencia a atualização independentemente de como o azd foi instalado originalmente — sem precisar rastrear separadamente caminhos de Homebrew, WinGet ou MSI.

## Modo não interativo via AZD_NON_INTERACTIVE

Definir `AZD_NON_INTERACTIVE=true` (ou usar `--non-interactive` / `--no-prompt`) agora produz falhas consistentes e determinísticas em pipelines de CI/CD quando uma entrada necessária não pode ser resolvida automaticamente. Anteriormente, o comportamento era inconsistente entre os comandos.

## Verificação prévia de cota de modelos de IA

`azd provision` valida a cota do Azure Cognitive Services antes de tentar provisionar recursos de modelos de IA. Implantações que falhariam por limites de cota agora exibem o erro cedo no processo em vez de no meio do provisionamento.

## "Corrigir este erro" na solução de problemas do Copilot

A integração de solução de problemas do Copilot no azd ganha a capacidade de aplicar diretamente uma correção sugerida — não apenas descrevê-la. Quando o agente identifica um problema corrigível, ele pode fazer a alteração no local.

## Provedores de provisionamento personalizados e resolvedor de segredos do Key Vault

Os autores de extensões agora podem registrar backends de infraestrutura alternativos com `WithProvisioningProvider()`. Separadamente, o azd resolve automaticamente referências `@Microsoft.KeyVault(...)` antes de passar a configuração para extensões, eliminando a necessidade de resolução manual de segredos em provedores personalizados.

## Exclusões para templates e modo watch

Dois novos arquivos ignore oferecem controle mais preciso sobre o manuseio de arquivos:
- **`.azdignore`** — exclui arquivos exclusivos para colaboradores (documentação, configurações de CI) de cópias de templates para que os usuários finais obtenham um scaffold de projeto limpo.
- **`.azdxignore`** — exclui diretórios de disparar reconstruções durante `azd x watch`, reduzindo o ruído durante o desenvolvimento iterativo.

## Preflight de nomes reservados e opção docker.network

O azd agora avisa quando os nomes de recursos previstos conteriam palavras reservadas do Azure (`MICROSOFT`, `WINDOWS` ou o prefixo `LOGIN`) antes do início do provisionamento. Uma nova opção `docker.network` passa `--network` para `docker build`, útil em ambientes de proxy corporativo que exigem uma rede Docker específica.

## Correções de segurança

O pacote MSI do Windows agora inclui verificação de assinatura de código. Uma correção separada fecha um vazamento de variável de ambiente que poderia expor valores entre os limites dos comandos de extensão.

---

Um mês intenso — o suporte a hooks em múltiplas linguagens em particular elimina um ponto de fricção real para equipes que não trabalham principalmente em Bash. Consulte as [notas de versão completas](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) para o changelog completo de todas as cinco versões.
