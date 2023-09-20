def test_y_counts():
  text = 'happy'
  assert count_vowels(text) == 2

def count_vowels(text):
  # fill in your code here
  count = 0
  for letter in text:
    if letter in 'aeiou':
      count = count + 1
  return count