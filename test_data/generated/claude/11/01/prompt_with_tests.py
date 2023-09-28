from typing import List

def multiply_list(nums: List[int]) -> int:
  result = 1
  for num in nums:
    result *= num
  return result
