import pytest  # noqa: F401 (для подавления предупреждения)

from src.search_for_operations_re import search_operations


def test_search_operations():
    test_data = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"}
    ]

    """ Проверка поиска по подстроке """
    result = search_operations(test_data, "перевод")
    assert len(result) == 2

    """ Проверка регистронезависимости """
    result = search_operations(test_data, "ПЕРЕВОД")
    assert len(result) == 2

    """ Проверка пустого результата """
    result = search_operations(test_data, "несуществующий")
    assert len(result) == 0

    """ Проверку пустого списка транзакций """
    assert len(search_operations([], "перевод")) == 0

    """ Проверка поиска по части слова """
    test_data.append({"description": "Переводной документ"})
    assert len(search_operations(test_data, "вод")) == 3




