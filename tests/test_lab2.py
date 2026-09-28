"""Модульные тесты заданий лабораторной работы №2."""

import unittest

from multiplication_table import build_multiplication_table
from prime_numbers import is_prime, prime_numbers_up_to
from search_utils import binary_search
from text_utils import count_vowels


class MultiplicationTableTests(unittest.TestCase):
    """Проверки таблицы умножения."""

    def test_builds_table_from_one_to_ten(self) -> None:
        table = build_multiplication_table()

        self.assertEqual(len(table), 10)
        self.assertEqual(table[0], list(range(1, 11)))
        self.assertEqual(table[-1], list(range(10, 101, 10)))

    def test_rejects_non_positive_size(self) -> None:
        with self.assertRaises(ValueError):
            build_multiplication_table(0)


class PrimeNumberTests(unittest.TestCase):
    """Проверки поиска простых чисел."""

    def test_finds_all_prime_numbers_up_to_one_hundred(self) -> None:
        expected = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97,
        ]

        self.assertEqual(prime_numbers_up_to(100), expected)

    def test_handles_numbers_below_two(self) -> None:
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))


class VowelCounterTests(unittest.TestCase):
    """Проверки подсчёта гласных."""

    def test_counts_russian_and_english_vowels(self) -> None:
        self.assertEqual(count_vowels("Привет, Python!"), 3)

    def test_handles_uppercase_and_empty_text(self) -> None:
        self.assertEqual(count_vowels("АЕЁИОУЫЭЮЯ"), 10)
        self.assertEqual(count_vowels(""), 0)


class BinarySearchTests(unittest.TestCase):
    """Проверки бинарного поиска."""

    def test_finds_first_middle_and_last_items(self) -> None:
        values = [2, 5, 8, 12, 16, 23, 38]

        self.assertEqual(binary_search(values, 2), 0)
        self.assertEqual(binary_search(values, 12), 3)
        self.assertEqual(binary_search(values, 38), 6)

    def test_returns_none_for_missing_item(self) -> None:
        self.assertIsNone(binary_search([2, 5, 8, 12], 7))
        self.assertIsNone(binary_search([], 7))

    def test_rejects_unsorted_sequence(self) -> None:
        with self.assertRaises(ValueError):
            binary_search([2, 8, 5, 12], 5)


if __name__ == "__main__":
    unittest.main()
