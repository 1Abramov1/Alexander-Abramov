import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
import pytest_mock

from src.reading_csv_and_excel import read_transact_excel_file


class TestExcelReader(unittest.TestCase):
    @patch("pandas.read_excel")
    def test_read_excel_returns_dict_list(self, mock_read: MagicMock) -> None:
        # Настраиваем mock для read_excel
        mock_read.return_value = MagicMock()
        mock_read.return_value.to_dict.return_value = [{"id": 1, "state": "EXECUTED"}]

        # Вызываем тестируемую функцию
        result = read_transact_excel_file("dummy_path.xlsx")

        # Проверяем, что результат - список
        self.assertIsInstance(result, list)
        # Проверяем, что pandas.read_excel был вызван
        self.assertIsInstance(result[0], dict)


def test_invalid_path(mocker: pytest_mock.MockerFixture) -> None:
    mocker.patch("pandas.read_excel", side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        read_transact_excel_file("invalid_path.xlsx")
