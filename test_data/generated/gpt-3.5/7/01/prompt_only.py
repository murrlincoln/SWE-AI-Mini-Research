def range_bitwise_and(m: int, n: int) -> int:
    while n > m:
        n = n & (n - 1)
    return n
