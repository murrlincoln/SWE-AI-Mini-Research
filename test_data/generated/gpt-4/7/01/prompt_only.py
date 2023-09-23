def range_bitwise_and(m: int, n: int) -> int:
    shift = 0
    # Shift m and n to the right until they are the same,
    # keeping track of the number of shifts needed.
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1
    # Shift m (or n, they are the same now) back to the left by the number of shifts needed.
    return m << shift
