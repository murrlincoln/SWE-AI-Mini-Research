def find_longest_substring_without_repeating_characters(text):
  char_set = set()
  l = 0
  res = ""
  for r in range(len(text)):
    while text[r] in char_set:
      char_set.remove(text[l])
      l += 1
    char_set.add(text[r])
    if (r - l + 1) > len(res):
      res = text[l:r+1]
  return res
