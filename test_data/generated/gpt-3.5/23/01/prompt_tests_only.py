def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k == 0:
        return ""

    char_count = {}
    max_len = 0
    start = 0
    max_start = 0

    for end in range(len(text)):
        char = text[end]
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            start_char = text[start]
            char_count[start_char] -= 1
            if char_count[start_char] == 0:
                del char_count[start_char]
            start += 1

        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_start = start

    return text[max_start:max_start + max_len]
