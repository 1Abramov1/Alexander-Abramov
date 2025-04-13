import json
import logging
from pprint import pprint
from typing import Any
from typing import Dict
from typing import List

# Создаем логгер

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
# Устанавливаем уровень логирования
logger.setLevel(logging.DEBUG)


def transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция для получения данных банковских операций из Json-файла"""
    try:
        logger.info(f"Получение данных из файла {file_path}")
        with open(file_path, encoding="utf-8") as f:
            operations = json.load(f)
            if not isinstance(operations, list):
                logger.error("Данные в файле не являются списком")
                return []
            return operations
    except FileNotFoundError:
        logger.error(f'Ошибка: файл "{file_path}" не найден')
        return []
    except json.JSONDecodeError:
        logger.error(f'Ошибка при чтении json-файла из файла "{file_path}"')
        return []


# Пример вызова функции
pprint(transactions("../data/operations.json"))
