"""Построение таблицы умножения."""


def build_multiplication_table(size: int = 10) -> list[list[int]]:
    """Создаёт квадратную таблицу умножения заданного размера.

    Args:
        size: Количество строк и столбцов таблицы.

    Returns:
        Таблица произведений чисел от 1 до ``size``.

    Raises:
        ValueError: Если размер таблицы меньше единицы.
    """
    if size < 1:
        raise ValueError("Размер таблицы должен быть положительным")

    return [
        [row * column for column in range(1, size + 1)]
        for row in range(1, size + 1)
    ]


def format_multiplication_table(size: int = 10) -> str:
    """Форматирует таблицу умножения для вывода в консоль."""
    table = build_multiplication_table(size)
    cell_width = len(str(size * size))
    return "\n".join(
        " ".join(f"{value:>{cell_width}}" for value in row)
        for row in table
    )


if __name__ == "__main__":
    print(format_multiplication_table())

