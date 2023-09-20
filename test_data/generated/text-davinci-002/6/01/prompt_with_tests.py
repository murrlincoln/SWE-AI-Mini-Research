def email_check(e):
  if '@' not in e or '.' not in e:
    return False
  else:
    return True