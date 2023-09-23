def function(a: list) -> int:
  """
  Returns the sum of all elements in the list.

  Args:
    a: A list of integers.

  Returns:
    The sum of all elements in the list.
  """

  sum = 0
  for i in a:
    sum += i
  return sum
