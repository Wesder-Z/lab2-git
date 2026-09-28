"""Пример импорта и использования бинарного поиска."""

from search_utils import binary_search


def main() -> None:
    """Ищет число в демонстрационном списке."""
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    index = binary_search(numbers, target)

    if index is None:
        print(f"Число {target} не найдено")
    else:
        print(f"Число {target} найдено, индекс: {index}")


if __name__ == "__main__":
    main()

