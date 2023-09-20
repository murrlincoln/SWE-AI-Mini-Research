def is_palindrome(string):
    """
    Function to check if a string is a palindrome
    :param string:
    :return: True or False
    """

    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False