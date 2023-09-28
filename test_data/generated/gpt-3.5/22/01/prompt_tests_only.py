def find_longest_substring_without_repeating_characters(text: str) -> str:
    if not text:
        return ""

    max_length = 0
    start = 0
    char_index_map = {}
    longest_substring = ""

    for end in range(len(text)):
        if text[end] in char_index_map and char_index_map[text[end]] >= start:
            start = char_index_map[text[end]] + 1
        char_index_map[text[end]] = end

        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substring = text[start:end + 1]

    return longest_substring
