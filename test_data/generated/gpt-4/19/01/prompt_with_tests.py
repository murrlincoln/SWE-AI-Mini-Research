def fibonacci(num: int) -> list:
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]
    
    fib_seq = [0, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > num:
            break
        fib_seq.append(next_num)
    
    return fib_seq
