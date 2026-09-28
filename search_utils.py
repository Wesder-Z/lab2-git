"""Алгоритмы поиска, подключаемые как отдельный модуль."""

from collections.abc import Sequence


def binary_search(values: Sequence[int], target: int) -> int | None:
    """Ищет число в отсортированной последовательности.

    Args:
        values: Последовательность целых чисел по возрастанию.
        target: Искомое число.

    Returns:
        Индекс найденного элемента или ``None``.

    Raises:
        ValueError: Если последовательность не отсортирована.
    """
    if any(left > right for left, right in zip(values, values[1:])):
        raise ValueError("Последовательность должна быть отсортирована")

    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = values[middle]

        if middle_value == target:
            return middle
        if middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return None
