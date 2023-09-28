def function(a: str) -> str:
    # Initialize a dictionary to store character frequencies
    char_count = {}
    
    # Iterate through the string 'a' and count the frequency of each character
    for char in a:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Iterate through the characters and return the first character with a frequency of 1
    for char in a:
        if char_count[char] == 1:
            return char
    
    # If no unique character is found, return an empty string
    return ''
