from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

"""Список словарей с датами"""

date_data = [{"date": "2023-10-01"}, {"date": "2023-09-15"}, {"date": "2023-11-05"}]

"""Функция сортировки по дате"""


def sort_by_date(data: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    try:
        return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=descending)
    except (KeyError, ValueError) as e:
        print(f"Ошибка при сортировке: {e}")
        return []


"""Вызов функции и вывод результата"""

sorted_data = sort_by_date(date_data)
print(sorted_data)


def filter_by_state(data: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
    return [item for item in data if item.get("state") == state]


"""Пример использования функции"""


state_data = [
    {"id": 1, "name": "Item 1", "state": "active"},
    {"id": 2, "name": "Item 2", "state": "inactive"},
    {"id": 3, "name": "Item 3", "state": "active"},
    {"id": 4, "name": "Item 4", "state": "pending"},
]

filtered_data = filter_by_state(state_data, "active")
print(filtered_data)