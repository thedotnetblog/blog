---
title: "NTLM verdwijnt in Git/libcurl: Azure DevOps Server-teams hebben een echt migratieplan nodig"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "De verwijdering van NTLM in september 2026 is geen klein compatibiliteitsprobleem; het is een identiteitsarchitectuurdeadline voor on-prem Azure DevOps Server-omgevingen."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

De aankomende NTLM-verwijdering in libcurl is een van die veranderingen die technisch oogt maar eigenlijk organisatorisch is. Als je Git-over-HTTPS-pad naar Azure DevOps Server nog steeds afhankelijk is van NTLM, is je probleem geen tooling, het is identiteitsschuld.

Oorspronkelijke bron: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft doet er goed aan hier hard op te duwen. NTLM heeft bekende cryptografische zwakheden en zou geen moderne enterprise-standaard moeten zijn. Het gevaarlijke deel is dat veel omgevingen geloven dat ze Kerberos gebruiken terwijl ze eigenlijk overleven op stille SPNEGO-terugval naar NTLM. Die illusie verdwijnt in september 2026.

Mijn mening: behandel dit niet als een "clientversie"-probleem. NTLM-vlaggen opnieuw inschakelen, oude Git-builds vastpinnen, of hopen dat fallback beschikbaar blijft, is een kortstondige workaround met langetermijnrisico. Als je herstelstrategie downgrade-en-uitstellen is, verhoog je actief de operationele broosheid.

Een praktische migratievolgorde zou bot en meetbaar moeten zijn.

Verifieer eerst het huidige authenticatiegedrag nu. Voer trace-gebaseerde controles en ticket cache-validatie uit in echte ontwikkelaars- en build-agentcontexten, inclusief off-domain- en remote-netwerkpaden. Fix ten tweede Kerberos end-to-end: SPN's, DNS-aliassen, load balancer-instellingen, delegatie en bereikbaarheid van domeincontrollers. Identificeer ten derde vroeg scenario's zonder domeinlidmaatschap of workgroup-scenario's en ontwerp een SSH-baan waar Kerberos niet betrouwbaar gemaakt kan worden.

Je hebt ook duidelijkheid over eigenaarschap nodig. Beveiligingsteams zouden beleidsbasislijnen moeten definiëren, maar platform-engineering moet implementatiegereedheid bezitten. Dit kan geen bijtaak zijn voor individuele repo-beheerders. Het vereist gecoördineerde veranderingen over IIS, AD, netwerkrand, CI-agents en richtlijnen voor ontwikkelaarswerkstations.

Eén subtiel risico is automatisering. Build-agents en serviceaccounts draaien vaak in contexten waar Kerberos-tickets ontbreken of ongeldig zijn, zelfs wanneer menselijke gebruikers prima functioneren. Als je alleen interactieve ontwikkelaarsworkflows test, mis je de meest kritieke breekpunten.

De opbrengst is reëel. Schoon overstappen naar Kerberos of SSH voorkomt niet alleen storingen, het vermindert ook het aanvalsoppervlak en stemt identiteitscontroles af op moderne compliance-verwachtingen. De teams die nu met deze overgang beginnen, zullen september als een non-event behandelen. De teams die wachten, zullen authenticatiefouten debuggen onder releasedruk.

Dit is geen waarschuwing om te archiveren. Het is een deadline om tegen te presteren.
