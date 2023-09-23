def function(a: str) -> str:
  """Returns the first word in a string.

  Args:
    a: A string.

  Returns:
    The first word in the string, or an empty string if the string is empty.
  """

  return a.split()[0]
