def function(a: str) -> str:
    if not a:
        return ""

    max_length = 0
    start_index = 0
    char_index_map = {}

    for end_index, char in enumerate(a):
        if char in char_index_map and char_index_map[char] >= start_index:
            start_index = char_index_map[char] + 1

        char_index_map[char] = end_index
        current_length = end_index - start_index + 1
        max_length = max(max_length, current_length)

    return a[start_index:start_index + max_length]
