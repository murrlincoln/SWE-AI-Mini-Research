def multiply_list(nums: list) -> int:
  """
  Multiply all the elements in a list.

  Args:
    nums: A list of numbers.

  Returns:
    The product of all the elements in the list.
  """

  product = 1
  for num in nums:
    product *= num
  return product
