def max_product(nums: List[int]) -> int:
  max_product = float('-inf')
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      product = nums[i] * nums[j]
      max_product = max(max_product, product)
  return max_product
