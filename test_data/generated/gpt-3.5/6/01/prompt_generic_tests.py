import re

def function(a: str) -> bool:
    # Use a regular expression to check if the input matches the email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_pattern, a))
