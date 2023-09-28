def function(a: str) -> str:
    if len(a) < 2:
        return a

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(a) and a[left] == a[right]:
            left -= 1
            right += 1
        return a[left + 1:right]

    longest_palindrome = ""
    for i in range(len(a)):
        # For odd length palindromes
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1

        # For even length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome
