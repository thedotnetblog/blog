---
title: "Extensão WinApp para VS Code: Execute, Depure e Empacote Apps Windows Sem Sair do Editor"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "A extensão WinApp para VS Code traz o CLI completo de Desenvolvimento de Apps Windows diretamente para o VS Code — execute, depure com identidade de pacote, empacote e assine apps Windows sem tocar no Visual Studio."
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Se já tentou desenvolver uma app Windows no VS Code, você conhece aquele momento. Está a trabalhar no fluxo, editando código no seu editor preferido — e de repente precisa de identidade de pacote para uma API do Windows. Ou criar um MSIX. Ou assinar um pacote. E de repente está a abrir o Visual Studio, ou a pesquisar no Google "msix packaging without visual studio" às 23h.

Esse atrito já não existe. A [extensão WinApp para VS Code](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp) está em preview pública — e é o [CLI de Desenvolvimento de Apps Windows](https://github.com/microsoft/WinAppCli) completo integrado diretamente no VS Code. Sem instalação separada, sem Visual Studio necessário.

## Identidade de Pacote com F5

O problema com as APIs do Windows — notificações, tarefas em segundo plano, funcionalidades de IA on-device, share targets — muitas delas exigem que a sua app tenha **identidade de pacote**. Sem ela, essas APIs simplesmente não funcionam.

Obter identidade de pacote tradicionalmente significava construir um instalador MSIX completo ou executar a partir do Visual Studio. A extensão WinApp muda isto completamente com um tipo de depuração `winapp` personalizado.

Adicione isto ao seu `launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

Prima F5. A extensão localiza o seu build output e manifesto, dá à sua app identidade de pacote via `winapp run`, e anexa o depurador. Para apps .NET é `coreclr` (requer C# Dev Kit). C/C++ usa `cppvsdbg`. Node/Electron usa o depurador incorporado.

Pode configurar um `preLaunchTask` para que o projeto compile automaticamente antes de cada F5 — mesmo fluxo build-and-launch do Visual Studio, mas no VS Code.

## Tudo na Paleta de Comandos

Abra `Ctrl+Shift+P`, escreva `WinApp`, e obtém o kit de ferramentas completo:

- **Initialize Project** — configurar o projeto com Windows SDK e/ou Windows App SDK
- **Run Application** — lançar como app empacotada com identidade de pacote
- **Create MSIX Package** — empacotar a app com opções de certificado e runtime
- **Update Manifest Assets** — gerar automaticamente todos os ícones necessários a partir de uma imagem fonte
- **Generate / Install Certificate** — gestão de certificados de desenvolvimento
- **Sign Package** — assinar um MSIX ou executável
- **Run SDK Tool** — executar `makeappx`, `signtool`, `mt` ou `makepri` diretamente

Também não precisa de instalar o CLI do WinApp. Vem incluído com a extensão.

## Funciona com Múltiplos Frameworks

Não é apenas uma ferramenta para .NET WPF/WinUI. A extensão funciona com:

- **.NET**: WPF, WinForms, Console, WinUI 3
- **C/C++**: Win32, CMake, MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

Esta abrangência é deliberada. VS Code é onde vivem os desenvolvedores web e multiplataforma. Se está a construir uma app Tauri ou Electron que precisa de empacotamento Windows, esta extensão cobre-o sem ter de adotar o Visual Studio.

## Porque Importa para Desenvolvedores .NET

Trabalho muito no VS Code — é onde escrevo Markdown, giro configurações, edito projetos pequenos e executo terminais. Mas para trabalho de desktop Windows em .NET, o Visual Studio tem sido a única opção real quando se precisa de algo relacionado com empacotamento.

Esta extensão fecha essa lacuna. Agora pode ter um ciclo completo de desenvolvimento de desktop Windows em .NET — editar, compilar, executar com identidade de pacote, depurar, empacotar, assinar — sem sair do VS Code. É uma melhoria genuína de qualidade de vida.

## Primeiros Passos

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

Ou pesquise **WinApp** na vista de Extensões (`Ctrl+Shift+X`).

Requisitos:
- Windows 10 ou posterior
- VS Code 1.109.0 ou posterior
- A extensão de depurador para a linguagem da sua app

Leia o [anúncio completo de Chiara Mooney](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/) para mais detalhes.

## Conclusão

A extensão WinApp para VS Code é uma bem-vinda adição para desenvolvedores de desktop Windows em .NET que vivem no VS Code mas têm tido de mudar para o Visual Studio para trabalho de empacotamento. Identidade de pacote com F5, empacotamento MSIX a partir da paleta de comandos, gestão de certificados integrada — é o conjunto certo de funcionalidades.

Experimente no seu próximo projeto WPF ou WinUI. A fricção com que tem estado a lidar acabou de ficar muito menor.
