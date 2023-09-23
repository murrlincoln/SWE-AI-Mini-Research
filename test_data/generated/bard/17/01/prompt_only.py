def count_digits(num: int) -> int:
  """Counts the number of digits in a number.

  Args:
    num: The number to count the digits of.

  Returns:
    The number of digits in the number.
  """

  count = 0
  while num > 0:
    num //= 10
    count += 1
  return count
