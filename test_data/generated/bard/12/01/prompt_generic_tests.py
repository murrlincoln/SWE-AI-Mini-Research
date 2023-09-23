def function(a: str) -> int:
  """Counts the number of vowels in a string.

  Args:
    a: A string.

  Returns:
    The number of vowels in the string.
  """

  count = 0
  for i in a:
    if i in "aeiou":
      count += 1
  return count
