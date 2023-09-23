def longest_palindromic_substring(text: str) -> str:
    if not text:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return text[left + 1:right]

    longest_palindrome = ""
    for i in range(len(text)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)

        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1

        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome
