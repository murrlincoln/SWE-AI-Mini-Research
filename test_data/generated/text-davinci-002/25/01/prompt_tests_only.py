def longest_common_substring(x, y):
  lcs = ''
  for i in range(min(len(x), len(y))):
    if x[i] == y[i]:
      lcs += x[i]
    else:
      break
  return lcs