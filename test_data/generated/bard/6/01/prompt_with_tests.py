import re

def validate_email(email: str) -> bool:
  """Validates an email address according to the following rules:

  - The email address must have at least one character before the "@" symbol.
  - The email address must have at least one character after the "@" symbol.
  - The email address must have at least one character after the "." symbol.
  - The email address must not contain any spaces.

  Args:
    email: The email address to validate.

  Returns:
    True if the email address is valid, False otherwise.
  """

  regex = r"[^@]+@[^@]+\.[^@]+"
  if not re.match(regex, email):
    return False

  if " " in email:
    return False

  return True
