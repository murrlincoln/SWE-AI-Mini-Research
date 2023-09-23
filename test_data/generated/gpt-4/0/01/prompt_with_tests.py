from typing import List

def sort_even_numbers(arr: List[int]) -> List[int]:
    evens = sorted([num for num in arr if num % 2 == 0])
    even_index = 0
    sorted_arr = arr.copy()
    
    for i, num in enumerate(arr):
        if num % 2 == 0:
            sorted_arr[i] = evens[even_index]
            even_index += 1
    
    return sorted_arr
