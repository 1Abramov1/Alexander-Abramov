from src.masks import get_mask_account
import pytest


@pytest.fixture
def account_number():
  return "73654108430135874305" # стандартная длина


def test_get_mask_account(account_number):
  masked_account = get_mask_account(account_number)
  assert masked_account == "**4305"


@pytest.mark.parametrize("account_number, expected", [
 ("44811934567890122392", "**2392"),  # стандартный случай
 ("1232", "**1232"), # минимальная длина
 ("","Пустая строка" ), # пустая строка
 ("1234567890123456789021", "**9021"),  # нестандартная длина
 ("abcd1234abcd5678bn2f", "**bn2f")  # нестандартный формат
])


def test_get_mask_account1(account_number, expected):
  masked_account = get_mask_account(account_number)
  assert masked_account == expected