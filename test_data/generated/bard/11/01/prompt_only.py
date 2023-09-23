def multiply_list(nums: list) -> int:
  """
  Multiplies all the numbers in a list.

  Args:
    nums: A list of numbers.

  Returns:
    The product of all the numbers in the list.
  """

  product = 1
  for num in nums:
    product *= num
  return product
