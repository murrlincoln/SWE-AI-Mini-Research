assert find_first_non_repeating_char('papper') == 'p'
  assert find_first_non_repeating_char('abcaaabbch rewarding') == 'r'

def find_first_non_repeating_char(text):
  for char in text:
    if char not in text:
      return char
  return '_'