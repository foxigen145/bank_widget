import json
from unittest.mock import mock_open
from unittest.mock import patch

from src.utils.json_handler import read_json


def test_read_json_valid():
    data = [{"id": 1}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        result = read_json("fake.json")
        assert result == data


def test_read_json_invalid():
    with patch("builtins.open", mock_open(read_data="{}")):
        result = read_json("fake.json")
        assert result == []


def test_read_json_not_found():
    result = read_json("no_file.json")
    assert result == []
