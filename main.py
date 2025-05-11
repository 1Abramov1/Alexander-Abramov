import csv
import json

import openpyxl

from src.search_for_operations_re import search_operations
from src.widget import mask_account_card


def main() -> None:
    """Основная функция управления программой."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    transactions = []
    while True:
        print("\nВыберите тип файла:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор (1-3): ")

        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            try:
                with open("data/operations.json", "r", encoding="utf-8") as file:
                    transactions = json.load(file)  # Обновляем переменную
                break
            except FileNotFoundError:
                print("JSON файл не найден, попробуйте снова")

        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            try:
                with open("data/transactions.csv", "r", encoding="utf-8") as file:
                    transactions = list(csv.DictReader(file, delimiter=";"))
                break
            except FileNotFoundError:
                print("CSV файл не найден, попробуйте снова")

        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            try:
                wb = openpyxl.load_workbook("data/transactions_excel.xlsx")
                sheet = wb.active
                if sheet is None:
                    print("В файле нет активного листа")
                    continue

                transactions = []
                headers = [str(cell.value) if cell.value is not None else "" for cell in sheet[1]]

                for row in sheet.iter_rows(min_row=2, values_only=True):
                    if not any(row):  # Пропускаем пустые строки
                        continue

                    # Создаем словарь, фильтруя None-значения
                    transaction = {
                        header: str(value) if value is not None else "" for header, value in zip(headers, row)
                    }
                    transactions.append(transaction)

                if not transactions:
                    print("Файл не содержит данных")
                    continue

                break
            except FileNotFoundError:
                print("XLSX файл не найден, попробуйте снова")
            except Exception as e:
                print(f"Ошибка при чтении XLSX: {e}")

        else:
            print("Неверный выбор")

        if not transactions:
            print("Не удалось загрузить транзакции")
            return

    valid_statuses = ["executed", "canceled", "pending"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        status = input("Ваш выбор: ").lower()
        if status in valid_statuses:
            transactions = [t for t in transactions if t.get("state") and t["state"].lower() == status]
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен')

    sort_answer = input("Отсортировать операции по дате? (да/нет): ").lower()
    if sort_answer == "да":
        order = input("По возрастанию или по убыванию? ").lower()
        reverse = order == "по убыванию"
        transactions.sort(key=lambda x: x["date"], reverse=reverse)

    # Фильтрация по валюте
    rub_answer = input("Выводить только рублевые транзакции? (да/нет): ").lower()
    if rub_answer == "да":
        transactions = [
            t
            for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code", "").lower() == "rub"
        ]

    # Фильтрация по ключевому слову
    word_answer = input("Фильтровать по слову в описании? (да/нет): ").lower()
    if word_answer == "да":
        search_word = input("Введите слово для поиска: ")
        transactions = search_operations(transactions, search_word)

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего операций в выборке: {len(transactions)}")
    for t in transactions:
        from_account = f"{t.get('from_type', '')} {t.get('from', '')}"
        to_account = f"{t.get('to_type', '')} {t.get('to', '')}"
        print(
            f"{t['date']} {t['description']}\n"
            f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}\n"
            f"Сумма: {t.get('amount', 'N/A')} {t.get('currency_code', '')}\n"
        )


if __name__ == "__main__":
    main()
