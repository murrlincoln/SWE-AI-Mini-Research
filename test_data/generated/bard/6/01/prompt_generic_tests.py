import re

def function(a: str) -> bool:
  """Returns True if the given string is a valid email address, False otherwise."""
  email_regex = r"[^@]+@[^@]+\.[^@]+"
  return re.match(email_regex, a) is not None
