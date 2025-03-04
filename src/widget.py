import sys

sys.path.append('C:/Users/New_Alexs/PycharmProjects/PythonProject1')

from src.masks import get_mask_account
from src.masks import get_mask_card_number

"""
Написать функцию, которая, обрабатывает информацию о карте и о счете
"""


def mask_account_card(number: str) -> str:
    """Функция, маскировки счета/номера карты"""
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result

    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
        return result

    else:
        return "Введен некорректный номер счета"


def get_new_data(old_data: str) -> str:
    """Функция принимает строку и выводит дату в формате dd.mm.yyyy"""
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])

print(mask_account_card('Счет 45457000792289606361'))
print(get_new_data("2024-03-11T02:26:18.671407"))