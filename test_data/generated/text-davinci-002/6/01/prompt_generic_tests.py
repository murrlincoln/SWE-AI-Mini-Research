Write a Python function to check whether a string is a valid email address or not.

def is_valid_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):  
        return True  
    else:  
        return False