# Учебный проект по Python "Приложение для Банка" 

## Описание:

Проект "Личный кабинет банка" -  это приложение для работы с банком

1. Клонируйте репозиторий:
```
https://github.com/1Abramov1/Alexander-Abramov/tree/main
```

### Тестирование

Для тестирования проекта используется библиотека `pytest`. 

Чтобы запустить тесты, выполните команду:

'pytest'

Тесты покрывают следующие модули и функции:
- `utils`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_data`.
- `processing`: функции `filter_by_state` и `sort_by_date`.

Покрытие тестами составляет 98% кода проекта.


# Учебный проект по Python "Приложение для Банка" 


## Разработал модули decorators.py, test_decorators.py, добавил mylog.txt


## Примеры использования функци декоратора def log


### def log

```python

from functools import wraps

from typing import Any

from typing import Callable

from typing import Union


def log (filename: Any = None) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)

        def wrapper(*args: Any, **kwargs: Any) -> Any:


""" код условий добавления логов и обработок ошибок """

        
       return wrapper

     return decorator


@log("mylog.txt")

def my_decorator(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:

    return a * b


print(my_decorator(3, 5))

Покрытие тестами составляет 93% кода проекта.


## Разработал модули external_api.py, utils.py

## Примеры использования функци декоратора def log

### def log


1. Описание функциональности:
"Проект расширен поддержкой чтения финансовых операций из CSV- и Excel-файлов." 
"Реализованы функции для считывания данных в унифицированном формате."

2. Примеры использования:

# Чтение CSV
from src.reading_csv_and_excel import read_transact_csv_file
data = read_transact_csv_file('data/transactions.csv')

# Чтение Excel
from src.reading_csv_and_excel import read_transact_excel_file
data = read_transact_excel_file('data/transactions.xlsx')


1. Требования:
"Для работы необходимы:

• pandas
• openpyxl (для работы с Excel)"

1. Тестирование:

"Запуск тестов:

pytest tests/ --cov=src

Покрытие тестами: 91% 


1.2. Описание функциональности:

"Проект расширен модулями: подсчет категорий, работа с операциями через библиотеку re."

"Написана функция main в модуле main, которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой."

"Функция main предоставляет пользовательский интерфейс в соответствии с условиями задания."

" Разработал тесты для новых модулей, кроме main"

"Запуск тестов:

pytest tests/ --cov=src

Покрытие тестами: 93% 