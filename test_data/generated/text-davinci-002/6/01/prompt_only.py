The function should:

- have one parameter, `email`
- return `True` if the `email` is valid, `False` otherwise
- consider the email to be valid if:
  - it contains exactly one "@" character
  - the character before the "@" is not a space
  - the character after the "@" is not a space
  - there are at least 1 characters before the "@"
  - there are at least 3 characters after the "@"

def validate_email(email):
    if "@" not in email or " " in email or email.count("@") > 1:
        return False

    name, domain = email.split("@")
    return len(name) > 0 and len(domain) > 2