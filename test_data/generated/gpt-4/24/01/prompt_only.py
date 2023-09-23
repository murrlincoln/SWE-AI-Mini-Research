def expand_from_center(left: int, right: int, text: str) -> str:
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return text[left+1:right]

def longest_palindromic_substring(text: str) -> str:
    if not text:
        return ""
    
    longest = ""
    for i in range(len(text)):
        # Odd length palindrome
        palindrome1 = expand_from_center(i, i, text)
        # Even length palindrome
        palindrome2 = expand_from_center(i, i+1, text)
        
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
            
    return longest
