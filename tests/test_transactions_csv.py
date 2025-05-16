import unittest
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

from src.reading_csv_and_excel import read_transact_csv_file


class TestCSVReader(unittest.TestCase):
    @patch("builtins.open", mock_open(read_data="id;state\n1;EXECUTED\n2;CANCELED"))
    @patch("csv.DictReader")
    def test_returns_list_of_dicts(self, mock_read: MagicMock) -> None:
        # Настраиваем mock для DictReader
        mock_read.return_value = [{"id": "1", "state": "EXECUTED"}, {"id": "2", "state": "CANCELED"}]

        # Вызываем тестируемую функцию
        result = read_transact_csv_file("dummy_path.csv")

        # Проверяем, что результат - список
        self.assertIsInstance(result, list)

        # И что все элементы - словари
        for item in result:
            self.assertIsInstance(item, dict)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_invalid_path(self, mocked_open: MagicMock) -> None:
        with self.assertRaises(FileNotFoundError):
            read_transact_csv_file("invalid_path.csv")
        mocked_open.assert_called_once_with("./data/transactions.csv", encoding="utf-8")
