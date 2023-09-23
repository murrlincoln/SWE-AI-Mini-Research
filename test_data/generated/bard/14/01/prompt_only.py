def longest_word(sentence: str) -> str:
  """Returns the longest word in a sentence.

  Args:
    sentence: A string containing the sentence.

  Returns:
    A string containing the longest word in the sentence.
  """

  words = sentence.split()
  longest_word = max(words, key=len)
  return longest_word
