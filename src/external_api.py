import os
from typing import Any
from typing import Dict
from typing import Optional

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_currency(transaction: Dict[str, Any]) -> Optional[float]:
    currency = transaction.get("currency")
    amount = transaction.get("amount")

    if currency is None or amount is None:
        raise ValueError("Invalid transaction data")
    if currency not in ("USD", "EUR"):
        raise ValueError("Unsupported currency")

    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на HTTP ошибки
        data = response.json()
        rub_amount = float(amount * data["info"]["rate"])
        return rub_amount
    except RequestException as error:
        print(f"Error fetching data from API: {error}")
        return None


# Пример вызова функции
try:
    transaction = {"amount": 100, "currency": "USD"}  # Создаём словарь с нужными данными
    result = convert_currency(transaction)  # Передаём словарь в функцию
    if result is not None:
        print(f"Converted amount: {result} RUB")
except ValueError as e:
    print(e)
