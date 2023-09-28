def count_occurrences(s, substr):
    count = 0
    start = 0
    while True:
        start = s.find(substr, start)
        if start == -1:
            return count
        count += 1
        start += len(substr)
