def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("Input should be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
