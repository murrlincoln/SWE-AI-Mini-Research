from typing import List

def max_product(nums: List[int]) -> int:
  product = 1
  for n in nums:
    product *= n
  return product
