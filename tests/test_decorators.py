from typing import Any

import pytest

from src.decorators import log


def test_my_decorator() -> None:
    @log()
    def add_numbers(a: int, b: int) -> int:
        return a * b

    result = add_numbers(3, 5)
    assert result == 15


def test_my_decorators(capsys: Any) -> None:
    @log()
    def add_numbers(a: int, b: int) -> int:
        return a * b

    result = add_numbers(3, 5)
    assert result == 15  # 3 * 5
    captured = capsys.readouterr()
    assert "add_numbers ok: 15" in captured.out  # сравнивает с результатом из log файла


@log()
def faulty_function(a: int, b: int) -> int:
    return int(a / b)  # Это вызовет ошибку, если b == 0


def test_faulty_function() -> None:
    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)
