from collections import Counter


def count_transactions_types(transactions: list[dict], categories: list) -> dict[str, int]:
    categories_lower = [c.lower() for c in categories]  # Приводим к нижнему регистру один раз
    counter = Counter()

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories_lower:  # Проходим по списку категорий
            if category in description:  # Ищем прямое вхождение
                counter[category] += 1
                break  # Прерываем после первого совпадения

    return dict(counter)
