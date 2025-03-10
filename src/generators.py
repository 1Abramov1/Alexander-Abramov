from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(list_of_dict: List[Dict], input_currency: str = "") -> Iterator[Dict]:

    if not input_currency:
        if not input_currency:
            raise ValueError("Не выбрана валюта")
        return
    for item in list_of_dict:
        if item["operationAmount"]["currency"]["code"] == input_currency:
            yield item


transact_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


usd_transactions = filter_by_currency(transact_list, "USD")

for transaction in usd_transactions:
    print(transaction)


def transaction_descriptions(transact_list: List[Dict]) -> Iterator[str]:
    for t in transact_list:
        yield t.get("description") or "Описание отсутствует"


for description in transaction_descriptions(transact_list):
    print(description)


def card_number_generator(start: int, stop: int) -> Iterator[str]:

    for number in range(start, stop):

        card_number_g = str(number)

        while len(card_number_g) < 16:

            card_number_g = "0" + card_number_g

        formatted_card_number = (
            f"{card_number_g[0:4]} {card_number_g[4:8]} {card_number_g[8:12]} {card_number_g[12:16]}"
        )

        yield formatted_card_number


for card_number in card_number_generator(1, 20):

    print(card_number)
