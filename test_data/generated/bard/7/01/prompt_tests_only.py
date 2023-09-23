def range_bitwise_and(m: int, n: int) -> int:
  """Returns the bitwise AND of all integers in the range [m, n] inclusive."""
  result = m
  for i in range(m + 1, n + 1):
    result &= i
  return result
