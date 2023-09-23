def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
  """Finds the longest substring with k distinct characters in a given string.

  Args:
    text: The string to search.
    k: The number of distinct characters in the substring.

  Returns:
    The longest substring with k distinct characters, or an empty string if no
    such substring exists.
  """

  # Create a dictionary to store the characters in the current substring and their
  # frequencies.
  substring_chars = {}

  # Initialize the start and end indices of the longest substring.
  longest_substring_start = 0
  longest_substring_end = 0

  # Iterate over the characters in the text.
  for i in range(len(text)):
    # Add the current character to the dictionary.
    substring_chars[text[i]] = substring_chars.get(text[i], 0) + 1

    # If the number of distinct characters in the substring is greater than k,
    # remove the character at the start of the substring.
    while len(substring_chars) > k:
      substring_chars[text[longest_substring_start]] -= 1
      if substring_chars[text[longest_substring_start]] == 0:
        del substring_chars[text[longest_substring_start]]
      longest_substring_start += 1

    # If the length of the current substring is greater than the length of the
    # longest substring, update the longest substring indices.
    if i - longest_substring_start + 1 > longest_substring_end - longest_substring_start:
      longest_substring_start = longest_substring_start
      longest_substring_end = i + 1

  # Return the longest substring.
  return text[longest_substring_start:longest_substring_end]
