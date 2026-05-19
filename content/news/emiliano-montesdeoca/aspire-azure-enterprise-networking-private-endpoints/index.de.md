---
title: "Private Endpoints, VNets, NSGs — Aspire übernimmt jetzt das Netzwerk"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Der neue Azure-Unternehmensnetzwerk-Support für Aspire ermöglicht es, VNets, private Endpoints, NAT-Gateways, NSGs und Netzwerksicherheitsperimeter direkt im AppHost zu modellieren — ohne Infrastrukturdrift."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Ich habe dieses Szenario zu oft gesehen. Die App ist fertig. Die Demo ist großartig. Dann erscheint die Sicherheits-Checkliste: Speicher aus dem öffentlichen Internet nehmen, innerhalb eines VNets ausführen, ausgehende IPs für die Allowlist des Partners bereitstellen, nachweisen, dass nur die richtigen Subnetze mit den richtigen Diensten kommunizieren.

An diesem Punkt beginnen das Anwendungsmodell und das Infrastrukturmodell auseinanderzudriften, auf eine Art, die schmerzhaft zu pflegen ist.

Der neue Azure-Unternehmensnetzwerk-Support für Aspire adressiert dies direkt. Sie beschreiben die Netzwerkstruktur neben den Ressourcen, die sie verwenden, in Ihrem AppHost.

## Die Bausteine

Hier ist, wofür jedes Azure-Netzwerkkonzept verwendet wird, destilliert:

| Funktion | Verwenden Sie es wenn | Warum es wichtig ist |
|---------|------------|----------------|
| Virtuelles Netzwerk | Sie einen privaten Adressraum benötigen | Die Netzwerkgrenze für Subnetze, private Endpoints und Routing |
| Subnetz | Sie Workloads innerhalb des VNets trennen müssen | Jeder Teil des Systems erhält seinen eigenen Adressbereich und seine eigene Richtlinienoberfläche |
| Delegiertes Subnetz | Ein Plattformdienst (wie ACA) ein Subnetz verwalten muss | Ermöglicht dem Dienst, verwaltete Infrastruktur sicher in Ihrem VNet zu platzieren |
| NAT-Gateway | Sie vorhersagbare ausgehende öffentliche IPs benötigen | Stabile Adresse für Allowlists und Auditing |
| Privater Endpoint | Sie eine PaaS-Ressource privat erreichbar haben möchten | Platziert eine private IP für diesen Dienst in Ihrem VNet, entfernt öffentliche Exposition |
| NSG | Sie Regeln für Datenverkehr auf Subnetz-Ebene benötigen | Explizites Erlauben/Ablehnen für eingehenden und ausgehenden Datenverkehr pro Subnetz |

## Beschreibung im AppHost

Die wichtigste Änderung hier ist, dass Sie das Netzwerk *zusammen* mit den Ressourcen modellieren, die es verwenden, nicht in einer separaten Bicep-Datei, die mit der Zeit vom Anwendungsmodell abweicht.

Vom AppHost aus können Sie:

- VNets und Subnetze mit `AddVirtualNetwork()` und `AddSubnet()` erstellen
- Ein NAT-Gateway an Subnetze für stabile ausgehende IPs anhängen
- Private Endpoints für Speicher, Key Vault, SQL und andere PaaS-Dienste erstellen
- NSGs mit eingehenden und ausgehenden Sicherheitsregeln definieren
- Netzwerksicherheitsperimeter für ressourcenübergreifende Richtlinien konfigurieren

Das Ergebnis ist, dass wenn Sie `azd up` ausführen, die Infrastruktur mit dem übereinstimmt, was das Anwendungsmodell sagt, dass es benötigt. Nicht das, was eine manuell gepflegte Vorlage sagt.

## Warum das für echte Anwendungen wichtig ist

Einige Dinge, die erheblich einfacher werden, sobald das Netzwerk in Aspire modelliert ist:

**Private Endpoints für Key Vault und Speicher** — Sie beschreiben `WithPrivateEndpoint()` auf diesen Ressourcen, und Aspire übernimmt die DNS-Zonenkonfiguration und das Endpoint-Anhängen. Die App ändert sich nie.

**Konsistente ausgehende IPs** — fügen Sie ein NAT-Gateway zum entsprechenden Subnetz hinzu, und jede ausgehende Anfrage Ihrer App geht durch eine bekannte, stabile IP. Partner können sie allowlisten. Auditoren können sie nachverfolgen.

**NSG-Regeln aus Code** — anstatt durch das Portal zu klicken oder ein Bicep-Snippet zu pflegen, leben Ihre Sicherheitsregeln im AppHost neben den Ressourcen, die sie schützen.

Dies ist die Art von Integration, die Demos nicht aufregend macht, aber Produktionssysteme wartbar macht.

## Fazit

Netzwerksicherheit, die spät im Projektlebenszyklus auftaucht, ist ein gelöstes Problem, wenn Sie sie von Anfang an zusammen mit der App modellieren. Der Unternehmensnetzwerk-Support von Aspire macht das möglich, ohne eine separate Infrastruktur-Spur zu benötigen.

Vollständige Details im ursprünglichen Beitrag: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
