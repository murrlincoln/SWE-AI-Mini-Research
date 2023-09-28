def count_occurrences(s: str, substr: str) -> int:
    count = 0
    start = 0
    while start < len(s):
        index = s.find(substr, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count
