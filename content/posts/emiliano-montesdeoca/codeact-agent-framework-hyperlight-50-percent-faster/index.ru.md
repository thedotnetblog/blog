---
title: "CodeAct в Agent Framework: Как сократить задержку агента вдвое"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct сворачивает многошаговые цепочки инструментов в один изолированный блок кода — снижая задержку на 52% и использование токенов на 64%."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Эта статья была переведена автоматически. Для просмотра оригинала [нажмите здесь]({{< ref "index.md" >}}).*

В каждом проекте с агентами наступает момент, когда смотришь на трассировку и думаешь: «Почему это так долго работает?» Модель в порядке. Инструменты работают. Но для получения результата, который можно вычислить за один раз, происходит семь туров обмена данными.

Именно эту проблему решает CodeAct — и [команда Agent Framework только что выпустила альфа-поддержку](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) через новый пакет `agent-framework-hyperlight`.

## Что такое CodeAct?

[Паттерн CodeAct](https://arxiv.org/abs/2402.01030) элегантно прост: вместо того чтобы давать модели список инструментов для поочерёдного вызова, вы даёте ей единственный инструмент `execute_code` и позволяете выразить *весь план* как короткую программу на Python.

| Подход | Время | Токены |
|--------|------|--------|
| Традиционный | 27,81с | 6 890 |
| CodeAct | 13,23с | 2 489 |
| **Улучшение** | **52,4%** | **63,9%** |

## Безопасность: Микро-VM Hyperlight

Пакет `agent-framework-hyperlight` использует микро-VM [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Каждый вызов `execute_code` получает собственную свежесозданную микро-VM. Запуск измеряется в миллисекундах. Изоляция практически бесплатна.

Ваши инструменты продолжают работать на хосте. Сгенерированный моделью *связующий код* выполняется в песочнице. Это правильное разделение.

## Минимальная настройка

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## Когда использовать CodeAct (и когда не стоит)

**Используйте CodeAct, когда:**
- Задача включает много небольших вызовов инструментов (поиск, объединение, вычисления)
- Важны задержка и стоимость токенов
- Нужна надёжная изоляция для кода, генерируемого моделью

**Оставайтесь на традиционном вызове инструментов, когда:**
- Агент делает лишь один-два вызова за ход
- Каждый вызов имеет побочные эффекты, требующие индивидуального одобрения
- Описания инструментов скудны или неоднозначны

## Попробуйте сейчас

```bash
pip install agent-framework-hyperlight --pre
```

Читайте [полную статью в блоге Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) для углублённого изучения.
