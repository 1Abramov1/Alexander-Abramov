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

