from typing import Dict
from typing import List
from typing import Tuple

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.fixture
def transact_list_fixture() -> List[Dict]:
    return [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "EUR"}}}]


def test_filter_by_currency(transact_list_fixture: List[Dict]) -> None:
    result = list(filter_by_currency(transact_list_fixture, "USD"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


@pytest.mark.parametrize(
    "transact_list, expected",
    [
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        ([{"description": "Перевод с карты на счет"}], ["Перевод с карты на счет"]),
        ([{"description": ""}], ["Описание отсутствует"]),
    ],
)
def test_transaction_descriptions(transact_list: List[dict], expected: List[str]) -> None:
    result = list(transaction_descriptions(transact_list))
    assert result == expected


@pytest.mark.parametrize(
    "card_number_g, expected",
    [
        ((1, 2), ["0000 0000 0000 0001"]),
        ((10, 12), ["0000 0000 0000 0010", "0000 0000 0000 0011"]),
        ((9999999999999998, 10000000000000000), ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(card_number_g: Tuple[int, int], expected: list[str]) -> None:
    result = list(card_number_generator(*card_number_g))
    assert result == expected
