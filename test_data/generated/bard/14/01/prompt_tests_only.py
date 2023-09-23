def longest_word(sentence: str) -> str:
  """Returns the longest word in the given sentence.

  Args:
    sentence: A string representing the sentence.

  Returns:
    A string representing the longest word in the sentence.
  """

  words = sentence.split()
  if not words:
    return ''
  return max(words, key=len)
