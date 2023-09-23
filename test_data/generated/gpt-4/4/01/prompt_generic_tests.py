from typing import List

def function(a: List[int]) -> int:
    return sum(abs(x) for x in a)
