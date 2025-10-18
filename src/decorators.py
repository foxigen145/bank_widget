import datetime
from functools import wraps
from typing import Any
from typing import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Если указан `filename`, записывает логи в указанный файл.
    Если не указан, выводит логи в консоль.

    Логирование включает:
    - имя функции и успешное завершение;
    - имя функции, тип ошибки и входные параметры, если выполнение завершилось с ошибкой.

    :param filename: Имя файла для записи логов (по умолчанию None — вывод в консоль).
    :return: Декоратор, оборачивающий функцию логированием.
    """
    def decorator(func: Callable) -> Callable:
        """
        Оборачивает функцию для добавления логирования при вызове.

        :param func: Целевая функция, которую нужно логировать.
        :return: Обёрнутая функция с логированием.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Выполняет функцию и логирует результат или ошибку.

            :param args: Позиционные аргументы функции.
            :param kwargs: Именованные аргументы функции.
            :return: Результат выполнения функции.
            """
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{datetime.datetime.now()} — {message}\n")
                else:
                    print(message)
                return result
            except Exception as error:
                error_message = (
                    f"{func.__name__} error: {type(error).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{datetime.datetime.now()} — {error_message}\n")
                else:
                    print(error_message)
                raise

        return wrapper
    return decorator
