---
title: "VS Code 1.112: O que desenvolvedores .NET realmente deveriam se importar"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 acabou de sair e vem carregado com upgrades de agentes, um depurador de navegador integrado, sandboxing MCP e suporte a monorepos. Aqui está o que realmente importa se você desenvolve com .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 acabou de chegar, e honestamente? Este aqui bate diferente se você passa seus dias em território .NET. Tem muita coisa nas [notas de versão oficiais](https://code.visualstudio.com/updates/v1_112), mas deixe-me poupar alguma rolagem e focar no que realmente importa para nós.

## Copilot CLI ficou muito mais útil

O grande tema desta versão é a **autonomia do agente** — dar ao Copilot mais espaço para fazer seu trabalho sem você supervisionar cada passo.

### Direcionamento e fila de mensagens

Sabe aquele momento quando o Copilot CLI está no meio de uma tarefa e você percebe que esqueceu de mencionar algo? Antes, você tinha que esperar. Agora pode enviar mensagens enquanto uma requisição ainda está em andamento — seja para direcionar a resposta atual ou enfileirar instruções de acompanhamento.

Isso é enorme para aquelas tarefas mais longas de scaffolding `dotnet` onde você está assistindo o Copilot configurar um projeto e pensa "oh espera, também preciso de MassTransit ali".

### Níveis de permissão

Este é o que mais me empolga. Sessões do Copilot CLI agora suportam três níveis de permissão:

- **Permissões padrão** — o fluxo usual onde as ferramentas pedem confirmação antes de executar
- **Ignorar aprovações** — auto-aprova tudo e tenta novamente em erros
- **Autopiloto** — totalmente autônomo: aprova ferramentas, responde suas próprias perguntas e continua até a tarefa estar completa

Se você está fazendo algo como criar uma nova API ASP.NET Core com Entity Framework, migrations e setup Docker — o modo Autopiloto significa que você descreve o que quer e vai pegar um café. Ele vai resolver.

Você pode habilitar o Autopiloto com a configuração `chat.autopilot.enabled`.

### Pré-visualizar mudanças antes de delegar

Quando você delega uma tarefa ao Copilot CLI, ele cria um worktree. Antes, se você tivesse mudanças não commitadas, tinha que verificar o Controle de Código Fonte para ver o que seria afetado. Agora a visualização do Chat mostra as mudanças pendentes ali mesmo antes de você decidir se copia, move ou ignora.

Coisa pequena, mas salva você daquele momento de "espera, o que eu tinha no staging?".

## Depure apps web sem sair do VS Code

O navegador integrado agora suporta **depuração completa**. Você pode colocar breakpoints, fazer step through do código e inspecionar variáveis — tudo dentro do VS Code. Acabou o trocar para Edge DevTools.

Há um novo tipo de debug `editor-browser`, e se você já tem configurações de lançamento `msedge` ou `chrome` existentes, migrar é tão simples quanto mudar o campo `type` no seu `launch.json`:

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Para desenvolvedores Blazor, isso é um divisor de águas. Você já está executando `dotnet watch` no terminal — agora sua depuração fica na mesma janela também.

O navegador também ganhou níveis de zoom independentes (finalmente), menus de contexto com clique direito apropriados, e o zoom é lembrado por site.

## Sandboxing de servidores MCP

Isso importa mais do que você imagina. Se você está usando servidores MCP — talvez tenha configurado um personalizado para seus recursos Azure ou consultas de banco de dados — eles estavam rodando com as mesmas permissões do seu processo VS Code. Isso significa acesso total ao seu sistema de arquivos, rede, tudo.

Agora você pode colocá-los em sandbox. No seu `mcp.json`:

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Quando um servidor em sandbox precisa de acesso a algo que não tem, o VS Code solicita que você conceda permissão. Muito melhor que a abordagem de "torcer para ninguém fazer nada estranho".

> **Nota:** O sandboxing está disponível no macOS e Linux por enquanto. Suporte a Windows está vindo — cenários remotos como WSL funcionam porém.

## Descoberta de personalizações em monorepos

Se você trabalha em um monorepo (e sejamos honestos, muitas soluções .NET empresariais acabam virando um), isso resolve um ponto de dor real.

Anteriormente, se você abria uma subpasta do seu repositório, o VS Code não encontrava seu `copilot-instructions.md`, `AGENTS.md`, ou skills personalizados na raiz do repositório. Agora com a configuração `chat.useCustomizationsInParentRepositories`, ele sobe até a raiz `.git` e descobre tudo.

Isso significa que seu time pode compartilhar instruções de agente, arquivos de prompt e ferramentas personalizadas entre todos os projetos em um monorepo sem que todos precisem abrir a pasta raiz.

## /troubleshoot para depuração de agentes

Já configurou instruções personalizadas ou skills e se perguntou por que não estão sendo detectados? O novo skill `/troubleshoot` lê os logs de depuração do agente e te diz o que aconteceu — quais ferramentas foram usadas ou puladas, por que as instruções não carregaram, e o que está causando respostas lentas.

Habilite com:

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Então simplesmente digite `/troubleshoot why is my custom skill not loading?` no chat.

Você também pode exportar e importar esses logs de depuração agora, o que é ótimo para compartilhar com seu time quando algo não está funcionando como esperado.

## Suporte a arquivos de imagem e binários

Agentes agora podem ler arquivos de imagem do disco e arquivos binários nativamente. Os arquivos binários são apresentados em formato hexdump, e saídas de imagem (como capturas de tela do navegador integrado) aparecem em uma visualização de carrossel.

Para desenvolvedores .NET, pense: cole uma captura de tela de um bug de UI no chat e faça o agente entender o que está errado, ou faça-o analisar a saída de renderização de um componente Blazor.

## Referências automáticas de símbolos

Pequena melhoria de qualidade de vida: quando você copia o nome de um símbolo (uma classe, método, etc.) e cola no chat, o VS Code agora automaticamente converte em uma referência `#sym:Name`. Isso dá ao agente contexto completo sobre aquele símbolo sem você ter que adicioná-lo manualmente.

Se quiser texto puro, use `Ctrl+Shift+V`.

## Plugins agora podem ser habilitados/desabilitados

Anteriormente, desabilitar um servidor MCP ou plugin significava desinstalá-lo. Agora você pode ligá-los e desligá-los — tanto globalmente quanto por workspace. Clique direito na visualização de Extensões ou na visualização de Personalizações e pronto.

Plugins de npm e pypi também podem se auto-atualizar agora, embora peçam aprovação primeiro já que atualizações significam executar código novo na sua máquina.

## Para finalizar

VS Code 1.112 está claramente empurrando forte na experiência do agente — mais autonomia, melhor depuração, segurança mais apertada. Para desenvolvedores .NET, a depuração do navegador integrado e as melhorias do Copilot CLI são as funcionalidades destaque.

Se você ainda não experimentou rodar uma sessão completa do Copilot CLI em modo Autopiloto para um projeto .NET, esta versão é um bom momento para começar. Só lembre de configurar suas permissões e deixar cozinhar.

[Baixar VS Code 1.112](https://code.visualstudio.com/updates/v1_112) ou atualizar de dentro do VS Code via **Ajuda > Verificar Atualizações**.
