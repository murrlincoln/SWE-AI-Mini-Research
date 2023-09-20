def longest_word(sentence): 
  words = sentence.split() 
  max_len = len(words[0]) 
  longest_word = words[0] 
  for word in words[1:]: 
    if len(word) > max_len: 
      max_len = len(word) 
      longest_word = word 
      return longest_word