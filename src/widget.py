"""Функции для работы с отображением карточек/счетов и дат в виджете."""

from datetime import datetime
from typing import Tuple

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def _split_name_and_number(info: str) -> Tuple[str, str]:
    """
    Вспомогательная: разбивает исходную строку на "имя" (тип) и "номер".
    Делает это безопасно: берёт последний "токен" как номер, а всё остальное — имя.
    """
    parts = info.strip().split()
    if len(parts) < 2:
        raise ValueError("Ожидается строка вида '<Имя> <Номер>' (например, 'Visa Classic 1234...' или 'Счет 1234...').")
    name = " ".join(parts[:-1])
    number = parts[-1]
    return name, number


def mask_account_card(info: str) -> str:
    """
    Принимает одну строку с типом и номером карты/счёта и возвращает строку с замаскированным номером.

    Использует ранее реализованные функции маскировки из модуля `masks`.
    """
    name, number = _split_name_and_number(info)

    # Определяем: счёт это или карта — по первому слову (Счет/Счёт).
    first_word = name.split()[0].lower()
    if first_word in ("счет", "счёт"):
        return f"{name} {get_mask_account(number)}"

    # Иначе считаем, что это карта (Visa/MasterCard/Maestro/и т.п.)
    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Принимает ISO-дату и возвращает дату в формате 'ДД.ММ.ГГГГ' (например, '11.03.2024').
    """
    # fromisoformat корректно понимает строку с 'T' и микросекундами.
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")