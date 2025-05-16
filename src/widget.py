from src.masks import get_mask_account
from src.masks import get_mask_card_number

"""
Написать функцию, которая, обрабатывает информацию о карте и о счете
"""

def mask_account_card(number: str) -> str:
    """Функция, маскировки счета/номера карты"""
    number = number.split()
    if  number == []:
        return "Номер карты не найден"
    if "счет" in number[0].lower():
        number[-1] = get_mask_account(number[-1])
    else:
        number[-1] = get_mask_card_number(number[-1])
    return " ".join(number)


def get_new_data(old_data: str) -> str:
    """Функция принимает строку и выводит дату в формате dd.mm.yyyy"""
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])

#print(mask_account_card('Счет 45457000792289606361'))
#print(get_new_data("2024-03-11T02:26:18.671407"))