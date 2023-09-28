def count_occurrences(s: str, substr: str) -> int:
    count = 0
    substr_length = len(substr)
    for i in range(len(s) - substr_length + 1):
        if s[i:i + substr_length] == substr:
            count += 1
    return count
