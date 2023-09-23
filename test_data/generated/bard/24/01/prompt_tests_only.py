def longest_palindromic_substring(text: str) -> str:
  """Returns the longest palindromic substring of the given text.

  Args:
    text: The text to search for the longest palindromic substring.

  Returns:
    The longest palindromic substring of the given text.
  """

  n = len(text)
  dp = [[False for _ in range(n)] for _ in range(n)]

  # Initialize the base cases.
  for i in range(n):
    dp[i][i] = True

  # Iterate over the length of the substring.
  for length in range(2, n + 1):
    for i in range(n - length + 1):
      j = i + length - 1

      # If the first and last characters are the same, then the substring is a
      # palindrome if the substring in between is also a palindrome.
      if text[i] == text[j] and dp[i + 1][j - 1]:
        dp[i][j] = True

  # Find the longest palindromic substring.
  longest_palindromic_substring = ''
  for i in range(n):
    for j in range(i, n):
      if dp[i][j] and len(text[i:j + 1]) > len(longest_palindromic_substring):
        longest_palindromic_substring = text[i:j + 1]

  return longest_palindromic_substring

