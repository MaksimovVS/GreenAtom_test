# Тестовые задания от GreenAtom

Необходимо клонировать репозиторий, создать и активировать виртуальное окружение и установить зависимости.

```bash
git clone git@github.com:MaksimovVS/GreenAtom_test.git

# windows
python -m venv venv
source venv/Scripts/activate 
# linux
python3 -m venv venv
source venv/bin/activate 

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 1 задание

_Какие шаги следует предпринять, если пользователь сообщит о том, что API возвращает ему ошибку 500?_

[Решение](tasks/task1.md)

## 2 задание

_Какие проблемы в следующем фрагменте кода? Как его следует исправить? Необходимо исправить ошибку и переписать код ниже с использованием типизации_

```python
def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()
```

[Решение](tasks/task2.py)


## 3 задание

_Сколько HTML-тегов в коде главной страницы сайта [greenatom.ru](https://greenatom.ru/)? Сколько из них содержит атрибуты? Необходимо написать скрипт на Python, который выводит ответы на вопросы выше._

[Решение](tasks/task3.py)


## 4 задание

_Написать функцию на Python, которая возвращает текущий публичный IP-адрес компьютера с использованием сервиса [ifconfig.me](https://ifconfig.me/)_

[Решение](tasks/task4.py)


## 5 задание

_Написать функцию на Python, выполняющую сравнение версий по условиям ниже._

```
- Return -1 if version A is older than version B
- Return 0 if versions A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.
```

[Решение](tasks/task5.py)

#### Backend developer

[Владмир Максимов](https://github.com/MaksimovVS) @MaksimovVS
