import re

def validate_email(email):
  if re.match(r'[^@]+@[^@]+\.[^@]+', email):
    return True
  else:
    return False
