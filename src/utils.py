import json
from pprint import pprint
from typing import Any
from typing import Dict
from typing import List


def transactions() -> List[Dict[str, Any]]:
    data = []
    try:
        with open("../data/operations.json", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")  # Отладочный вывод ошибки
    return data


pprint(transactions())
