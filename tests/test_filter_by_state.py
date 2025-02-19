import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize("input_data, state, expected", [
    ([{'state': 'active'}, {'state': 'inactive'}, {'state': 'active'}], 'active', [{'state': 'active'}, {'state': 'active'}]),
    ([{'state': 'inactive'}, {'state': 'inactive'}], 'active', []),
    ([{'state': 'active'}, {'state': 'inactive'}], 'inactive', [{'state': 'inactive'}])
])
def test_filter_by_state(input_data, state, expected):
    assert filter_by_state(input_data, state) == expected