"""Демонстрация заданий лабораторной работы №2."""

from multiplication_table import format_multiplication_table
from prime_numbers import prime_numbers_up_to
from search_utils import binary_search
from text_utils import count_vowels


def main() -> None:
    """Последовательно показывает результаты всех заданий."""
    print("Таблица умножения 1-10:")
    print(format_multiplication_table())

    print("\nПростые числа до 100:")
    print(*prime_numbers_up_to())

    text = "Методы и технологии программирования"
    print(f'\nГласных в строке "{text}": {count_vowels(text)}')

    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    print(f"\nИндекс числа {target}: {binary_search(numbers, target)}")


if __name__ == "__main__":
    main()
