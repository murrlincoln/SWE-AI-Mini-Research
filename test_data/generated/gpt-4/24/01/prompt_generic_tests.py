def function(a: str) -> str:
    def longest_palindrome_substring(s: str) -> str:
        longest = ''
        for i in range(len(s)):
            # Check odd-length palindromes centered at i
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            # Check even-length palindromes centered at i
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1
        return longest

    return longest_palindrome_substring(a)
