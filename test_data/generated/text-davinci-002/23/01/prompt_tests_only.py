def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
  if k == 0:
    return ''
  
  substr = ''
  longest = ''
  for i in range(len(text)):
    if text[i] in substr:
      continue
    elif len(substr) < k:
      substr += text[i]
    else:
      if len(substr) > len(longest):
        longest = substr
      substr = text[i-k+1:i+1]
  
  if len(substr) > len(longest):
    longest = substr
  
  return longest