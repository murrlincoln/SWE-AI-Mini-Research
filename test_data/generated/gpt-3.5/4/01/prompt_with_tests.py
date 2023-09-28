from typing import List

def max_product(nums: List[int]) -> int:
    # Sort the list in ascending order
    nums.sort()
    
    # The maximum product will either be the product of the two largest positive numbers
    # or the product of the two largest negative numbers (if there are more than two negative numbers).
    return max(nums[-1] * nums[-2], nums[0] * nums[1])
