def function(a: List[int]) -> int:
  """A function that returns the sum of the absolute values of the elements in a list.

  Args:
    a: A list of integers.

  Returns:
    The sum of the absolute values of the elements in a.
  """

  sum = 0
  for element in a:
    sum += abs(element)
  return sum
