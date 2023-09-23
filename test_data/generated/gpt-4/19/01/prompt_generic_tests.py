def function(a: int) -> list:
    if a == 0:
        return [0]
    elif a == 1:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, a):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
