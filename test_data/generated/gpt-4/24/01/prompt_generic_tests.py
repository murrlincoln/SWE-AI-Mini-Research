def function(a: str) -> str:
    if not a:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(a) and a[left] == a[right]:
            left -= 1
            right += 1
        return a[left + 1:right]

    longest_palindrome = ""
    
    for i in range(len(a)):
        # Odd-length palindrome
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        
        # Even-length palindrome
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome
