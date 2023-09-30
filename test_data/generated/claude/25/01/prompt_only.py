def longest_common_substring(text1, text2):
  m = len(text1)
  n = len(text2)
  
  longest = ""
  for i in range(m):
    for j in range(n):
      temp = ""
      k = 0
      while i + k < m and j + k < n and text1[i+k] == text2[j+k]:
        temp += text1[i+k]
        k += 1
      if len(temp) > len(longest):
        longest = temp
        
  return longest
