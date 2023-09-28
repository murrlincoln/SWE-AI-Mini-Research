def find_first_non_repeating_char(text: str) -> str:
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in text:
        if char_count[char] == 1:
            return char
    
    return ''
