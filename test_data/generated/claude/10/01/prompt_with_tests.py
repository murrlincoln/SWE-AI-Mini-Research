def factorial_recursive_2(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive_2(n-1)
