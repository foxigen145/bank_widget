# bank-widget# Bank Widget — processing

Добавлены утилиты для обработки операций:
- `filter_by_state(items, state='EXECUTED')` — фильтрует по полю state.
- `sort_by_date(items, descending=True)` — сортирует по полю date (ISO format).

Примеры:
```py
from src.processing import filter_by_state, sort_by_date

data = [...]
executed = filter_by_state(data)
sorted_desc = sort_by_date(data)
Учебный проект: маскировка номеров карты и счёта.
