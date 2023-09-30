def longest_substring_with_k_distinct_characters(text, k):
  max_substr = ''
  for i in range(len(text)):
    substr = text[i]
    while len(set(substr)) <= k:
      i += 1
      if i == len(text):
        break
      substr += text[i]
    if len(substr) > len(max_substr):
      max_substr = substr
  return max_substr
