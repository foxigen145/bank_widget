from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по коду валюты.

    :param transactions: список словарей с данными транзакций
    :param currency_code: код валюты (например, 'USD')
    :return: итератор с транзакциями в заданной валюте
    """
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Возвращает описания транзакций по очереди.

    :param transactions: список словарей с данными транзакций
    :return: итератор с описаниями
    """
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное число
    :param stop: конечное число
    :return: итератор с номерами карт
    """
    for number in range(start, stop + 1):
        yield f"{number:016}".replace("", " ")[1:-1]
