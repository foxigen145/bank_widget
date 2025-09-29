import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 937919570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
])
def test_filter_by_state(sample_data, state, expected_count):
    out = filter_by_state(sample_data, state=state)
    assert all(item["state"] == state for item in out)
    assert len(out) == expected_count


@pytest.mark.parametrize("descending, expected_first_id", [
    (True, 41428829),      # Самая новая дата
    (False, 937919570),    # Самая старая дата
])
def test_sort_by_date(sample_data, descending, expected_first_id):
    out = sort_by_date(sample_data, descending=descending)
    assert out[0]["id"] == expected_first_id

