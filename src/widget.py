"""Функции для работы с отображением карточек/счетов и дат в виджете."""

from datetime import datetime
from typing import Tuple

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def _split_name_and_number(info: str) -> Tuple[str, str]:
    """
    Вспомогательная функция: разбивает исходную строку на "имя" (тип карты/счета) и "номер".

    Берёт последний "токен" как номер, а всё остальное — имя.

    Args:
        info (str): строка вида '<Имя> <Номер>', например,
                    'Visa Classic 1234567890123456' или 'Счет 73654108430135874305'.

    Returns:
        Tuple[str, str]: кортеж (name, number), где name — тип карты/счета, number — номер.

    Raises:
        ValueError: если строка не содержит хотя бы два слова.
    """
    parts = info.strip().split()
    if len(parts) < 2:
        raise ValueError(
            "Ожидается строка вида '<Имя> <Номер>' " "(например, 'Visa Classic 1234...' или 'Счет 1234...')."
        )
    name = " ".join(parts[:-1])
    number = parts[-1]
    return name, number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета, оставляя видимыми только первые и последние цифры.

    Использует ранее реализованные функции маскировки из модуля `masks`.

    Args:
        info (str): строка с типом и номером карты/счета, например:
                    'Visa Platinum 7000792289606361' или 'Счет 73654108430135874305'.

    Returns:
        str: строка с замаскированным номером карты или счета, например:
             'Visa Platinum 7000 79** **** 6361' или 'Счет **4305'.
    """
    name, number = _split_name_and_number(info)

    first_word = name.split()[0].lower()
    if first_word in ("счет", "счёт"):
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формате ISO 8601
    в строку в формате 'ДД.ММ.ГГГГ'.

    Args:
        date_str (str): строка с датой, например:
                        "2024-03-11T02:26:18.671407".

    Returns:
        str: строка с датой в формате "ДД.MM.YYYY", например "11.03.2024".
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
