from typing import List

def max_product(nums: List[int]) -> int:
    if len(nums) < 2:
        raise ValueError("The input list must contain at least two integers.")

    max_num = max(nums)
    nums.remove(max_num)
    second_max_num = max(nums)

    return max_num * second_max_num
