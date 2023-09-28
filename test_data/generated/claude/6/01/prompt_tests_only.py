import re

def validate_email(email: str) -> bool:
  regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
  return bool(re.search(regex, email))
