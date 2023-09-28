def factorial_recursive_2(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_recursive_2(n - 1)
