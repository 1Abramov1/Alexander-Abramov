from collections import Counter


def count_transactions_types(transactions,  category_dict):

     counter = Counter()

     for transaction in transactions:

       description = transaction.get('description', ' ').lower()
       for category, keywords in category_dict.items():
           for keyword in keywords:
            if keyword.lower() in description:
                counter[category] +=1
                break  #   прерываем проверку остальных ключей, так как нашли совпадение

     return dict(counter)