from collections import Counter


def count_transactions_types(transactions: list[dict], category_dict: dict[str, list[str]]) -> dict[str, int]:

    counter: Counter[str] = Counter()

    for transaction in transactions:

        description = transaction.get("description", " ").lower()
        for category, keywords in category_dict.items():
            for keyword in keywords:
                if keyword.lower() in description:
                    counter[category] += 1
                    break  # прерываем проверку остальных ключей, так как нашли совпадение

    return dict(counter)
