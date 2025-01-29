from typing import Any

inform_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(inform_dict: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает на вход список словарей и значений для ключа
       state и формирует, и выдает новый список с этим ключом"""
    list_state = []

    for key in inform_dict:
        if key.get("state") == state_id:
            list_state.append(key)
    return list_state


def sort_by_date(inform_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки по дате"""
    sorted_inform_state = sorted(inform_dict, key=lambda x: x["date"], reverse=reverse)
    return sorted_inform_state


# print(filter_by_state(inform_dict))
# print(sort_by_date(inform_dict))
