from typing import List

def multiply_list(nums: List[int]) -> int:
    product = 1
    for num in nums:
        product *= num
    return product
