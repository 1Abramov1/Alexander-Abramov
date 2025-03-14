import pytest
from src.decorators import log

def test_my_decorator():
    @log("../src/mylog.txt")
    def add_numbers(a, b):
        return a * b

    result = add_numbers(3, 5)
    assert result == 15


