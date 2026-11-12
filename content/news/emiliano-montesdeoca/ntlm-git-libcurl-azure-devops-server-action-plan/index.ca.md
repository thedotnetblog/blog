---
title: "NTLM S'acaba a Git/libcurl: Els Equips d'Azure DevOps Server Necessiten un Pla de Migració Real"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "L'eliminació de NTLM al setembre de 2026 no és un problema menor de compatibilitat; és una data límit d'arquitectura d'identitat per a entorns d'Azure DevOps Server on-premises."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

L'eliminació de NTLM a libcurl és un d'aquells canvis que sembla tècnic però que en realitat és organitzatiu. Si el vostre camí de Git sobre HTTPS a Azure DevOps Server encara depèn de NTLM, el vostre problema no és d'eines, és de deute d'identitat.

Font original: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft fa bé d'empènyer amb fermesa aquí. NTLM té debilitats criptogràfiques conegudes i no hauria de ser un valor predeterminat empresarial modern. La part perillosa és que molts entorns creuen que estan utilitzant Kerberos quan en realitat estan sobrevivint amb una fallada silenciosa de SPNEGO a NTLM. Aquesta il·lusió desapareix al setembre de 2026.

La meva opinió: no tracteu això com un problema de "versió del client." Rehabilitar les banderes de NTLM, fixar builds antics de Git o esperar que la fallada romangui disponible és una solució temporal de curta durada amb risc a llarg termini. Si la vostra estratègia de remediació és degradar i retardar, esteu augmentant activament la fragilitat operativa.

Una seqüència de migració pràctica hauria de ser directa i mesurable.

Primer, verifiqueu el comportament d'autenticació actual ara. Executeu comprovacions basades en traces i validació de la cau de tiquets en contextos reals de desenvolupadors i agents de compilació, incloent camins fora de domini i de xarxa remota. Segon, corregiu Kerberos de punta a punta: SPNs, àlies DNS, configuració del balancejador de càrrega, delegació i accessibilitat del controlador de domini. Tercer, identifiqueu els escenaris no units a domini o de grup de treball aviat i dissenyeu un carril SSH on Kerberos no es pugui fer fiable.

També necessiteu claredat de propietat. Els equips de seguretat haurien de definir les línies base de política, però l'enginyeria de plataforma ha de tenir la responsabilitat de la implementació. Això no pot ser una tasca secundària per a administradors de repositori individuals. Requereix canvis coordinats a través d'IIS, AD, la vora de xarxa, els agents de CI i la guia per a estacions de treball de desenvolupadors.

Un risc subtil és l'automatització. Els agents de compilació i els comptes de servei sovint s'executen en contextos on els tiquets Kerberos falten o són invàlids, fins i tot quan els usuaris humans estan bé. Si només proveu fluxos de treball de desenvolupadors interactius, us perdreu els punts de trencament més crítics.

La part positiva és real. Moure's netament a Kerberos o SSH no només evita la ruptura, sinó que redueix la superfície d'atac i alinea els controls d'identitat amb les expectatives de compliment modernes. Els equips que comencin aquesta transició ara tractaran setembre com un no-esdeveniment. Els equips que esperin estaran depurant fallades d'autenticació sota pressió de llançament.

Això no és un avís per arxivar. És una data límit contra la qual executar.