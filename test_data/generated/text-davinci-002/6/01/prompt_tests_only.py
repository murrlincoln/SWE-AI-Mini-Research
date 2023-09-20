assert validate_email('@example.com') == False')

def validate_email(email):
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return True
    return False