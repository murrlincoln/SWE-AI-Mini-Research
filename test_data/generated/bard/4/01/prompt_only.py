def max_product(nums: List[int]) -> int:
  """Finds the maximum product of any two integers in a given list.

  Args:
    nums: A list of integers.

  Returns:
    The maximum product of any two integers in the list.
  """

  # Check if the list is empty.
  if not nums:
    return 0

  # Sort the list in ascending order.
  nums.sort()

  # Get the maximum product of the first two and last two elements.
  max_product = max(nums[0] * nums[1], nums[-1] * nums[-2])

  # Iterate over the list and find the maximum product of any two consecutive elements.
  for i in range(1, len(nums) - 1):
    max_product = max(max_product, nums[i] * nums[i + 1])

  return max_product
