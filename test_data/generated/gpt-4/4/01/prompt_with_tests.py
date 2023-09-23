from typing import List

def max_product(nums: List[int]) -> int:
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])
