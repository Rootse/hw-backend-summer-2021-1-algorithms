__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number < 2:
        return False

    if number % 2 == 0:
        return number == 2

    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True
