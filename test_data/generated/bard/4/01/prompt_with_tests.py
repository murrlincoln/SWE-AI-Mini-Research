def max_product(nums: List[int]) -> int:
  """Finds the maximum product of any two integers in a given list.

  Args:
    nums: A list of integers.

  Returns:
    The maximum product of any two integers in the list.
  """

  # Initialize the maximum product.
  max_product = nums[0] * nums[1]

  # Iterate over the list, multiplying each pair of elements and comparing the
  # product to the maximum product.
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      product = nums[i] * nums[j]
      if product > max_product:
        max_product = product

  # Return the maximum product.
  return max_product
