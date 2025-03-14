from functools import wraps
from typing import Any
from typing import Callable
from typing import Union


def log(filename: Any = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok: {result}"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


@log("mylog.txt")
def my_decorator(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


print(my_decorator(3, 5))
