def count_occurrences(s: str, substr: str) -> int:
    count = 0
    index = 0
    
    while index < len(s):
        # Find the next occurrence of the substring in s
        next_index = s.find(substr, index)
        
        # If no more occurrences are found, exit the loop
        if next_index == -1:
            break
        
        # Increment the count and update the index to search for the next occurrence
        count += 1
        index = next_index + 1
    
    return count
