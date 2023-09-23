def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
  """Finds the longest substring with k distinct characters in a given string.

  Args:
    text: The string to search.
    k: The number of distinct characters in the substring.

  Returns:
    The longest substring with k distinct characters, or an empty string if no such
    substring exists.
  """

  start = 0
  end = 0
  max_length = 0
  max_substring = ''
  char_counts = {}

  while end < len(text):
    char = text[end]
    if char not in char_counts:
      char_counts[char] = 0
    char_counts[char] += 1

    while len(char_counts) > k:
      start_char = text[start]
      char_counts[start_char] -= 1
      if char_counts[start_char] == 0:
        del char_counts[start_char]
      start += 1

    current_length = end - start + 1
    if current_length > max_length:
      max_length = current_length
      max_substring = text[start:end + 1]
    end += 1

  return max_substring
