---
title: "dotnet new WinUI: Criar apps Windows sem tocar no Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Os templates de projeto WinUI agora funcionam com dotnet new — apps em branco, padrões NavigationView e mais. Suporte a VS Code, sem necessidade do Visual Studio, com Fluent Design por padrão."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

O desenvolvimento com WinUI costumava exigir o Visual Studio. Isso está a mudar: a Microsoft publicou templates de projetos e itens open source para WinUI que funcionam com `dotnet new`, trazendo o desenvolvimento de apps Windows para o fluxo de trabalho padrão da CLI.

## Começar em três comandos

```shell
# Instalar os templates
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Criar uma app NavigationView
dotnet new winui-navview -n MyApp

# Executar
cd MyApp
dotnet run
```

Sem Visual Studio, sem configuração manual do projeto. A app executa com `dotnet run`.

## O que está incluído

**Template em branco** (`dotnet new winui`) — um ponto de partida moderno com uma barra de título Fluent já configurada, ícone de app atualizado com asset `.ico`, e valores padrão corretos para modo claro/escuro. Melhor do que o antigo template em branco que te deixava a configurar o básico sozinho.

**Template NavigationView** (`dotnet new winui-navview`) — o padrão de navegação master-detail, totalmente configurado com um NavigationView, barra de título moderna e estrutura de navegação multipágina. Segue a silhueta padrão de apps Windows para aplicações baseadas em navegação. Se estás a construir algo com navegação lateral, começa aqui.

Ambos os templates seguem as [silhuetas de apps Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — padrões modernos de Fluent Design para layout, navegação e estrutura visual — prontos a usar desde o início.

## Por que importa para developers que não usam Visual Studio

Os developers WinUI que usam VS Code, Rider ou ferramentas de linha de comandos têm sido negligenciados. Os templates existentes do Visual Studio não eram utilizáveis fora do VS — era preciso recriar manualmente a estrutura do projeto e configurar o básico.

Estes templates são open source (ver [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), desenvolvidos a partir do [feedback da comunidade](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), e disponíveis agora. O suporte ao Visual Studio está a ser desenvolvido — estes mesmos templates funcionarão também lá eventualmente.

Para equipas que querem automatizar a configuração dos seus projetos WinUI, integrá-la em CI, ou simplesmente usar um editor diferente do Visual Studio, isto é uma melhoria significativa.

Post original: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
