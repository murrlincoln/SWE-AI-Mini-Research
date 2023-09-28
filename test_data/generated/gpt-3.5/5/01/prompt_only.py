def count_occurrences(s: str, substr: str) -> int:
    count = 0
    index = 0
    
    while index < len(s):
        index = s.find(substr, index)
        if index == -1:
            break
        count += 1
        index += len(substr)
    
    return count
