from typing import Any

from src.decorators import log


def test_my_decorator() -> None:
    @log("../src/mylog.txt")
    def add_numbers(a: int, b: int) -> int:
        return a * b

    result = add_numbers(3, 5)
    assert result == 15


def test_my_decorators(capsys: Any) -> None:
    @log()
    def add_numbers(a: int, b: int) -> int:
        return a * b

    result = add_numbers(3, 5)
    assert result == 15
    captured = capsys.readouterr()
    assert "add_numbers ok: 15" in captured.out
