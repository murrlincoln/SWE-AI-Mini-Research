from typing import List

def function(a: int) -> List[int]:
    if a == 0:
        return [0]
    
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= a:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence
