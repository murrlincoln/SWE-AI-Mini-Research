def count_vowels(text):
  count = 0
  for character in text:
    if character in "aeiouAEIOU":
      count += 1
  return count