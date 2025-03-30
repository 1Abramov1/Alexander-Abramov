import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize("mask_account, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                    ("Счет 64686473678894779589", "Счет **9589")])
def test_mask_account_card(mask_account, expected):
    assert mask_account_card(mask_account) == expected
