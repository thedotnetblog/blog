---
title: "La Veritable Frontera per al SQL Agèntic: Auditabilitat amb OBO al SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "L'autenticació On-Behalf-Of a Data API builder més SQL MCP Server és una fita important de governança perquè Azure SQL finalment pot auditar l'humà darrere d'una acció d'agent."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Hi ha una veritat dolorosa en els projectes d'IA empresarial: molts equips s'obsessionen amb la qualitat del model i ignoren la responsabilitat. Quan un agent escriu o llegeix dades de producció, la primera pregunta de la revisió d'incidents no és "la resposta era bona?" És "qui va fer això realment?"

Font original: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

Per això el suport OBO a Data API builder 2.0 amb SQL MCP Server és més important del que sembla. Els enfocaments de nom d'usuari/contrasenya i identitat gestionada encara funcionen operativament, però tots dos col·lapsen la identitat dins del límit del servei. Els logs mostren l'aplicació o el middleware, no l'origen de la sol·licitud humana. Això és acceptable per a automatització simple. No ho és per a fluxos de treball agèntics regulats.

Amb OBO, SQL autentica el context d'usuari delegat, no la identitat de l'amfitrió de l'eina. Això us dóna un model d'auditoria fonamentalment millor: principal d'usuari, acció, context de declaració i identificador d'aplicació de nivell mitjà junts. Obteniu traçabilitat sense perdre la superfície de control de les eines MCP i els permisos d'entitat DAB.

La meva opinió és ferma aquí: si el vostre agent pot tocar dades SQL sensibles, OBO hauria de ser la vostra arquitectura predeterminada, no una tasca d'enduriment opcional. La configuració és més complexa, però el deute d'identitat sempre es paga després, normalment durant incidents de seguretat, auditories de compliment o escalades executives.

Guia d'implementació pràctica:

Comenceu validant el flux d'identitat amb una vista "WhoAmI" mínima i comprovacions automatitzades en tests d'integració. Si el principal de SQL no coincideix amb l'usuari autenticat, atureu-vos i arregleu-ho abans d'enviar. Després, connecteu consultes de Log Analytics per a SQLSecurityAuditEvents als vostres dashboards de SOC i alerteu sobre accions d'alt risc iniciades a través de camins OBO. Finalment, alineeu RBAC i permisos DAB perquè la identitat a nivell d'usuari i l'autorització a nivell d'acció es mantinguin consistents de punta a punta.

Un punt de disseny subtil però important de l'anunci és el comportament de la memòria cau. DAB bloqueja explícitament la memòria cau de respostes quan l'auth delegada d'usuari està habilitada. Aquesta compensació és correcta. Els trucs de rendiment que poden filtrar resultats amb àmbit d'usuari no valen la pena en entorns multi-tenant o regulats.

SQL MCP Server més OBO és el començament d'un patró madur: agents com a operadors controlats, usuaris com a principals responsables, plans de dades com a sistemes auditables. Si la vostra arquitectura no pot respondre "qui va fer això" amb confiança, no és IA preparada per a producció, per molt polida que sembli la demo.