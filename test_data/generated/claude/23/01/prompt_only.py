def longest_substring_with_k_distinct_characters(text, k):
  longest = ''
  for i in range(len(text)):
    seen = set()
    current = ''
    for j in range(i, len(text)):
      if text[j] not in seen:
        seen.add(text[j])
        current += text[j]
        if len(seen) > k:
          break
      else:
        current += text[j]
    if len(current) > len(longest):
      longest = current
  return longest
