def longest_palindromic_substring(text): 
    if text == None or len(text) < 1: 
        return None 
        
    start, end = 0, 0 
    for i in range(len(text)): 
        len1 = expand_around_center(text, i, i) 
        len2 = expand_around_center(text, i, i+1) 
        l max(len1, len2) 
        if l > end - start: 
            start = i - (l-1)/2
            end = i + l/2 
    return text[start:end+1] 

def expand_around_center(s, left, right): 
    while left >= 0 and right < len(s) and s[left]== s[right]: 
        left -=1 
        right += 1 
    return right - left - 1