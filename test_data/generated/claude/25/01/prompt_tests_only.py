def longest_common_substring(text1, text2):
  m = len(text1)
  n = len(text2)
  
  LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
 
  result = 0
  for i in range(m + 1):
    for j in range(n + 1):
      if (i == 0 or j == 0):
        LCSuff[i][j] = 0
      elif (text1[i-1] == text2[j-1]):
        LCSuff[i][j] = LCSuff[i-1][j-1] + 1
        result = max(result, LCSuff[i][j])
      else:
        LCSuff[i][j] = 0

  return text1[len(text1)-result:len(text1)]
