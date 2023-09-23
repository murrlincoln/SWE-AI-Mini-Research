def count_digits(num: int) -> int:
  """Counts the number of digits in an integer.

  Args:
    num: An integer.

  Returns:
    The number of digits in the integer.
  """

  count = 0
  while num > 0:
    num //= 10
    count += 1
  return count
