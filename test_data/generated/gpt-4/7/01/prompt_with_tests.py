def range_bitwise_and(m: int, n: int) -> int:
    shift = 0
    # Find common 1-bits
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift
