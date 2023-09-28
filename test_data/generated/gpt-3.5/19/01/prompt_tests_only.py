from typing import List

def fibonacci(num: int) -> List[int]:
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) <= num:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence
