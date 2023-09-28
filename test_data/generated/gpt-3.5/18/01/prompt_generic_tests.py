def function(a: int) -> int:
    if a == 0 or a == 1:
        return 1
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result
