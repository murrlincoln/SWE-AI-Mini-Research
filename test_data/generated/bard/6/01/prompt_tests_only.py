import re

def validate_email(email: str) -> bool:
  """Validates an email address.

  Args:
    email: The email address to validate.

  Returns:
    True if the email address is valid, False otherwise.
  """

  regex = r"[^@]+@[^@]+\.[^@]+"
  return re.match(regex, email) is not None
