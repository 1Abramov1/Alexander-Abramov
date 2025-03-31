import pytest

from src.processing import sort_by_date


@pytest.mark.parametrize ("sort_date, expected", [
    ([{'date': '2023-10-01'}, {'date': '2023-09-15'}, {'date': '2023-11-05'}],
     [{'date': '2023-09-15'}, {'date': '2023-10-01'}, {'date': '2023-11-05'}]),  # по возрастанию
    ([{'date': '2023-10-01'}, {'date': '2023-10-01'}, {'date': '2023-10-01'}],
     [{'date': '2023-10-01'}, {'date': '2023-10-01'}, {'date': '2023-10-01'}]),  # одинаковые даты
    ([{'date': 'invalid-date'}, {'date': '2023-10-01'}], [])  # некорректная дата
])
def test_sort_by_date(sort_date, expected):
    assert sort_by_date(sort_date, descending=False) == expected