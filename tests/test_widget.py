import pytest
from src.widget import get_date, mask_account_card



@pytest.fixture
def cards_data():
    return {
        "Visa Platinum 7000792289606361": "Visa Platinum 7000 79** **** 6361",
        "Maestro 1596837868705199": "Maestro 1596 83** **** 5199",
        "MasterCard 7158300734726758": "MasterCard 7158 30** **** 6758",
        "Visa Classic 6831982476730758": "Visa Classic 6831 98** **** 7658",
        "Visa Gold 5999442284263533": "Visa Gold 5999 41** **** 6353",
    }


@pytest.fixture
def accounts_data():
    return {
        "Счет 7354108430153874305": "Счет **4305",
        "Счет 6468647376889479589": "Счет **9589",
        "Счет 35380333474447895560": "Счет **5560",
    }


@pytest.fixture
def dates_data():
    return {
        "2024-03-11T02:26:18.671409": "11.03.2024",
        "2018-07-11T15:42:00.000000": "11.07.2018",
        "2025-09-12T12:00:00.123456": "12.09.2025",
    }


@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476730758", "Visa Classic 6831 98** **** 7658"),
    ("Visa Gold 5999442284263533", "Visa Gold 5999 41** **** 6353"),
])
def test_mask_account_card_cards(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("Счет 7354108430153874305", "Счет **4305"),
    ("Счет 6468647376889479589", "Счет **9589"),
    ("Счет 35380333474447895560", "Счет **5560"),
])
def test_mask_account_card_accounts(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("2024-03-11T02:26:18.671409", "11.03.2024"),
    ("2018-07-11T15:42:00.000000", "11.07.2018"),
    ("2025-09-12T12:00:00.123456", "12.09.2025"),
])
def test_get_date(input_str, expected):
    assert get_date(input_str) == expected

