def longestPalindromicSubstring(string):
  longest = ''

  for i in range (len(string)):
    for j in range (i, len(string)):
      substring = string[i:j + 1]

      if len(substring) > len(longest) and substring == substring[::-1]:
        longest = substring

  return longest