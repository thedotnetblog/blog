---
title: "A avaliação de modernização do GitHub Copilot é a melhor ferramenta de migração que você ainda não está usando"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "A extensão de modernização do GitHub Copilot não sugere apenas mudanças de código — ela produz uma avaliação completa de migração com issues acionáveis, comparações de alvos Azure e um fluxo de trabalho colaborativo. Aqui explico por que o documento de avaliação é a chave de tudo."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "dotnet-modernization-assessment-github-copilot.md" >}}).*

Migrar uma aplicação legada do .NET Framework para .NET moderno é uma daquelas tarefas que todo mundo sabe que deveria fazer, mas ninguém quer começar. Nunca é apenas "mudar o target framework." São APIs que desapareceram, pacotes que não existem mais, modelos de hosting que funcionam de forma completamente diferente, e um milhão de pequenas decisões sobre o que containerizar, o que reescrever e o que deixar como está.

Jeffrey Fritz acabou de publicar um [mergulho profundo na avaliação de modernização do GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/), e honestamente? Este é o melhor tooling de migração que eu vi para .NET. Não pela geração de código — isso já é padrão agora. Pelo documento de avaliação que ele produz.

## Não é apenas um motor de sugestões de código

A extensão do VS Code segue um modelo de **Avaliar → Planejar → Executar**. A fase de avaliação analisa todo o seu codebase e produz um documento estruturado que captura tudo: o que precisa mudar, quais recursos Azure provisionar, qual modelo de deploy usar. Tudo que vem depois — infraestrutura como código, containerização, manifestos de deploy — flui do que a avaliação encontra.

A avaliação é armazenada em `.github/modernize/assessment/` no seu projeto. Cada execução produz um relatório independente, então você vai construindo um histórico e pode acompanhar como sua postura de migração evolui conforme corrige issues.

## Duas formas de começar

**Avaliação Recomendada** — o caminho rápido. Escolha entre domínios curados (Upgrade Java/.NET, Cloud Readiness, Segurança) e obtenha resultados significativos sem mexer em configuração. Ótimo para um primeiro olhar de onde sua aplicação está.

**Avaliação Personalizada** — o caminho direcionado. Configure exatamente o que analisar: compute alvo (App Service, AKS, Container Apps), SO alvo, análise de containerização. Escolha múltiplos alvos Azure para comparar abordagens de migração lado a lado.

Essa visão de comparação é genuinamente útil. Uma app com 3 issues obrigatórios para App Service pode ter 7 para AKS. Ver ambos ajuda a tomar a decisão de hosting antes de se comprometer com um caminho de migração.

## O detalhamento de issues é acionável

Cada issue vem com um nível de criticidade:

- **Obrigatório** — deve ser corrigido ou a migração falha
- **Potencial** — pode impactar a migração, precisa de julgamento humano
- **Opcional** — melhorias recomendadas, não bloqueiam a migração

E cada issue linka para arquivos afetados e números de linha, fornece uma descrição detalhada do que está errado e por que importa para sua plataforma alvo, dá passos concretos de remediação (não apenas "corrija isso"), e inclui links para documentação oficial.

Você pode atribuir issues individuais a desenvolvedores e eles têm tudo que precisam para agir. Essa é a diferença entre uma ferramenta que diz "tem um problema" e uma que diz como resolver.

## Os caminhos de upgrade cobertos

Para .NET especificamente:
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Cada caminho de upgrade tem regras de detecção que sabem quais APIs foram removidas, quais padrões não têm equivalente direto, e quais issues de segurança precisam de atenção.

Para times que gerenciam múltiplas aplicações, também há um CLI que suporta avaliações batch multi-repo — clone todos os repos, avalie todos, obtenha relatórios por app mais uma visão agregada do portfólio.

## Minha opinião

Se você está sentado em cima de aplicações legadas em .NET Framework (e vamos ser honestos, a maioria dos times enterprise está), esta é *a* ferramenta para começar. Só o documento de avaliação já vale o tempo — transforma um vago "deveríamos modernizar" em uma lista concreta e priorizada de itens de trabalho com caminhos claros adiante.

O fluxo de trabalho colaborativo também é inteligente: exporte avaliações, compartilhe com seu time, importe-as sem re-executar. Revisões de arquitetura onde quem toma decisões não é quem roda as ferramentas? Coberto.

## Finalizando

A avaliação de modernização do GitHub Copilot transforma a migração .NET de um projeto assustador e indefinido em um processo estruturado e rastreável. Comece com uma avaliação recomendada para ver onde você está, depois use avaliações personalizadas para comparar alvos Azure e construir seu plano de migração.

Leia o [walkthrough completo](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) e baixe a [extensão do VS Code](https://aka.ms/ghcp-appmod/vscode-ext) para testar no seu próprio codebase.
