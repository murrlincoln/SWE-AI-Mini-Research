def longest_common_substring(text1: str, text2: str) -> str:
  """Returns the longest common substring of two strings.

  Args:
    text1: The first string.
    text2: The second string.

  Returns:
    The longest common substring of the two strings.
  """

  n, m = len(text1), len(text2)
  dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if text1[i - 1] == text2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  longest_common_substring = ''
  i, j = n, m
  while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
      i -= 1
    elif dp[i][j] == dp[i][j - 1]:
      j -= 1
    else:
      longest_common_substring += text1[i - 1]
      i -= 1
      j -= 1

  return longest_common_substring[::-1]
