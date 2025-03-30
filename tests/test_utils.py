import unittest
from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import transactions


class TestTransactions(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_transactions(self, mock_file):
        result = transactions()
        self.assertEqual(result, [{"id": 1, "amount": 100}])


if __name__ == "__main__":
    unittest.main()
