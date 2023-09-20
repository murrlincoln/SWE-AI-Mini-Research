def longest_word(sentence):
  """
  Returns the longest word in a given sentence.
  If there are ties, the first longest word is returned.
  """

  # YOUR CODE HERE
  if sentence=='':
    return ''
  words=sentence.split()
  return max(words, key=len)