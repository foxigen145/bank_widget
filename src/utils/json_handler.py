import json
from typing import Any
from typing import Dict
from typing import List


def read_json(path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, поврежден или не найден — возвращает пустой список.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
