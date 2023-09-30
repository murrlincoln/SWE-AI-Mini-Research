def longest_palindromic_substring(text):
  def find_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    return s[l+1:r]

  res = ""
  for i in range(len(text)):
    # odd length
    tmp = find_palindrome(text, i, i)
    if len(tmp) > len(res):
      res = tmp
    # even length  
    tmp = find_palindrome(text, i, i+1)
    if len(tmp) > len(res):
      res = tmp

  return res
