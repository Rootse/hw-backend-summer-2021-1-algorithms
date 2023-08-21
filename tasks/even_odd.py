__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    sum_even = sum(i for i in arr if i & 1)
    sum_odd = sum(i for i in arr if not i & 1)

    return sum_even / sum_odd if sum_odd else 0
