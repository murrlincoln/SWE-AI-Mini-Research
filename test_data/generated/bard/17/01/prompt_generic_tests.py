def function(a: int) -> int:
  """
  Returns the number of digits in the given integer.

  Args:
    a: An integer.

  Returns:
    The number of digits in the given integer.
  """

  count = 0
  while a > 0:
    a //= 10
    count += 1
  return count
