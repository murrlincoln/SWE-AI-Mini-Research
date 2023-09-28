import re

def validate_email(email: str) -> bool:
  if len(email) > 254:
    return False

  regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  return bool(re.match(regex, email))
