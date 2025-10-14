from src.processing import filter_by_state
from src.processing import sort_by_date

SAMPLE = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state_default() -> None:
    out = filter_by_state(SAMPLE)
    assert all(item["state"] == "EXECUTED" for item in out)
    assert len(out) == 2


def test_filter_by_state_custom() -> None:
    out = filter_by_state(SAMPLE, "CANCELED")
    assert len(out) == 2
    assert all(item["state"] == "CANCELED" for item in out)


def test_sort_by_date_default_desc() -> None:
    out = sort_by_date(SAMPLE)
    # Первая запись должна быть самой новой (2019)
    assert out[0]["id"] == 41428829


def test_sort_by_date_asc() -> None:
    out = sort_by_date(SAMPLE, descending=False)
    # Первая запись должна быть самой старой (2018-06-30)
    assert out[0]["id"] == 939719570
