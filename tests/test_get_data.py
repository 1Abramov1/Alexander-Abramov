import pytest

from src.widget import get_new_data


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"

def test_get_new_data(date):
    assert get_new_data(date) == "11.03.2024"




