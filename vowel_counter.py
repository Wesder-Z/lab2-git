"""Консольная программа для подсчёта гласных."""

import sys

from text_utils import count_vowels


def main() -> None:
    """Получает текст из аргументов или из стандартного ввода."""
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Введите текст: ")

    print(f"Количество гласных: {count_vowels(text)}")


if __name__ == "__main__":
    main()
