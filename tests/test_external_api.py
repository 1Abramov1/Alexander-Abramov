import unittest
from unittest.mock import Mock
from unittest.mock import patch

import requests

from src.external_api import convert_currency


class TestCurrencyConversion(unittest.TestCase):
    @patch("src.external_api.requests.get")
    def test_convert_currency(self, mock_get: Mock):
        # Замоканные данные, которые вернёт API
        mock_get.return_value.json.return_value = {"info": {"rate": 74.5}, "result": 7450}
        mock_get.return_value.status_code = 200

        # Тестируем конвертацию 100 USD в рубли
        result = convert_currency(100, "USD")
        self.assertEqual(result, 7450)
        # Проверяем, что запрос был сделан с правильными параметрами
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
            headers={"apikey": "lLSU3JdlytNTvWwQmNBichQwsDgssXUV"},
        )


if __name__ == "__main__":
    unittest.main()

    @patch("src.external_api.requests.get", side_effect=requests.exceptions.Timeout)
    def test_convert_currency_timeout(self, mock_get):
        # Проверяем, что функция возвращает None или обрабатывает тайм-аут корректно
        result = convert_currency(100, "USD")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
