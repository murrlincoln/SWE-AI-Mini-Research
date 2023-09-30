def longest_palindromic_substring(text):
  def expand(left, right):
    while left >= 0 and right < len(text) and text[left] == text[right]:
      left -= 1
      right += 1
    return text[left+1:right]
    
  if len(text) < 2:
    return text
  
  longest = ''
  for i in range(len(text)):
    odd = expand(i, i)
    even = expand(i, i+1)
    palindrome = max(odd, even, key=len)
    if len(palindrome) > len(longest):
      longest = palindrome
      
  return longest
