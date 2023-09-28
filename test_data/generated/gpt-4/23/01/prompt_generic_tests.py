def function(a: str, b: int) -> str:
    substrings = [a[i: j] for i in range(len(a)) for j in range(i + 1, len(a) + 1)]
    unique_substrings = [sub for sub in substrings if len(set(sub)) <= b]
    longest_substring = max(unique_substrings, key=len, default='')
    return longest_substring
