import re


def validate_email(email: str) -> bool:
  """Validates an email address according to certain rules.

  Args:
    email: The email address to validate.

  Returns:
    True if the email address is valid, False otherwise.
  """

  regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  if re.match(regex, email):
    return True
  else:
    return False

