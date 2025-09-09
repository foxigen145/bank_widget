"""Утилиты маскирования номеров карты и счёта."""

from typing import Union


def _digits_only(value: Union[int, str]) -> str:
    """Возвращает строку, очищенную от всех символов, кроме цифр."""
    return "".join(ch for ch in str(value) if ch.isdigit())


def _group4(s: str) -> str:
    """Разбивает строку на блоки по 4 символа и соединяет пробелами."""
    return " ".join(s[i:i+4] for i in range(0, len(s), 4))


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Видны первые 6 и последние 4 цифры.
    """
    digits = _digits_only(card_number)

    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    masked = digits[:6] + "**" + "****" + digits[-4:]
    return _group4(masked)


def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Маскирует номер счёта в формате **XXXX (видны последние 4 цифры).
    """
    digits = _digits_only(account_number)

    if len(digits) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{digits[-4:]}"
