def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k == 0:
        return ""
    
    char_index = {}  # dictionary to keep track of the last index at which each character appears
    max_length = 0
    max_substr = ""
    left = 0  # left pointer to the current substring
    
    for right in range(len(text)):
        char = text[right]
        char_index[char] = right  # update the last index at which this character appears
        
        # If the substring has more than k distinct characters,
        # move the left pointer to the right
        while len(char_index) > k:
            left_char = text[left]
            if char_index[left_char] == left:
                del char_index[left_char]  # remove characters that are no longer in the substring
            left += 1
        
        # Update the result if we get a larger window
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_substr = text[left:right+1]
            
    return max_substr
