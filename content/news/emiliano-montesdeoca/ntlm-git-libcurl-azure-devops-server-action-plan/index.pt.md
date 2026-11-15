---
title: "NTLM Está Chegando ao Fim no Git/libcurl: Equipes do Azure DevOps Server Precisam de um Plano de Migração de Verdade"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "A remoção do NTLM em setembro de 2026 não é um problema menor de compatibilidade; é um prazo de arquitetura de identidade para ambientes on-premises do Azure DevOps Server."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

A próxima remoção do NTLM no libcurl é uma daquelas mudanças que parecem técnicas, mas na verdade são organizacionais. Se o seu caminho de Git sobre HTTPS até o Azure DevOps Server ainda depende do NTLM, seu problema não é ferramental, é dívida de identidade.

Fonte original: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

A Microsoft está certa em pressionar forte aqui. O NTLM tem fraquezas criptográficas conhecidas e não deveria ser um padrão corporativo moderno. A parte perigosa é que muitos ambientes acreditam estar usando Kerberos quando, na verdade, estão sobrevivendo com um fallback silencioso do SPNEGO para NTLM. Essa ilusão desaparece em setembro de 2026.

Minha opinião: não trate isso como um problema de "versão de cliente". Reativar flags de NTLM, fixar builds antigos do Git ou torcer para que o fallback continue disponível é uma solução paliativa de curta duração com risco de longo prazo. Se sua estratégia de remediação é fazer downgrade e adiar, você está aumentando ativamente a fragilidade operacional.

Uma sequência prática de migração deveria ser direta e mensurável.

Primeiro, verifique o comportamento de autenticação atual agora. Rode verificações baseadas em trace e validação de cache de tickets em contextos reais de desenvolvedores e agentes de build, incluindo caminhos fora do domínio e de rede remota. Segundo, corrija o Kerberos de ponta a ponta: SPNs, aliases de DNS, configurações de balanceador de carga, delegação e acessibilidade dos controladores de domínio. Terceiro, identifique cedo cenários de workgroup ou não ingressados no domínio e projete uma via SSH onde o Kerberos não puder ser tornado confiável.

Você também precisa de clareza de responsabilidade. As equipes de segurança deveriam definir as linhas de base de política, mas a engenharia de plataforma precisa ser dona da prontidão de implementação. Isso não pode ser uma tarefa secundária de administradores individuais de repositório. Requer mudanças coordenadas em IIS, AD, borda de rede, agentes de CI e orientação para estações de trabalho de desenvolvedores.

Um risco sutil é a automação. Agentes de build e contas de serviço frequentemente rodam em contextos onde os tickets Kerberos estão ausentes ou inválidos, mesmo quando os usuários humanos estão bem. Se você só testar fluxos interativos de desenvolvedores, vai perder os pontos de ruptura mais críticos.

O lado positivo é real. Migrar de forma limpa para Kerberos ou SSH não só evita quebras, como também reduz a superfície de ataque e alinha os controles de identidade com expectativas modernas de conformidade. As equipes que começarem essa transição agora vão tratar setembro como um não-evento. As equipes que esperarem vão estar depurando falhas de autenticação sob pressão de release.

Este não é um aviso para arquivar. É um prazo para executar.
