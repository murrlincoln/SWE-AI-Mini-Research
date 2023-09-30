def longest_common_substring(text1, text2):
  m = len(text1)
  n = len(text2)
  
  LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

  result = 0
  pos = 0
  
  for i in range(m):
    for j in range(n):
      if text1[i] == text2[j]:
        LCSuff[i+1][j+1] = LCSuff[i][j] + 1
        if LCSuff[i+1][j+1] > result:
          result = LCSuff[i+1][j+1]
          pos = i + 1

  return text1[pos-result:pos]
