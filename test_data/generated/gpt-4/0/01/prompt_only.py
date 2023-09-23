from typing import List

def sort_even_numbers(arr: List[int]) -> List[int]:
    evens = sorted([num for num in arr if num % 2 == 0])
    even_index = 0
    sorted_arr = []
    
    for num in arr:
        if num % 2 == 0:
            sorted_arr.append(evens[even_index])
            even_index += 1
        else:
            sorted_arr.append(num)
    
    return sorted_arr
