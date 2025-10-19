from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}
    mock_get.return_value.raise_for_status = lambda: None

    transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}
    result = convert_to_rub(transaction)
    assert result == 1000.0


def test_convert_rub_no_api_call():
    transaction = {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}}
    result = convert_to_rub(transaction)
    assert result == 500.0
