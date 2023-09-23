def find_longest_substring_without_repeating_characters(text: str) -> str:
    start = 0  # Start of the current substring
    max_len = 0  # Length of the longest substring
    start_max = 0  # Start of the longest substring
    last_seen = {}  # Dictionary to store the last index where each character was seen

    for i, char in enumerate(text):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            start_max = start

    return text[start_max:start_max + max_len]
