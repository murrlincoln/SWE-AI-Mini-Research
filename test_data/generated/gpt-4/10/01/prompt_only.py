def factorial_recursive_2(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive_2(n - 1)
