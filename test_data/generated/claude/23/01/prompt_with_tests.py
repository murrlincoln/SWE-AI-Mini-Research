def longest_substring_with_k_distinct_characters(text, k):
  max_substr = ''
  for i in range(len(text)):
    substr = text[i] 
    chars = set(substr)
    while len(chars) <= k and i+len(substr) < len(text):
      substr += text[i+len(substr)]
      chars = set(substr)
    if len(chars) == k and len(substr) > len(max_substr):
      max_substr = substr
  return max_substr
