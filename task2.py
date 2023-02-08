from typing import Callable


def create_handler(callback: Callable[[int], None]) -> list:
    """
    Создает список из пяти анонимных функций, которые принимают
    аргумент callback и вызывают его с аргументом step.
    """
    print(type(callback))
    handlers = []
    for step in range(5):
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: list) -> None:
    """Вызывает функции из списка handlers."""
    for handler in handlers:
        handler()


def callback(step: int) -> None:
    """Выводит на экран аргументы анонимной функции."""
    print(step)


def main() -> None:
    """Главная функция, точка входа."""
    handlers = create_handler(callback)
    execute_handlers(handlers)


if __name__ == "__main__":
    main()
