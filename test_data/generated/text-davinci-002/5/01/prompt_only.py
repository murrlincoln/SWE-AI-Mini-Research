def count_occurrences(s: str, substr: str) -> int:
    """Returns the number of times substr appears in s."""
    count = 0
    i = 0
    while i < len(s) - len(substr) + 1:
        if s[i : i + len(substr)] == substr:
            count += 1
        i += 1
    return count