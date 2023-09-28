def function(a: str, b: int) -> str:
    if not a:
        return ''

    max_length = 0
    start = 0
    char_index = {}
    
    for end in range(len(a)):
        if a[end] in char_index and char_index[a[end]] >= start:
            start = char_index[a[end]] + 1

        char_index[a[end]] = end
        current_length = end - start + 1

        if current_length > max_length:
            max_length = current_length

    return a[start:start + max_length]
