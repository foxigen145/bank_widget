# Bank Widget — обработка банковских операций

Проект предназначен для обработки данных о банковских операциях.  
Реализованы функции для фильтрации и сортировки списка операций по заданным параметрам.

---

## Установка и использование

### 1. Клонирование репозитория
```bash
git clone https://github.com/<ВАШ_НИК_НА_GITHUB>/<ИМЯ_РЕПОЗИТОРИЯ>.git
cd <ИМЯ_РЕПОЗИТОРИЯ>
```

### 2. Создание виртуального окружения (рекомендуется)
```bash
python -m venv venv
```

**Активация окружения:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux / Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

---

## Примеры использования

### Фильтрация операций по статусу
```python
from processing import filter_by_state

transactions = [
    {"id": 1, "state": "EXECUTED", "amount": 100},
    {"id": 2, "state": "CANCELED", "amount": 200},
    {"id": 3, "state": "EXECUTED", "amount": 300},
]

result = filter_by_state(transactions)
print(result)
# [{'id': 1, 'state': 'EXECUTED', 'amount': 100}, {'id': 3, 'state': 'EXECUTED', 'amount': 300}]
```

---

### Сортировка операций по дате
```python
from processing import sort_by_date

transactions = [
    {"id": 1, "date": "2024-08-10T10:30:00", "amount": 150},
    {"id": 2, "date": "2024-09-15T12:15:00", "amount": 200},
    {"id": 3, "date": "2024-07-05T08:00:00", "amount": 100},
]

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)
# [{'id': 2, 'date': '2024-09-15T12:15:00', 'amount': 200},
#  {'id': 1, 'date': '2024-08-10T10:30:00', 'amount': 150},
#  {'id': 3, 'date': '2024-07-05T08:00:00', 'amount': 100}]
```
## Документация и ссылки

- [Документация по Python](https://docs.python.org/3/)
- [Репозиторий проекта на GitHub](https://github.com/ВАШ_НИК_НА_GITHUB/ИМЯ_РЕПОЗИТОРИЯ)

## Лицензия

Этот проект распространяется под лицензией MIT