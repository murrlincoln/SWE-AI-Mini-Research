def find_longest_substring_without_repeating_characters(text: str) -> str:
    start = 0
    max_length = 0
    max_substring = ""
    char_index_map = {}

    for end in range(len(text)):
        if text[end] in char_index_map and char_index_map[text[end]] >= start:
            start = char_index_map[text[end]] + 1

        char_index_map[text[end]] = end
        current_length = end - start + 1

        if current_length > max_length:
            max_length = current_length
            max_substring = text[start:end + 1]

    return max_substring
