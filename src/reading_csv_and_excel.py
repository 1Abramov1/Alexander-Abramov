import csv
from typing import Any
from typing import Dict
from typing import Hashable

import pandas as pd

"""Функция для чтения CSV-файла и преобразования его в список словарей"""


def read_transact_csv_file(file_path: str) -> list[Dict[str, str]]:
    transactions = []
    with open('../data/transactions.csv', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            if row["state"].strip() == "EXECUTED":
                transactions.append(row)
        print(len(transactions))
        return transactions


filtered_transactions = read_transact_csv_file('../data/transactions.csv')  # преобразование выводимых данных из файла сsv
for transact in filtered_transactions:
    print(
        f" ID: {transact['id']}, State: {transact['state']}, "
        f" Date: {transact['date']}, Amount: {transact['amount']}, Currency_name: {transact['currency_name']} "
        f" Currency_code: {transact['currency_code']}, From: {transact['from']}, "
        f" To: {transact['to']}, Description: {transact['description']} "
    )
    print("-" * 240)


"""Функция для чтения Excel-файла и преобразования его в список словарей"""


def read_transact_excel_file(file_path: str) -> list[dict[Hashable, Any]]:
    return pd.read_excel(file_path, engine="openpyxl").to_dict(orient="records")


# Вызов функции и вывод результата
result = read_transact_excel_file('../data/transactions_excel.xlsx')
for transaction in result:  # type: dict[Hashable, Any]
    print(transaction)
    print("-" * 50)  # разделитель между записями
