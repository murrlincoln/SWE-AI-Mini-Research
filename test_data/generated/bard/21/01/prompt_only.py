def find_first_non_repeating_char(text: str) -> str:
  """Finds the first non-repeating character in a given string.

  Args:
    text: The string to search.

  Returns:
    The first non-repeating character in the string, or None if there is none.
  """

  seen = set()
  for char in text:
    if char not in seen:
      return char
    seen.add(char)
  return None
