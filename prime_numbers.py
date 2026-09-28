"""Поиск простых чисел."""


def is_prime(number: int) -> bool:
    """Проверяет, является ли целое число простым."""
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def prime_numbers_up_to(limit: int = 100) -> list[int]:
    """Возвращает простые числа, не превышающие заданную границу."""
    return [number for number in range(2, limit + 1) if is_prime(number)]


if __name__ == "__main__":
    print(*prime_numbers_up_to())

