def longest_common_substring(text1: str, text2: str) -> str:
  """Finds the longest common substring between two strings.

  Args:
    text1: The first string.
    text2: The second string.

  Returns:
    The longest common substring between the two strings.
  """

  table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
  longest_substring = ""
  longest_substring_length = 0

  for i in range(1, len(text1) + 1):
    for j in range(1, len(text2) + 1):
      if text1[i - 1] == text2[j - 1]:
        table[i][j] = table[i - 1][j - 1] + 1
        if table[i][j] > longest_substring_length:
          longest_substring_length = table[i][j]
          longest_substring = text1[i - longest_substring_length:i]
      else:
        table[i][j] = 0

  return longest_substring
