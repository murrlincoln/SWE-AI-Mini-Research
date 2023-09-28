def count_occurrences(s: str, substr: str) -> int:
  """Counts the number of occurrences of a substring in a string.

  Args:
    s: The string to search.
    substr: The substring to count.

  Returns:
    The number of occurrences of the substring in the string.
  """

  count = 0
  for i in range(len(s) - len(substr) + 1):
    if s[i:i + len(substr)] == substr:
      count += 1
  return count
