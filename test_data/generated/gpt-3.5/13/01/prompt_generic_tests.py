def function(a: str) -> bool:
    # Check if the input string is empty or a palindrome
    return a == '' or a == a[::-1]
