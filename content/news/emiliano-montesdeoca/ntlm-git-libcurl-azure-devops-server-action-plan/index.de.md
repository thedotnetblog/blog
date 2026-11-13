---
title: "NTLM Endet In Git/libcurl: Azure DevOps Server-Teams Brauchen Einen Echten Migrationsplan"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "Die NTLM-Entfernung im September 2026 ist kein geringes Kompatibilitätsproblem; es ist eine Identitätsarchitektur-Frist für lokale Azure DevOps Server-Umgebungen."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

Die bevorstehende NTLM-Entfernung in libcurl ist eine dieser Änderungen, die technisch aussehen, aber tatsächlich organisatorisch sind. Wenn Ihr Git-over-HTTPS-Pfad zu Azure DevOps Server immer noch von NTLM abhängt, ist Ihr Problem nicht Tooling, es ist Identitätsschulden.

Originalquelle: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft hat recht, hier hart vorzugehen. NTLM hat bekannte kryptografische Schwächen und sollte kein moderner Enterprise-Standard sein. Der gefährliche Teil ist, dass viele Umgebungen glauben, sie verwenden Kerberos, wenn sie tatsächlich nur durch stillen SPNEGO-Fallback auf NTLM überleben. Diese Illusion verschwindet im September 2026.

Meine Meinung: Behandeln Sie dies nicht als "Client-Version"-Problem. Das erneute Aktivieren von NTLM-Flags, das Fixieren alter Git-Builds oder die Hoffnung, dass der Fallback verfügbar bleibt, ist ein kurzlebiger Workaround mit langfristigem Risiko. Wenn Ihre Abhilfestrategie Downgrade-und-Verzögern ist, erhöhen Sie aktiv die operative Fragilität.

Eine praktische Migrationssequenz sollte direkt und messbar sein.