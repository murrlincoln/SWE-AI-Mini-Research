def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k == 0:
        return ""
    
    n = len(text)
    longest_substring = ""
    
    for i in range(n):
        distinct_chars = {}
        for j in range(i, n):
            char = text[j]
            if char not in distinct_chars:
                if len(distinct_chars) == k:
                    break
                distinct_chars[char] = 0
            distinct_chars[char] += 1
            if j - i + 1 > len(longest_substring):
                longest_substring = text[i:j + 1]
    
    return longest_substring
