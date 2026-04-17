---
title: "Docker Sandbox permite a los agentes de Copilot refactorizar tu código sin poner en riesgo tu máquina"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox ofrece a los agentes de GitHub Copilot una microVM segura donde pueden refactorizar sin límites — sin prompts de permisos, sin riesgos para tu host. Así es como esto cambia todo para la modernización de .NET a gran escala."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "copilot-docker-sandbox-agentic-refactoring" >}}).*

Si usaste el modo agente de Copilot para algo más que ediciones pequeñas, conocés el dolor. Cada escritura de archivo, cada comando en terminal — otro prompt de permisos. Ahora imaginá eso multiplicado por 50 proyectos. No es divertido.

El equipo de Azure acaba de publicar un post sobre [Docker Sandbox para agentes de GitHub Copilot](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/), y honestamente, es una de las mejoras más prácticas que he visto en herramientas agénticas. Usa microVMs para darle a Copilot un entorno completamente aislado donde puede hacer de todo — instalar paquetes, ejecutar builds, correr tests — sin tocar tu sistema host.

## Qué te da realmente Docker Sandbox

La idea central es simple: levantar una microVM liviana con un entorno Linux completo, sincronizar tu workspace dentro de ella, y dejar que el agente de Copilot opere libremente adentro. Cuando termina, los cambios se sincronizan de vuelta.

Esto es lo que lo hace más que simplemente "ejecutar cosas en un contenedor":

- **Sincronización bidireccional del workspace** que preserva rutas absolutas. La estructura de tu proyecto se ve idéntica dentro del sandbox. Sin fallos de build por rutas.
- **Docker daemon privado** corriendo dentro de la microVM. El agente puede construir y ejecutar contenedores sin montar jamás el socket de Docker de tu host. Eso es importante para la seguridad.
- **Proxies de filtrado HTTP/HTTPS** que controlan lo que el agente puede alcanzar en la red. Vos decidís qué registries y endpoints están permitidos. ¿Ataques a la cadena de suministro por un `npm install` malicioso dentro del sandbox? Bloqueados.
- **Modo YOLO** — sí, así lo llaman. El agente corre sin prompts de permisos porque literalmente no puede dañar tu host. Toda acción destructiva está contenida.

## Por qué los desarrolladores .NET deberían prestar atención

Pensá en el trabajo de modernización que tantos equipos están enfrentando ahora mismo. Tenés una solución .NET Framework con 30 proyectos, y necesitás moverla a .NET 9. Son cientos de cambios en archivos — archivos de proyecto, actualizaciones de namespaces, reemplazos de APIs, migraciones de NuGet.

Con Docker Sandbox, podés apuntar un agente de Copilot a un proyecto, dejarlo refactorizar libremente dentro de la microVM, ejecutar `dotnet build` y `dotnet test` para validar, y solo aceptar los cambios que realmente funcionan. Sin riesgo de que accidentalmente destruya tu entorno de desarrollo local mientras experimenta.

El post también describe ejecutar una **flota de agentes en paralelo** — cada uno en su propio sandbox — trabajando en diferentes proyectos simultáneamente. Para soluciones .NET grandes o arquitecturas de microservicios, eso ahorra una cantidad enorme de tiempo. Un agente por servicio, todos corriendo aislados, todos validados independientemente.

## El ángulo de seguridad importa

Acá está lo que la mayoría pasa por alto: cuando dejás que un agente de IA ejecute comandos arbitrarios, le estás confiando toda tu máquina. Docker Sandbox invierte ese modelo. El agente tiene autonomía total dentro de un entorno desechable. El proxy de red asegura que solo pueda descargar de fuentes aprobadas. Tu filesystem host, tu Docker daemon y tus credenciales quedan intactos.

Para equipos con requisitos de compliance — y eso es la mayoría de las empresas .NET — esta es la diferencia entre "no podemos usar IA agéntica" y "podemos adoptarla de forma segura".

## Conclusión

Docker Sandbox resuelve la tensión fundamental de la programación agéntica: los agentes necesitan libertad para ser útiles, pero libertad en tu máquina host es peligroso. Las microVMs te dan ambas cosas. Si estás planificando cualquier refactorización o modernización de .NET a gran escala, vale la pena configurar esto ahora. La combinación de la inteligencia de código de Copilot con un entorno de ejecución seguro es exactamente lo que los equipos de producción estaban esperando.
