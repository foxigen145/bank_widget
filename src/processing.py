from datetime import datetime
from typing import Any
from typing import Dict
from typing import List


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Возвращает список операций с заданным статусом.

    :param operations: список словарей операций
    :param state: значение статуса (по умолчанию "EXECUTED")
    :return: новый список словарей, где 'state' равен переданному значению
    """
    filtered_operations: List[Dict[str, Any]] = [
        operation for operation in operations if operation.get("state") == state
    ]
    return filtered_operations


def sort_by_date(
    operations: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """
    Возвращает список операций, отсортированный по дате.

    :param operations: список словарей операций
    :param descending: True — по убыванию (новые даты первыми), False — по возрастанию
    :return: новый список словарей, отсортированный по дате
    """
    def parse_date(operation: Dict[str, Any]) -> datetime:
        date_value = operation.get("date")
        if isinstance(date_value, str):
            try:
                return datetime.fromisoformat(date_value)
            except ValueError:
                # Если дата некорректная, считаем минимальной
                return datetime.min
        # Если дата отсутствует, возвращаем минимальную дату
        return datetime.min

    return sorted(operations, key=parse_date, reverse=descending)
