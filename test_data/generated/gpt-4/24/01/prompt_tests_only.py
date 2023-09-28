def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindromic_substring(text: str) -> str:
    if not text or len(text) < 1:
        return ""
    start = 0
    end = 0
    for i in range(len(text)):
        len1 = expand_around_center(text, i, i)
        len2 = expand_around_center(text, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return text[start:end + 1]
