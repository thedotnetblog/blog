---
title: "Docker Sandbox lässt Copilot-Agenten euren Code refactoren — ohne Risiko für eure Maschine"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox gibt GitHub Copilot-Agenten eine sichere MicroVM zum freien Refactoring — keine Berechtigungsabfragen, kein Risiko für euren Host. Hier erfahrt ihr, warum das alles verändert für großangelegte .NET-Modernisierung."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Wer Copilots Agent-Modus für mehr als kleine Änderungen genutzt hat, kennt den Schmerz. Jeder Dateischreibvorgang, jeder Terminal-Befehl — wieder eine Berechtigungsabfrage. Jetzt stellt euch das mal bei 50 Projekten vor. Macht keinen Spaß.

Das Azure-Team hat gerade einen Beitrag über [Docker Sandbox für GitHub Copilot-Agenten](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/) veröffentlicht, und ehrlich gesagt ist das eine der praktischsten Verbesserungen für agentisches Tooling, die ich gesehen habe. Es nutzt MicroVMs, um Copilot eine vollständig isolierte Umgebung zu geben, in der er frei arbeiten kann — Pakete installieren, Builds ausführen, Tests laufen lassen — ohne euer Host-System zu berühren.

## Was Docker Sandbox tatsächlich bietet

Die Kernidee ist simpel: Eine leichtgewichtige MicroVM mit einer vollständigen Linux-Umgebung hochfahren, euren Workspace hineinsynchronisieren und den Copilot-Agenten frei darin arbeiten lassen. Wenn er fertig ist, werden die Änderungen zurücksynchronisiert.

Das macht es zu mehr als nur "Sachen in einem Container ausführen":

- **Bidirektionale Workspace-Synchronisation**, die absolute Pfade beibehält. Eure Projektstruktur sieht innerhalb der Sandbox identisch aus. Keine pfadbedingten Build-Fehler.
- **Privater Docker-Daemon** innerhalb der MicroVM. Der Agent kann Container bauen und ausführen, ohne jemals den Docker-Socket eures Hosts zu mounten. Das ist ein großer Sicherheitsgewinn.
- **HTTP/HTTPS-Filterproxys**, die kontrollieren, was der Agent im Netzwerk erreichen kann. Ihr entscheidet, welche Registries und Endpoints erlaubt sind. Supply-Chain-Angriffe durch ein fragwürdiges `npm install` in der Sandbox? Geblockt.
- **YOLO-Modus** — ja, so nennen sie das wirklich. Der Agent läuft ohne Berechtigungsabfragen, weil er buchstäblich euren Host nicht beschädigen kann. Jede destruktive Aktion ist eingedämmt.

## Warum .NET-Entwickler aufhorchen sollten

Denkt an die Modernisierungsarbeit, vor der so viele Teams gerade stehen. Ihr habt eine .NET-Framework-Solution mit 30 Projekten und müsst auf .NET 9 umsteigen. Das sind hunderte Dateiänderungen — Projektdateien, Namespace-Updates, API-Ersetzungen, NuGet-Migrationen.

Mit Docker Sandbox könnt ihr einen Copilot-Agenten auf ein Projekt ansetzen, ihn innerhalb der MicroVM frei refactoren lassen, `dotnet build` und `dotnet test` zur Validierung ausführen und nur die Änderungen übernehmen, die tatsächlich funktionieren. Kein Risiko, dass er versehentlich eure lokale Entwicklungsumgebung zerschießt, während er experimentiert.

Der Beitrag beschreibt auch den Einsatz einer **Flotte paralleler Agenten** — jeder in seiner eigenen Sandbox — die gleichzeitig verschiedene Projekte bearbeiten. Für große .NET-Solutions oder Microservice-Architekturen ist das eine massive Zeitersparnis. Ein Agent pro Service, alle isoliert laufend, alle unabhängig validiert.

## Der Sicherheitsaspekt zählt

Hier ist der Punkt, den die meisten übersehen: Wenn ihr einem KI-Agenten erlaubt, beliebige Befehle auszuführen, vertraut ihr ihm eure gesamte Maschine an. Docker Sandbox dreht dieses Modell um. Der Agent bekommt volle Autonomie in einer Wegwerfumgebung. Der Netzwerk-Proxy stellt sicher, dass er nur von genehmigten Quellen ziehen kann. Euer Host-Dateisystem, Docker-Daemon und eure Credentials bleiben unangetastet.

Für Teams mit Compliance-Anforderungen — und das sind die meisten .NET-Unternehmen — ist das der Unterschied zwischen "Wir können agentische KI nicht nutzen" und "Wir können sie sicher einsetzen."

## Fazit

Docker Sandbox löst die fundamentale Spannung des agentischen Programmierens: Agenten brauchen Freiheit, um nützlich zu sein, aber Freiheit auf eurer Host-Maschine ist gefährlich. MicroVMs geben euch beides. Wenn ihr großangelegtes .NET-Refactoring oder eine Modernisierung plant, lohnt es sich, das jetzt einzurichten. Die Kombination aus Copilots Code-Intelligenz mit einer sicheren Ausführungsumgebung ist genau das, worauf Produktionsteams gewartet haben.
