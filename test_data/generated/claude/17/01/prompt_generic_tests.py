def digit_sum(a: int) -> int:
    total = 0
    while a > 0:
        total += a % 10
        a //= 10
    return total
