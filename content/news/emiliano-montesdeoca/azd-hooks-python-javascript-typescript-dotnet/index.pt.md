---
title: "Hooks do azd em Python, TypeScript e .NET: chega de scripts shell"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "A CLI do Azure Developer agora suporta hooks em Python, JavaScript, TypeScript e .NET. Sem mais troca de contexto para Bash só para rodar um script de migração."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Se você já teve um projeto completamente em .NET e mesmo assim precisou escrever scripts Bash para os hooks do azd, conhece bem essa dor. Por que mudar para sintaxe de shell num passo de pré-provisioning quando tudo o mais no projeto é C#?

Essa frustração agora tem uma solução oficial. A CLI do Azure Developer [acaba de lançar suporte a múltiplos idiomas para hooks](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), e é exatamente tão bom quanto parece.

## Hooks, brevemente

Hooks são scripts que rodam em pontos-chave do ciclo de vida do `azd` — antes do provisioning, após o deployment e mais. São definidos no `azure.yaml` e permitem injetar lógica customizada sem modificar a CLI.

Antes, apenas Bash e PowerShell eram suportados. Agora você pode usar **Python, JavaScript, TypeScript ou .NET** — e o `azd` cuida do resto automaticamente.

## Como funciona a detecção

Basta apontar o hook para um arquivo e o `azd` infere o idioma pela extensão:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Sem configuração extra. Se a extensão for ambígua, você pode adicionar `kind: python` (ou o que for) para especificar explicitamente.

## Detalhes por linguagem

### Python

Coloque um `requirements.txt` ou `pyproject.toml` ao lado do script (ou em um diretório pai). O `azd` cria automaticamente um ambiente virtual, instala dependências e executa o script.

### JavaScript e TypeScript

Mesmo padrão — coloque um `package.json` perto do script e o `azd` executará `npm install` primeiro. Para TypeScript, usa `npx tsx` sem etapa de compilação e sem `tsconfig.json`.

### .NET

Dois modos disponíveis:

- **Modo projeto**: Se houver um `.csproj` ao lado do script, o `azd` executa `dotnet restore` e `dotnet build` automaticamente.
- **Modo single-file**: No .NET 10+, arquivos `.cs` independentes executam diretamente via `dotnet run script.cs`. Sem arquivo de projeto.

## Configuração por executor

Cada linguagem suporta um bloco `config` opcional:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## Por que isso importa para desenvolvedores .NET

Os hooks eram o último lugar num projeto baseado em azd que forçava uma troca de linguagem. Agora todo o pipeline de deployment pode viver em um único idioma. Você pode reutilizar utilitários .NET existentes em hooks, referenciar bibliotecas compartilhadas e abandonar a manutenção de scripts shell.

## Conclusão

Um desses mudanças que parecem pequenas, mas que removem muita fricção do dia a dia com azd. O suporte multi-linguagem para hooks já está disponível — confira o [post oficial](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) para a documentação completa.
