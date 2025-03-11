from src.decorators import log

def test_decorators():
    @log("mylog.txt")
    def add_numbers(a, b):
        return a * b

    result = add_numbers(3, 5)
    assert result == 15


