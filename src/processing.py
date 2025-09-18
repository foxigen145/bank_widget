from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(items: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей из `items`, у которых ключ 'state' равен заданному `state`.
    Параметр state по умолчанию = "EXECUTED".
    """
    return [item for item in items if item.get("state") == state]


def sort_by_date(items: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Возвращает новый список, отсортированный по ключу 'date'.
    Параметр `descending=True` (по умолчанию) — сортировка по убыванию (сначала новые даты).
    Дата ожидается в ISO формате: "YYYY-MM-DDTHH:MM:SS[.micro]".
    """
    def _parse_date(item: Dict[str, Any]) -> datetime:
        d = item.get("date")
        try:
            return datetime.fromisoformat(d)
        except Exception:
            # если дата отсутствует или некорректна, ставим минимальную дату
            return datetime.min

    return sorted(items, key=_parse_date, reverse=descending)
