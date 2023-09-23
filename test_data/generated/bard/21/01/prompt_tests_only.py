def find_first_non_repeating_char(text: str) -> str:
  """Finds the first non-repeating character in a string.

  Args:
    text: The string to search.

  Returns:
    The first non-repeating character in the string, or None if there is none.
  """

  seen = set()
  for char in text:
    if char in seen:
      continue
    seen.add(char)
    return char
  return None
