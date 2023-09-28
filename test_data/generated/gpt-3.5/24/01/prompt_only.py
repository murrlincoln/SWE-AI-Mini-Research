def longest_palindromic_substring(text: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return text[left + 1:right]
    
    longest = ""
    
    for i in range(len(text)):
        # Check for odd-length palindromes
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Check for even-length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest
