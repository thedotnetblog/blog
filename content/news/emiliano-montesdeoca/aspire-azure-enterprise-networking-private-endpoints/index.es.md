---
title: "Endpoints Privados, VNets, NSGs — Aspire Gestiona la Red Ahora"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "El nuevo soporte de redes empresariales de Azure para Aspire permite modelar VNets, endpoints privados, puertas de enlace NAT, NSGs y perímetros de seguridad de red directamente en tu AppHost, sin deriva de infraestructura."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

He visto este escenario demasiadas veces. La aplicación está lista. La demo es excelente. Luego aparece la lista de verificación de seguridad: saca el almacenamiento de internet público, ejecuta dentro de una VNet, proporciona IPs de salida para la lista de autorización del socio, demuestra que solo las subredes correctas hablan con los servicios correctos.

En ese punto el modelo de aplicación y el modelo de infraestructura comienzan a divergir de maneras que son dolorosas de mantener.

El nuevo soporte de redes empresariales de Azure para Aspire aborda esto directamente. Describes la forma de la red junto a los recursos que la usan, en tu AppHost.

## Los Bloques de Construcción

Aquí está para qué sirve cada concepto de red de Azure, resumido:

| Característica | Úsala cuando | Por qué importa |
|---------|------------|----------------|
| Red virtual | Necesitas un espacio de direcciones privado | El límite de red para subredes, endpoints privados y enrutamiento |
| Subred | Necesitas separar cargas de trabajo dentro de la VNet | Cada parte del sistema obtiene su propio rango de direcciones y superficie de política |
| Subred delegada | Un servicio de plataforma (como ACA) necesita gestionar una subred | Permite que el servicio coloque infraestructura gestionada en tu VNet de forma segura |
| Puerta de enlace NAT | Necesitas IPs públicas de salida predecibles | Dirección estable para listas de autorización y auditoría |
| Endpoint privado | Quieres un recurso PaaS accesible privadamente | Pone una IP privada para ese servicio dentro de tu VNet, elimina la exposición pública |
| NSG | Necesitas reglas de tráfico a nivel de subred | Permitir/denegar explícito para tráfico entrante y saliente por subred |

## Describiéndolo en tu AppHost

El cambio clave aquí es que estás modelando la red *junto* a los recursos que la usan, no en un archivo Bicep separado que se aleja del modelo de aplicación con el tiempo.

Desde el AppHost, puedes:

- Crear VNets y subredes con `AddVirtualNetwork()` y `AddSubnet()`
- Adjuntar una puerta de enlace NAT a subredes para IPs de salida estables
- Crear endpoints privados para almacenamiento, Key Vault, SQL y otros servicios PaaS
- Definir NSGs con reglas de seguridad de entrada y salida
- Configurar Perímetros de Seguridad de Red para políticas entre recursos

El resultado es que cuando ejecutas `azd up`, la infraestructura coincide con lo que el modelo de aplicación dice que necesita. No lo que dice una plantilla mantenida manualmente.

## Por Qué Importa para Aplicaciones Reales

Algunas cosas que se vuelven significativamente más fáciles una vez que la red se modela en Aspire:

**Endpoints privados para Key Vault y almacenamiento** — describes `WithPrivateEndpoint()` en esos recursos, y Aspire maneja la configuración de zonas DNS y el adjunto de endpoints. La aplicación nunca cambia.

**IPs de salida consistentes** — agrega una puerta de enlace NAT a la subred relevante y cada solicitud de salida de tu aplicación pasa por una IP conocida y estable. Los socios pueden autorizarla. Los auditores pueden rastrearla.

**Reglas NSG desde el código** — en lugar de hacer clic en el portal o mantener un fragmento de Bicep, tus reglas de seguridad viven en el AppHost junto a los recursos que protegen.

Este es el tipo de integración que no hace que las demos sean emocionantes pero hace que los sistemas de producción sean mantenibles.

## Conclusión

La seguridad de red apareciendo tarde en el ciclo de vida del proyecto es un problema resuelto si la modelas junto con la aplicación desde el principio. El soporte de redes empresariales de Aspire hace eso posible sin requerir un seguimiento de infraestructura separado.

Detalles completos en la publicación original: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
