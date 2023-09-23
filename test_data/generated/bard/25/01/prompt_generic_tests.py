def function(a: str, b: str) -> str:
  """Returns the longest common substring of two strings.

  Args:
    a: The first string.
    b: The second string.

  Returns:
    The longest common substring of a and b.
  """

  n, m = len(a), len(b)
  dp = [[0] * (m + 1) for _ in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if a[i - 1] == b[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  lcs = ""
  i, j = n, m
  while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
      i -= 1
    elif dp[i][j] == dp[i][j - 1]:
      j -= 1
    else:
      lcs += a[i - 1]
      i -= 1
      j -= 1
  return lcs[::-1]
