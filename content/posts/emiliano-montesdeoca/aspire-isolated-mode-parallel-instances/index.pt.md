---
title: "O Modo Isolado do Aspire Resolve o Pesadelo de Conflitos de Porta no Desenvolvimento Paralelo"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 introduz o modo --isolated: portas aleatórias, segredos separados e zero colisões ao executar múltiplas instâncias do mesmo AppHost. Perfeito para agentes de IA, worktrees e fluxos de trabalho paralelos."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Se você já tentou executar duas instâncias do mesmo projeto ao mesmo tempo, conhece a dor. A porta 8080 já está em uso. A porta 17370 está ocupada. Matar algo, reiniciar, fazer malabarismo com variáveis de ambiente — é um assassino de produtividade.

Esse problema está piorando, não melhorando. Agentes de IA criam git worktrees para trabalhar de forma independente. Agentes em segundo plano criam ambientes separados. Desenvolvedores fazem checkout do mesmo repo duas vezes para branches de funcionalidades. Cada um desses cenários bate na mesma parede: duas instâncias da mesma app brigando pelas mesmas portas.

Aspire 13.2 resolve isso com um único flag. James Newton-King do time do Aspire [escreveu todos os detalhes](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), e é uma daquelas funcionalidades "por que não tínhamos isso antes?"

## A solução: `--isolated`

```bash
aspire run --isolated
```

Isso é tudo. Cada execução recebe:

- **Portas aleatórias** — sem mais colisões entre instâncias
- **Segredos de usuário isolados** — connection strings e chaves API ficam separadas por instância

Sem reatribuição manual de portas. Sem malabarismo de variáveis de ambiente. Cada execução recebe um ambiente limpo e livre de colisões automaticamente.

## Cenários reais onde isso brilha

**Múltiplos checkouts.** Você tem uma branch de funcionalidade em um diretório e um bugfix em outro:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Ambos rodam sem conflitos. O dashboard mostra o que está rodando e onde.

**Agentes em segundo plano no VS Code.** Quando o agente em background do Copilot Chat cria um git worktree para trabalhar no seu código de forma independente, ele pode precisar executar seu AppHost do Aspire. Sem `--isolated`, isso é uma colisão de porta com seu worktree principal. Com ele, ambas instâncias simplesmente funcionam.

O skill do Aspire que vem com `aspire agent init` instrui automaticamente os agentes a usar `--isolated` quando trabalhando em worktrees. Então o agente em background do Copilot deve lidar com isso nativamente.

**Testes de integração junto ao desenvolvimento.** Precisa rodar testes contra um AppHost ao vivo enquanto continua construindo funcionalidades? O modo isolado dá a cada contexto suas próprias portas e configuração.

## Como funciona internamente

Quando você passa `--isolated`, a CLI gera um ID de instância único para a execução. Isso aciona dois comportamentos:

1. **Randomização de portas** — em vez de vincular a portas previsíveis definidas na configuração do seu AppHost, o modo isolado escolhe portas aleatórias disponíveis para tudo — o dashboard, endpoints de serviço, tudo. O service discovery se ajusta automaticamente, então os serviços se encontram independentemente de quais portas foram atribuídas.

2. **Isolamento de segredos** — cada execução isolada recebe seu próprio armazenamento de user secrets, indexado pelo ID da instância. Connection strings e chaves API de uma execução não vazam para outra.

Seu código não precisa de mudanças. O service discovery do Aspire resolve endpoints em tempo de execução, então tudo se conecta corretamente independentemente da atribuição de portas.

## Quando usar

Use `--isolated` quando executar múltiplas instâncias do mesmo AppHost simultaneamente — seja desenvolvimento paralelo, testes automatizados, agentes de IA ou git worktrees. Para desenvolvimento de instância única onde você prefere portas previsíveis, o `aspire run` regular continua funcionando bem.

## Concluindo

O modo isolado é uma funcionalidade pequena que resolve um problema real e cada vez mais comum. À medida que o desenvolvimento assistido por IA nos empurra para mais fluxos paralelos — múltiplos agentes, múltiplos worktrees, múltiplos contextos — a capacidade de simplesmente subir outra instância sem brigar por portas é essencial.

Leia o [post completo](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) para todos os detalhes técnicos e experimente com `aspire update --self` para obter a 13.2.
