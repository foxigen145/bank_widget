import os
from typing import Any
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Если валюта уже RUB — возвращает сумму без изменений.
    """
    amount_str = transaction.get("operationAmount", {}).get("amount", 0)
    try:
        amount = float(amount_str)
    except (TypeError, ValueError):
        amount = 0.0

    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Явно приводим курс к float, чтобы mypy не ругался
    rate_raw: Any = response.json().get("rates", {}).get("RUB", 0)
    try:
        rate: float = float(rate_raw)
    except (TypeError, ValueError):
        rate = 0.0

    return amount * rate
