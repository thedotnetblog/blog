---
title: "Stop met databases als speciale sneeuwvlokken te behandelen: Azure DevOps + SQL Projects goed gedaan"
date: 2026-07-15
author: Emiliano Montesdeoca
description: "Het SQL projects-pijplijnmodel in Azure DevOps bewijst dat databaselevering herhaalbaar, veilig en testbaar kan zijn wanneer teams code-first CI/CD-discipline omarmen."
tags:
  - Azure DevOps
  - Azure SQL
  - CI/CD
  - SQL Projects
  - DevSecOps
  - Data Engineering
---

Veel teams beweren dat ze aan DevOps doen, en deployen vervolgens databasewijzigingen handmatig vanaf iemands laptop. Die tegenstrijdigheid is precies wat deze Azure SQL-richtlijn oplost. SQL projects plus Azure DevOps-pijplijnen maken databaselevering deterministisch, controleerbaar en veilig genoeg voor echte productieworkflows.

Oorspronkelijke bron: https://devblogs.microsoft.com/azure-sql/fundamentals-of-azure-devops-with-sql-projects/

Het sterkste onderdeel van de aanpak is niet de YAML-syntax, het is de disciplinevolgorde: eerst bouwen, dan publiceren, en het deploymentpad beveiligen met minimale privileges en wachtwoordloze identiteit. Het bouwen van een .sqlproj met dotnet valideert vroeg de compatibiliteit met het doelplatform en produceert een DACPAC-artefact dat door omgevingen kan worden gepromoveerd.

Mijn mening is eenvoudig: als je schema niet in CI wordt gebouwd, is je databasekwaliteitsproces vooral hoop. Lokaal succes in SSMS of VS Code is geen release-garantie.

Het deploymentontwerp is ook verfrissend pragmatisch. Gebruik serviceverbindingen gekoppeld aan Entra-identiteiten, verleen afgebakende databaserollen voor schema- en datavergelijking, en automatiseer tijdelijke firewallopeningen voor runner-IP's met gegarandeerde opruiming. Dit is het soort operationele hygiëne dat teams overslaan totdat een inbreukonderzoek hen dwingt alles te herzien.

Praktische aanbevelingen om direct toe te passen:

Splits build- en deploy-pijplijnen. Build zou moeten draaien bij branchwijzigingen en snel moeten falen. Deploy zou omgevingsspecifiek en beleidsgated moeten zijn. Bewaar doelverbindingsstrings en infrastructuurmetadata in beveiligde pijplijnvariabelen, en roteer governance-reviews voor rol-toewijzingen regelmatig. Houd ook SqlPackage-versies expliciet en gepind in CI om onverwachte gedragsveranderingen te voorkomen.

Overprivilegieer niet vroegtijdig. Beginnen met db_ddladmin, db_datareader en db_datawriter is een betere basislijn dan db_owner geven aan elke pijplijnprincipal "om het gewoon te laten werken". Escaleer alleen wanneer een concrete deploymentvereiste bewijst dat het nodig is.

Nog een sterke conclusie is portabiliteit. Omdat SQL projects draaien op de .NET SDK-toolchain, is dit patroon niet exclusief voor Azure DevOps. Dezelfde fundamenten vertalen zich naar GitHub Actions of andere orchestrators, wat deze richtlijn strategisch maakt, niet platformgebonden.

Als je organisatie schema-levering nog steeds behandelt als een speciaal proces buiten app-CI/CD, is dit je migratieblauwdruk. Je hebt geen heroïsche platform-engineering nodig. Je hebt consistentie nodig, identiteit-eerst-beveiliging en de bereidheid om te stoppen met het verzenden van databasewijzigingen via ad-hoc privilegepaden.

De teams die dit doen, zullen sneller leveren met minder rollback-events. De teams die uitstellen, blijven de verborgen belasting van handmatige data-plane-deployments betalen.
