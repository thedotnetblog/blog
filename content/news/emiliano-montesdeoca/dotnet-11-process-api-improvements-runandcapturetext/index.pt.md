---
title: ".NET 11 finalmente corrige a API de Processos"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process recebe a sua maior atualização em anos. RunAndCaptureTextAsync, KillOnParentExit, APIs SafeProcessHandle e controlo total sobre o redirecionamento de handles padrão — sem mais boilerplate de deadlock."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Todo desenvolvedor .NET que alguma vez precisou lançar um processo e capturar a sua saída escreveu alguma variação do mesmo boilerplate perigoso: leitura async de stdout, leitura async de stderr, `WaitForExitAsync`, sem esquecer de drenar ambos os streams ou haverá um deadlock. É uma armadilha bem conhecida que existe há anos.

O .NET 11 finalmente resolve isto corretamente.

## RunAndCaptureTextAsync

A adição principal: um único método estático que inicia um processo, captura stdout e stderr, e aguarda a saída sem deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Uma única chamada. Sem drenagem manual de streams. Sem `WaitForExit` cuidadosamente posicionado. Se apenas precisas de executar algo e obter a sua saída, esta é a API que queres.

Existe também `Process.RunAsync` para o caso em que queres aguardar a saída sem capturar o output.

## KillOnParentExit

Um problema comum com processos lançados: se o processo pai falha ou é terminado, os processos filhos continuam a correr como órfãos. `KillOnParentExit` permite-te declarar no momento de iniciar o processo que o processo filho deve ser terminado quando o processo pai sair.

Esta é uma funcionalidade que existia de formas específicas da plataforma (job objects no Windows, prctl no Linux) mas exigia p/invoke ou bibliotecas de terceiros para ser usada a partir do .NET. Agora é uma propriedade de primeira classe em `ProcessStartInfo`.

## APIs Baseadas em SafeProcessHandle

A nova superfície de API leve é construída em torno de `SafeProcessHandle` em vez da classe `Process` completa. A classe `Process` completa carrega muito estado e é difícil de fazer trim — o caminho `SafeProcessHandle` é mais amigável ao trimmer para aplicações que precisam minimizar o tamanho de saída (WASM, AOT nativo).

## Controlo Total Sobre a Herança de Handles

A atualização também adiciona controlo granular sobre quais handles um processo filho herda e como os handles padrão são redirecionados. Anteriormente podias redirecionar stdin/stdout/stderr mas não podias especificar exatamente quais handles herdar ao nível do SO. As novas APIs expõem esse controlo.

## Porquê Isto Importa

A classe `Process` é usada em tooling, sistemas de build, executores de testes e qualquer aplicação que invoca outros executáveis. A antiga superfície de API datava do .NET Framework e estava a mostrar a sua idade. Não é uma mudança que quebra compatibilidade — as APIs antigas continuam a funcionar — mas o novo código deve preferir a nova superfície.

Para aplicações com trim ou cenários de compilação AOT, o caminho `SafeProcessHandle` é particularmente bem-vindo. A antiga classe `Process` trazia muito código pesado em reflexão que complicava o trimming.

Post original: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
