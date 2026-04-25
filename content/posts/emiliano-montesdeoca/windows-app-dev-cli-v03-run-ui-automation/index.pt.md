---
title: "Windows App Dev CLI v0.3: F5 a partir do terminal e automação de UI para agentes"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 traz winapp run para lançamentos debug a partir do terminal, winapp ui para automação de interface e um novo pacote NuGet que faz o dotnet run funcionar com apps empacotadas."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

A experiência F5 do Visual Studio é fantástica. Mas ter que abrir o VS só para lançar e depurar uma app Windows empacotada é demais — seja num pipeline de CI, num workflow automatizado, ou quando um agente de IA está fazendo os testes.

Windows App Development CLI v0.3 acabou de ser [lançada](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) e aborda isso diretamente com dois recursos principais: `winapp run` e `winapp ui`.

## winapp run: F5 a partir de qualquer lugar

`winapp run` recebe uma pasta de app não empacotada e um manifesto, e faz tudo que o VS faz num debug launch: registra um pacote loose, lança a app e preserva o `LocalState` entre re-deploys.

```bash
# Compilar a app e então executá-la como app empacotada
winapp run ./bin/Debug
```

Funciona para WinUI, WPF, WinForms, Console, Avalonia e mais. Os modos são pensados para desenvolvedores e workflows automatizados:

- **`--detach`**: Lança e devolve o controle ao terminal imediatamente. Perfeito para CI.
- **`--unregister-on-exit`**: Limpa o pacote registrado ao fechar a app.
- **`--debug-output`**: Captura mensagens `OutputDebugString` e exceções em tempo real.

## Novo pacote NuGet: dotnet run para apps empacotadas

Para desenvolvedores .NET há um novo pacote NuGet: `Microsoft.Windows.SDK.BuildTools.WinApp`. Após a instalação, `dotnet run` cuida de todo o inner loop: build, preparar um pacote loose-layout, registrar no Windows e lançar — tudo em uma etapa.

```bash
winapp init
# ou
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI Automation a partir da linha de comando

Este é o recurso que abre os cenários agênticos. `winapp ui` fornece acesso completo de UI Automation a qualquer app Windows em execução — WPF, WinForms, Win32, Electron, WinUI3 — diretamente do terminal.

O que é possível fazer:

- Listar todas as janelas de nível superior
- Navegar pela árvore completa de UI Automation de uma janela
- Procurar elementos por nome, tipo ou ID de automação
- Clicar, invocar e definir valores
- Tirar screenshots
- Aguardar o aparecimento de elementos — ideal para sincronização de testes

Combinar `winapp ui` com `winapp run` cria um workflow completo build → lançar → verificar a partir do terminal. Um agente pode executar a app, inspecionar o estado da UI e validar o resultado.

## Outras novidades

- **`winapp unregister`**: Remove um pacote sideloaded quando terminar.
- **`winapp manifest add-alias`**: Adiciona um alias para lançar a app por nome a partir do terminal.
- **Tab completion**: Configure o completamento PowerShell com um único comando.

## Como obter

```bash
winget install Microsoft.WinAppCli
# ou
npm install -g @microsoft/winappcli
```

A CLI está em preview pública. O [repositório no GitHub](https://github.com/microsoft/WinAppCli) tem a documentação completa e o [anúncio original](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) tem todos os detalhes.
