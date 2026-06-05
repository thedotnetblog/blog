---
title: "Agent Skills no Visual Studio: Ensine o Copilot Como Seu Time Realmente Trabalha"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "O Visual Studio agora suporta Agent Skills — conjuntos de instruções reutilizáveis que ensinam ao Copilot os fluxos de trabalho, padrões de código e convenções específicos do seu time. Defina uma vez, aplique automaticamente."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Uma das frustrações persistentes com assistentes de codificação de IA: eles conhecem bem a programação geral, mas não conhecem as convenções específicas do *seu* time, suas APIs internas ou seus padrões preferidos. Em cada sessão, você reexplica o contexto. Agent Skills no Visual Studio foi projetado para resolver isso.

## O que São os Agent Skills

Conjuntos de instruções reutilizáveis — definidos em arquivos `SKILL.md` — que ensinam os agentes do Copilot como lidar com tarefas específicas. Defina um skill para "como executar nosso pipeline de build", "como gerar boilerplate para nossa camada de serviço" ou "nossa checklist de revisão de código". O agente aplica o skill automaticamente quando é relevante.

Isso não é um conceito novo (`.github/copilot-instructions.md` existe há um tempo), mas a integração do Visual Studio os torna objetos de primeira classe com uma interface de descoberta.

## Criação de Skills no Visual Studio

O fluxo de interface integrado: clique no ícone de ferramentas no Copilot Chat, abra o painel de skills, clique em `+`. Você escolhe o escopo global (pessoal) ou de solução, escolhe um nome e o Visual Studio gera um template. O modo Agente do Copilot pode então ajudá-lo a preencher o template — use o agente para escrever o skill para o agente.

Atualmente no canal Insiders, em breve disponível na versão Release.

Você também pode criar skills manualmente:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Locais de Descoberta

Os skills são auto-descobertos a partir de caminhos padrão:

**Nível de solução (compartilhado via repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/pessoal (seu perfil de usuário, disponível em todos os lugares):** `~/.copilot/skills/`, `~/.agents/skills/`

O suporte multi-localização significa que a mesma convenção funciona com GitHub Copilot, Claude Code e outros frameworks de agentes — defina seus skills uma vez, use-os em todos os lugares.

## O Formato

Os skills seguem o formato [agentskills.io/specification](https://agentskills.io/specification) — uma especificação baseada em Markdown que é legível tanto por humanos quanto por máquinas. Você pode incluir scripts, templates e exemplos ao lado do `SKILL.md`.

## Valor Prático

O poder real não está nas funcionalidades individuais — está na combinação de skills compartilhados pelo time (via `.github/skills/`) e skills pessoais (via `~/.agents/skills/`). Os skills do time codificam como sua organização faz as coisas. Os skills pessoais codificam como você especificamente trabalha. O agente obtém ambos os contextos automaticamente.

Para organizações que já usam o Copilot intensamente, este é um passo significativo para tornar a ferramenta verdadeiramente ciente das convenções específicas do seu codebase em vez de dar conselhos genéricos.

Post original: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
