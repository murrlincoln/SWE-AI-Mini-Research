def capitalize(text):
  words = text.split()
  capitalized_words = [word.capitalize() for word in words]
  return ' '.join(capitalized_words)
