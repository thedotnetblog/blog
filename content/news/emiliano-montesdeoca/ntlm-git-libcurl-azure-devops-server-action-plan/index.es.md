---
title: "NTLM termina en Git/libcurl: los equipos de Azure DevOps Server necesitan un plan de migración real"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "La eliminación de NTLM en septiembre de 2026 no es un problema menor de compatibilidad; es una fecha límite de arquitectura de identidad para entornos locales de Azure DevOps Server."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

La próxima eliminación de NTLM en libcurl es uno de esos cambios que parecen técnicos pero en realidad son organizativos. Si tu ruta de Git sobre HTTPS a Azure DevOps Server aún depende de NTLM, tu problema no son las herramientas, es la deuda de identidad.

Fuente original: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/