from typing import List

def function(a: List[int]) -> List[int]:
    even_numbers = [x for x in a if x % 2 == 0]
    odd_numbers = [x for x in a if x % 2 != 0]
    return odd_numbers + even_numbers
