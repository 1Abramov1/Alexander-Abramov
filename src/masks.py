
"""
Написать функцию, которая, получает на вход номер карты
и возвращает ее маску, то же самое с номером счета.
"""


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """ Функция для маскировки номера cчета"""
    return f"**{account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))


