def range_bitwise_and(m, n):
    result = m
    for i in range(m+1, n+1):
        result &= i
    return result
