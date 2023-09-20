def count_digits(num):
  """
  >>> count_digits(0)
  1
  >>> count_digits(5)
  1
  >>> count_digits(348)
  3
  """
  count = 0
  if num == 0:
    return 1
  while num > 0:
    count += 1
    num //= 10
  return count