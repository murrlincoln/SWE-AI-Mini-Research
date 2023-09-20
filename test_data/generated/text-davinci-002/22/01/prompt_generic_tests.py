assert function('pwwkew') == 'wke'

def function(s):
  max_substring = 0
  current_substring = 0
  current_letters = set()

  for i in range(len(s)):
    if s[i] in current_letters:
      current_letters = set(s[i])
      current_substring = 1
    else:
      current_letters.add(s[i])
      current_substring += 1
    if current_substring > max_substring:
      max_substring = current_substring
  return max_substring