def range_bitwise_and(m: int, n: int) -> int:
  """Calculates the bitwise AND of all numbers in a range from m to n.

  Args:
    m: The start of the range.
    n: The end of the range.

  Returns:
    The bitwise AND of all numbers in the range.
  """

  result = m
  for i in range(m + 1, n + 1):
    result &= i
  return result
