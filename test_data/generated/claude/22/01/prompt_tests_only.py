def find_longest_substring_without_repeating_characters(text):
  chars = set()
  left = 0
  right = 0
  longest = 0
  
  while right < len(text):
    if text[right] not in chars:
      chars.add(text[right])
      right += 1
      longest = max(longest, right-left)
    else:
      chars.remove(text[left])
      left += 1
        
  return text[left:left+longest]
