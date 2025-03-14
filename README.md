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
