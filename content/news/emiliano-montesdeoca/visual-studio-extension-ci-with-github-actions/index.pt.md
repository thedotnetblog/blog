---
title: 'Equipes de Extensão do Visual Studio Devem Parar de Lançar por Hábito e Começar a Lançar por Pipeline'
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: 'Um fluxo repetível do GitHub Actions para versionamento e publicação de VSIX agora é simples o suficiente para que etapas manuais de release sejam difíceis de justificar.'
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Fonte original: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Se você mantém extensões do Visual Studio e ainda executa partes significativas do release manualmente, este é seu sinal para modernizar.

O fluxo de trabalho mostrado neste post é intencionalmente prático: carimbar versão, construir, publicar artefatos de teste para uma galeria, depois publicar bits estáveis para o Marketplace. Sem cerimônia pesada de plataforma, apenas comportamento de release determinístico.

O que mais gosto é que o versionamento é tratado como estado de pipeline, não um item de checklist pré-release. Essa única decisão elimina um número surpreendente de erros: metadados incompatíveis, versões de assembly desatualizadas e notas de release inconsistentes.

A divisão entre publicação em galeria e publicação no Marketplace também é operacionalmente madura. Equipes precisam de um lugar para builds de validação rápidas que não carregam semântica de release oficial. Publicar tudo diretamente no Marketplace é de alto atrito e incentiva atalhos arriscados.

Um padrão de release forte para equipes de extensão é:

Em pull requests e commits na main, produza artefatos VSIX de CI e publique para a galeria para testadores.

Em releases marcados, publique pacotes assinados e validados para o Marketplace.

Mantenha o gerenciamento de tokens mínimo com segredos dedicados e escopos de privilégio mínimo.

Minha opinião: ecossistemas de extensão ficam atrás de ecossistemas de aplicativos em disciplina de CI porque equipes pequenas assumem que fluxos de trabalho manuais são gerenciáveis. Eles são gerenciáveis até não serem. Um patch apressado, um pacote quebrado, uma atualização de manifesto esquecida, e a confiança cai.

Essas ações reutilizáveis são úteis porque codificam a lógica de release repetida uma vez e permitem que as equipes se concentrem na qualidade da extensão em vez da mecânica de empacotamento.

Ainda é necessário julgamento de engenharia. Você deve proteger a publicação no Marketplace com verificações de qualidade, e deve tratar manifestos de publicação como artefatos de release auditados. Mas a complexidade básica do pipeline agora é baixa o suficiente para que releases exclusivamente manuais sejam principalmente dívida técnica.

Se você lidera desenvolvimento de extensões, padronize isso agora em todos os repositórios. Você obterá melhor rastreabilidade, integração mais fácil e menos gargalos de release de uma pessoa.

Implantação sugerida:

Comece com build mais publicação em galeria para uma extensão.

Introduza o carimbo de versão após validar suas convenções de fonte de manifesto.

Adicione a publicação no Marketplace somente após o gerenciamento de segredos e gates de release estarem em vigor.

Isso não é sobre seguir moda de DevOps. É sobre confiabilidade para as pessoas que instalam suas ferramentas e esperam que as atualizações funcionem.

Ecossistemas de extensão estáveis são construídos da mesma forma que aplicações estáveis: com automação repetitiva e chata que remove o trabalho de adivinhação humana.