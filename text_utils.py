"""Функции для обработки текста, подключаемые как отдельный модуль."""

VOWELS = frozenset("аеёиоуыэюяaeiou")


def count_vowels(text: str) -> int:
    """Подсчитывает русские и английские гласные в строке."""
    return sum(character.lower() in VOWELS for character in text)

