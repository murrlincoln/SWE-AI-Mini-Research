def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    
    if not text or k == 0:
        return ""
    
    start = 0
    end = 1
    longest = text[0]
    chars = set(text[0])
    
    while end < len(text):
        chars.add(text[end])
        if len(chars) <= k:
            # update the longest substring if necessary
            if end-start+1 > len(longest):
                longest = text[start:end+1]
        else:
            # otherwise, move the start pointer and remove a character from the set
            start += 1
            chars.remove(text[start-1])
        end += 1
    
    return longest