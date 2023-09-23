def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
  """
  Finds the longest substring of the given text that contains at most k distinct characters.

  Args:
    text: The text to search.
    k: The maximum number of distinct characters allowed in the substring.

  Returns:
    The longest substring of the given text that contains at most k distinct characters.
  """

  # Create a dictionary to store the character counts.
  char_counts = {}

  # Initialize the start and end indices of the longest substring.
  start_idx = 0
  end_idx = 0

  # Iterate over the text.
  for i in range(len(text)):
    # Add the current character to the dictionary.
    char_counts[text[i]] = char_counts.get(text[i], 0) + 1

    # If the number of distinct characters in the current substring is greater than k,
    # remove the character at the start of the substring from the dictionary.
    while len(char_counts) > k:
      char_counts[text[start_idx]] -= 1
      if char_counts[text[start_idx]] == 0:
        del char_counts[text[start_idx]]
      start_idx += 1

    # Update the end index of the longest substring.
    end_idx = i + 1

  # Return the longest substring.
  return text[start_idx:end_idx]

