def find_longest_substring_without_repeating_characters(text: str) -> str:
    start = 0
    max_length = 0
    max_substring = ""
    used_chars = {}

    for i, char in enumerate(text):
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        else:
            if i - start + 1 > max_length:
                max_length = i - start + 1
                max_substring = text[start:i+1]
        used_chars[char] = i

    return max_substring
