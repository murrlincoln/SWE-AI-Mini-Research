assert reverse_vowels('hiiii') == 'iiiih'
  assert reverse_vowels('oodji') == 'oijdo'
  assert reverse_vowels('s!@#$%^&*') == 's!@#$%^&*'

def reverse_vowels(word):
  vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
  word_list = list(word)
  i = 0
  j = len(word) - 1

  while i < j:
    if word_list[i] in vowels and word_list[j] in vowels:
      word_list[i], word_list[j] = word_list[j], word_list[i]
      i += 1
      j -= 1
    elif word_list[i] not in vowels:
      i += 1
    else:
      j -= 1

  return "".join(word_list)