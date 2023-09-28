def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k <= 0:
        return ""

    start = 0
    max_length = 0
    max_start = 0
    char_count = {}
    
    for end in range(len(text)):
        char = text[end]
        
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
        
        while len(char_count) > k:
            left_char = text[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1
        
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_start = start
    
    return text[max_start:max_start + max_length]
