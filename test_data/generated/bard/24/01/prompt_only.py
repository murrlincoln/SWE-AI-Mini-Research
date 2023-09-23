def longest_palindromic_substring(text: str) -> str:
  """Finds the longest palindromic substring in a given string.

  Args:
    text: The string to search.

  Returns:
    The longest palindromic substring in the given string.
  """

  n = len(text)
  table = [[0 for _ in range(n)] for _ in range(n)]

  # Initialize the table.
  for i in range(n):
    table[i][i] = 1

  # Fill in the table.
  for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
      if text[i] == text[j] and i + 1 == j:
        table[i][j] = 2
      elif text[i] == text[j]:
        table[i][j] = table[i + 1][j - 1] + 2
      else:
        table[i][j] = max(table[i + 1][j], table[i][j - 1])

  # Find the longest palindromic substring.
  max_length = 0
  start = 0
  for i in range(n):
    for j in range(i, n):
      if table[i][j] > max_length:
        max_length = table[i][j]
        start = i

  return text[start:start + max_length]
