from src.widget import get_date
from src.widget import mask_account_card


# Тесты для mask_account_card
def test_mask_account_card_cards() -> None:
    cards = {
        "Visa Platinum 7000792289606361": "Visa Platinum 7000 79** **** 6361",
        "Maestro 1596837868705199": "Maestro 1596 83** **** 5199",
        "MasterCard 7158300734726758": "MasterCard 7158 30** **** 6758",
        "Visa Classic 6831982476737658": "Visa Classic 6831 98** **** 7658",
        "Visa Gold 5999414228426353": "Visa Gold 5999 41** **** 6353",
    }
    for input_str, expected in cards.items():
        assert mask_account_card(input_str) == expected


def test_mask_account_card_accounts() -> None:
    accounts = {
        "Счет 73654108430135874305": "Счет **4305",
        "Счет 64686473678894779589": "Счет **9589",
        "Счет 35383033474447895560": "Счет **5560",
    }
    for input_str, expected in accounts.items():
        assert mask_account_card(input_str) == expected


def test_get_date() -> None:
    dates = {
        "2024-03-11T02:26:18.671407": "11.03.2024",
        "2018-07-11T15:42:00.000000": "11.07.2018",
        "2025-09-12T12:00:00.123456": "12.09.2025",
    }
    for input_str, expected in dates.items():
        assert get_date(input_str) == expected
