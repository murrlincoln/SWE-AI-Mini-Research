def longest_word(sentence: str) -> str:
  """Returns the longest word in a sentence.

  Args:
    sentence: A string.

  Returns:
    A string, the longest word in the sentence.
  """

  words = sentence.split()
  longest_word = ''
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word

