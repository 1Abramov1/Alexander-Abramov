import logging
import sys
import logging


# Создаем логгер

logger = logging.getLogger('masks')
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
# Устанавливаем уровень логирования
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""

    if len(card_number) == 0:
        logger.error("Пустая строка")
        return "Пустая строка"

    elif len(card_number) != 16:
        logger.error("Неверное количество цифр")
        return "Неверное количество цифр"

    logger.info(f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера cчета"""

    if len(account_number) == 0:
        logger.error("Пустая строка")
        return "Пустая строка"
    elif len(account_number) < 4:
        logger.error("Неверное количество цифр")
        return "Неверное количество цифр"
    masked_account = f"**{account_number[-4:]}"
    logger.info(f"Маскированный номер счета: {masked_account}")
    return masked_account


#print(get_mask_card_number("7000792289606361"))
#print(get_mask_account("73654108430135874305"))