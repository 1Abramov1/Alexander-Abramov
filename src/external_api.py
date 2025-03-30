import os
from typing import Optional

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_currency(amount: int, currency: str) -> Optional[float]:
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
    result = convert_currency(100, "USD")
    if result is not None:
        print(f"Converted amount: {result} RUB")
except ValueError as e:
    print(e)
