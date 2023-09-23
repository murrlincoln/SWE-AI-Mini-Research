def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k == 0:
        return ""

    n = len(text)
    left, right = 0, 0
    char_count = {}
    max_len = 0
    max_start = 0

    while right < n:
        if text[right] not in char_count:
            char_count[text[right]] = 0
        char_count[text[right]] += 1

        while len(char_count) > k:
            char_count[text[left]] -= 1
            if char_count[text[left]] == 0:
                del char_count[text[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left

        right += 1

    return text[max_start:max_start + max_len]
