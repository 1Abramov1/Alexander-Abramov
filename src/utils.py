import json
from pprint import pprint
from typing import Any
from typing import Dict
from typing import List


def transactions(file_path: str) -> List[Dict[str, Any]]:
    data = []
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")  # Отладочный вывод ошибки
    return data


# Пример вызова функции
pprint(transactions("../data/operations.json"))
