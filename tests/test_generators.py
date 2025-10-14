import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
            "description": "Оплата услуг",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300", "currency": {"name": "USD", "code": "USD"}},
            "description": "Покупка",
        },
    ]


@pytest.mark.parametrize("currency,expected_count", [("USD", 2), ("EUR", 1), ("RUB", 0)])
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count
    for t in result:
        assert t["operationAmount"]["currency"]["code"] == currency


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Оплата услуг", "Перевод", "Покупка"]


@pytest.mark.parametrize("start,stop,expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
    for card in result:
        assert len(card) == 19  # 16 цифр + 3 пробела


def test_card_number_generator_empty():
    assert list(card_number_generator(5, 4)) == []