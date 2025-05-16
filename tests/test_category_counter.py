import pytest  # noqa: F401 (для подавления предупреждения)

from src.category_counter import count_transactions_types


def test_search_by_description():
    """ Тест на поиск по полю description """
    test_data = [
        {"description": "Перевод организации", "other_field": "test"},
        {"other_field": "Другой перевод"}  # Должен быть проигнорирован
    ]
    categories = {"перевод": ["перевод"]}
    result = count_transactions_types(test_data, categories)
    assert result == {"перевод": 1}


def test_case_insensitive():
    """ Тест на регистронезависимость """
    test_data = [{"description": "ПЕРЕВОД Организации"}]
    categories = {"перевод": ["перевод"]}
    result = count_transactions_types(test_data, categories)
    assert result == {"перевод": 1}


def test_counter_logic():
    """ Тест работы счетчика """
    test_data = [
        {"description": "Перевод с карты"},
        {"description": "Оплата картой"},
        {"description": "Открытие вклада"}
    ]
    categories = {
        "карта": ["карта", "картой"],
        "перевод": ["перевод"]
    }
    result = count_transactions_types(test_data, categories)
    assert result == {"перевод": 1}


def test_empty_transactions():
    """Проверка работы с пустыми данными."""

    # Проверка пустого списка транзакций
    result1 = count_transactions_types([], {"категория": ["слово"]})

    # Проверка пустого словаря категорий
    result2 = count_transactions_types([{"description": "тест"}], {})

    # Проверка обоих пустых параметров
    result3 = count_transactions_types([], {})

    # Общие проверки для всех случаев
    assert result1 == {} and isinstance(result1, dict)
    assert result2 == {} and isinstance(result2, dict)
    assert result3 == {} and isinstance(result3, dict)