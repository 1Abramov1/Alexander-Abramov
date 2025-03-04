# Учебный проект по Python

# Добавлен новый модуль generators.py

## Примеры использования

### filter_by_currency 
```python
from src.generators import filter_by_currency

transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}},
    {"operationAmount": {"currency": {"code": "EUR"}}}
]

usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
    print(transaction)
```

### transaction_descriptions
```python
from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод с карты на счет"}
]

descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)
```

### card_number_generator
```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 3):
    print(card_number)


### Тестирование 

Для тестирования проекта используется библиотека `pytest`. 

Чтобы запустить тесты, выполните команду:

'pytest'

Тесты покрывают следующие модули и функции:
 
- 'generators': функции  'filter_by_currency'
- 'generators': функции  'transaction_descriptions'
- 'generators': функции   'card_number_generator'

- Покрытие тестами составляет 90% кода проекта.
