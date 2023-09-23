def fibonacci(num: int) -> list:
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, num + 1):
            fib.append(fib[i-1] + fib[i-2])
        return fib
