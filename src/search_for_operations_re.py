import re


def search_operations(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Ищет операции по строке в описании.
    :param transactions: Список словарей с транзакциями
    :param search_string: Строка для поиска в описании
    :return: Отфильтрованный список транзакций
    """
    result = []
    for operation in transactions:
        if re.search(search_string, operation["description"], re.IGNORECASE):
            result.append(operation)
    return result
