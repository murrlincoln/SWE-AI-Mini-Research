def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k == 0 or not text:
        return ''
    
    char_index = {}  # Holds the latest index of each character
    max_length = 0
    substring_start = 0
    longest_substring = ''
    
    for index, char in enumerate(text):
        char_index[char] = index  # Update the latest index of the character
        
        if len(char_index) > k:
            # If there are more than k distinct characters, remove the leftmost character
            # from char_index and update substring_start to the next character
            leftmost_char_index = min(char_index.values())
            del char_index[text[leftmost_char_index]]
            substring_start = leftmost_char_index + 1
        
        # Update max_length and longest_substring if a longer substring is found
        if index - substring_start + 1 > max_length:
            max_length = index - substring_start + 1
            longest_substring = text[substring_start:index + 1]
            
    return longest_substring
