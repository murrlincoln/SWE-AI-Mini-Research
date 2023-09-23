from typing import List

def sort_even_numbers(arr: List[int]) -> List[int]:
    even_numbers = [num for num in arr if num % 2 == 0]
    even_numbers.sort()
    sorted_arr = []
    even_index = 0
    for num in arr:
        if num % 2 == 0:
            sorted_arr.append(even_numbers[even_index])
            even_index += 1
        else:
            sorted_arr.append(num)
    return sorted_arr
