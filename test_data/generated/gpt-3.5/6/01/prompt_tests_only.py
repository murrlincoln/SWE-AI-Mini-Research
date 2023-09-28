import re

def validate_email(email: str) -> bool:
    # Regular expression pattern for valid email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
    return bool(re.match(pattern, email))
