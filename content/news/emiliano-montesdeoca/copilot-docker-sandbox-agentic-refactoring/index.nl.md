---
title: "Docker Sandbox Laat Copilot-agents Code Refactoren Zonder Je Machine te Riskeren"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox geeft GitHub Copilot-agents een veilige microVM om vrij te refactoren — geen toestemmingsprompts, geen risico voor de host. Dit is waarom het alles verandert voor grootschalige .NET-modernisering."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Als je Copilots agentmodus hebt gebruikt voor iets meer dan kleine bewerkingen, ken je de pijn. Elke bestandsschrijfoperatie, elk terminalopdracht — weer een toestemmingsprompt.

Het Azure-team heeft zojuist een bericht gepubliceerd over [Docker Sandbox voor GitHub Copilot-agents](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/).

## Wat Docker Sandbox je eigenlijk geeft

Het basisidee is eenvoudig: een lichtgewicht microVM opstarten met een volledige Linux-omgeving, je werkruimte erin synchroniseren, en de Copilot-agent vrij laten opereren binnenin.

Dit is meer dan "dingen in een container draaien":
- **Bidirectionele werkruimtesynchronisatie** die absolute paden behoudt
- **Privé Docker-daemon** die in de microVM draait
- **HTTP/HTTPS-filterproxy's** die netwerktoegang beheren
- **YOLO-modus** — de agent draait zonder toestemmingsprompts

## Waarom .NET-ontwikkelaars dit moeten bijhouden

Met Docker Sandbox kun je een Copilot-agent op een project richten, het vrijelijk laten refactoren in de microVM, `dotnet build` en `dotnet test` uitvoeren om te valideren, en alleen wijzigingen accepteren die daadwerkelijk werken.

## Conclusie

Docker Sandbox lost de fundamentele spanning van agentic coding op: agents hebben vrijheid nodig om nuttig te zijn, maar vrijheid op je host-machine is gevaarlijk. MicroVM's geven je allebei.
