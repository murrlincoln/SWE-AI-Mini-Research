def fibonacci(num: int) -> list:
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for _ in range(2, num):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
