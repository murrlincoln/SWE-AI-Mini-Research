def count_digits(num: int) -> int:
    if num == 0:
        return 1
    else:
        count = 0
        while num != 0:
            num //= 10
            count += 1
        return count
