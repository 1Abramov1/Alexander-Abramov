from src.masks import get_mask_card_number
import pytest

@pytest.fixture
def card_number():
  return "1234567812345678" # стандартная длина


def test_get_mask_card_number(card_number):
  masked_number = get_mask_card_number(card_number)
  assert masked_number == "1234 56** **** 5678"


@pytest.mark.parametrize("card_number, expected", [
 ("1234567812345678", "1234 56** **** 5678"),  # стандартный случай
 ("1234", "Неверное количество цифр"), # минимальная длина
 ("","Пустая строка" ), # пустая строка
 ("12345678901234567890", "Неверное количество цифр"),  # нестандартная длина
 ("abcd1234abcd5678", "abcd 12** **** 5678")  # нестандартный формат
])


def test_get_mask_card_number1(card_number, expected):
  masked_number = get_mask_card_number(card_number)
  assert masked_number == expected
