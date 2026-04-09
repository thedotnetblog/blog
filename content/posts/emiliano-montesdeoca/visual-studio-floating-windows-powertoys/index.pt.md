---
title: "Aquela Configuração de Janelas Flutuantes do Visual Studio Que Você Não Conhecia (Mas Deveria)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Uma configuração oculta do Visual Studio dá controle total sobre janelas flutuantes — entradas independentes na barra de tarefas, comportamento adequado com múltiplos monitores e integração perfeita com FancyZones. Um dropdown muda tudo."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "visual-studio-floating-windows-powertoys.md" >}}).*

Se você usa múltiplos monitores com o Visual Studio (e honestamente, quem não usa hoje em dia?), provavelmente já passou pela frustração: janelas flutuantes de ferramentas desaparecem quando você minimiza a IDE principal, elas sempre ficam em cima de tudo, e não aparecem como botões separados na barra de tarefas. Funciona para alguns fluxos de trabalho, mas para configurações com múltiplos monitores é frustrante.

Mads Kristensen da equipe do Visual Studio [compartilhou uma configuração pouco conhecida](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) que muda completamente como as janelas flutuantes se comportam. Um dropdown. Só isso.

## A configuração

**Tools > Options > Environment > Windows > Floating Windows**

O dropdown "These floating windows are owned by the main window" tem três opções:

- **None** — independência total. Cada janela flutuante tem sua própria entrada na barra de tarefas e se comporta como uma janela normal do Windows.
- **Tool Windows** (padrão) — documentos flutuam livremente, janelas de ferramentas ficam vinculadas à IDE.
- **Documents and Tool Windows** — comportamento clássico do Visual Studio, tudo vinculado à janela principal.

## Por que "None" é a melhor escolha para configurações com múltiplos monitores

Configure para **None** e de repente todas as suas janelas flutuantes de ferramentas e documentos se comportam como aplicações reais do Windows. Elas aparecem na barra de tarefas, ficam visíveis quando você minimiza a janela principal do Visual Studio, e param de se forçar para frente de tudo.

Combine isso com **PowerToys FancyZones** e é uma mudança total. Crie layouts personalizados nos seus monitores, encaixe seu Gerenciador de Soluções em uma zona, depurador em outra, e arquivos de código onde quiser. Tudo fica no lugar, tudo é acessível de forma independente, e seu espaço de trabalho parece organizado em vez de caótico.

## Recomendações rápidas

- **Usuários avançados com múltiplos monitores**: Configure para **None**, combine com FancyZones
- **Flutuadores ocasionais**: **Tool Windows** (padrão) é um bom meio-termo
- **Fluxo de trabalho tradicional**: **Documents and Tool Windows** mantém tudo clássico

Dica pro: **Ctrl + duplo clique** na barra de título de qualquer janela de ferramentas para flutuá-la ou ancorar instantaneamente. Não precisa reiniciar após mudar a configuração.

## Conclusão

É uma daquelas configurações do tipo "não acredito que eu não sabia disso". Se as janelas flutuantes do Visual Studio já te irritaram, vá mudar isso agora mesmo.

Leia o [post completo](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) para detalhes e capturas de tela.
