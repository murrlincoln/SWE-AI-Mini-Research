def find_first_non_repeating_char(text: str) -> str:
  """
  Finds the first non-repeating character in a given string.

  Args:
    text: The string to search.

  Returns:
    The first non-repeating character in the string, or None if there is none.
  """

  char_counts = {}
  for char in text:
    if char not in char_counts:
      char_counts[char] = 0
    char_counts[char] += 1

  for char in text:
    if char_counts[char] == 1:
      return char
  return None
