def count_digits(num):
    """
    Input: num = an integer
    Output: the number of digits in the integer
    """
    
    # Base case
    if num == 0:
        return 1
    
    # Recursive case: keep incrementing the count until num becomes 0
    return 1 + count_digits(num // 10)