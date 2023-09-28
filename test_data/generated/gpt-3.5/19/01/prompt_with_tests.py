from typing import List

def fibonacci(num: int) -> List[int]:
    if num <= 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while fib_sequence[-1] + fib_sequence[-2] <= num:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
