Борисов Анатолий Олегович, группа 221141, вариант 5, лабораторная №2

# Лабораторная работа №2

## Выполненные задания

### Средняя сложность

- №5: список простых чисел до 100 в `prime_numbers.py`;
- №7: подсчёт гласных в `text_utils.py` и `vowel_counter.py`;
- №1: таблица умножения в `multiplication_table.py`.

### Повышенная сложность

- №6: собственные модули импортируются в консольные программы и `main.py`;
- №8: бинарный поиск в `search_utils.py` с примером в `binary_search_demo.py`.

## Запуск

```bash
python main.py
```

```bash
python vowel_counter.py "Методы и технологии программирования"
```

## Проверка

```bash
python -m pip install -r requirements-dev.txt
python -m flake8 .
python -m unittest discover -v
```
