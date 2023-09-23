def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    n = len(text)
    if k == 0 or n == 0:
        return ""

    # Using sliding window approach
    left, right = 0, 0
    char_frequency = {}
    max_length = 0
    max_substr = ""

    while right < n:
        char = text[right]
        char_frequency[char] = char_frequency.get(char, 0) + 1

        while len(char_frequency) > k:
            left_char = text[left]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            left += 1

        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_substr = text[left:right+1]

        right += 1

    return max_substr
