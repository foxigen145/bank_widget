import pytest

from src.processing import filter_by_state, sort_by_date

operations_sample = [
    {"id": 1, "state": "EXECUTED", "date": "2024-08-10T10:30:00"},
    {"id": 2, "state": "CANCELED", "date": "2024-09-15T12:15:00"},
    {"id": 3, "state": "EXECUTED", "date": "2024-07-05T09:00:00"},
    {"id": 4, "state": "PENDING", "date": "2024-08-20T14:00:00"},
]

def test_filter_by_state_default():
    filtered = filter_by_state(operations_sample)
    assert all(op["state"] == "EXECUTED" for op in filtered)
    assert len(filtered) == 2

def test_filter_by_state_custom():
    filtered = filter_by_state(operations_sample, state="CANCELED")
    assert len(filtered) == 1
    assert filtered[0]["id"] == 2

def test_sort_by_date_descending():
    sorted_ops = sort_by_date(operations_sample)
    dates = [op["date"] for op in sorted_ops if "date" in op]
    assert dates == sorted(dates, reverse=True)

def test_sort_by_date_ascending():
    sorted_ops = sort_by_date(operations_sample, descending=False)
    dates = [op["date"] for op in sorted_ops if "date" in op]
    assert dates == sorted(dates)

