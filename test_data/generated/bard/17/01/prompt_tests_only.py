def count_digits(num: int) -> int:
  """Counts the number of digits in a given integer.

  Args:
    num: The integer to count the digits of.

  Returns:
    The number of digits in the given integer.
  """

  count = 0
  while num > 0:
    num //= 10
    count += 1
  return count
