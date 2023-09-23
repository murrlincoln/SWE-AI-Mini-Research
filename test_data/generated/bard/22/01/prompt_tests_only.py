def find_longest_substring_without_repeating_characters(text: str) -> str:
  """Finds the longest substring without repeating characters.

  Args:
    text: The string to search.

  Returns:
    The longest substring without repeating characters.
  """

  start = 0
  end = 0
  max_length = 0
  seen = set()

  while end < len(text):
    if text[end] not in seen:
      seen.add(text[end])
      end += 1
      max_length = max(max_length, end - start)
    else:
      seen.remove(text[start])
      start += 1

  return text[start:end]
