def is_palindrome(text):
  text = text.lower()
  text = text.replace(' ', '')
  
  return text == text[::-1]
