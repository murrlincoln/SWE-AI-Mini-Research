from typing import List

def fibonacci(num: int) -> List[int]:
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    
    sequence = [0, 1]
    while len(sequence) < num:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence
