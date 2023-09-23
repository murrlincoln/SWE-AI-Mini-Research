import re

def validate_email(email: str) -> bool:
    regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    if regex.match(email):
        return True
    return False
