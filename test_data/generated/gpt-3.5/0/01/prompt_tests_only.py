from typing import List

def sort_even_numbers(arr: List[int]) -> List[int]:
    even_numbers = [x for x in arr if x % 2 == 0]
    even_numbers.sort()
    
    result = []
    even_index = 0

    for num in arr:
        if num % 2 == 0:
            result.append(even_numbers[even_index])
            even_index += 1
        else:
            result.append(num)
    
    return result
