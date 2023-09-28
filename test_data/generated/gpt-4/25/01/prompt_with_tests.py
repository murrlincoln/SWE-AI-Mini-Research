def longest_common_substring(text1: str, text2: str) -> str:
    def lcp(strs):
        if not strs: return ""
        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        return shortest_str
    
    substrings_text1 = {text1[i:j + 1] for i in range(len(text1)) for j in range(i, len(text1))}
    substrings_text2 = {text2[i:j + 1] for i in range(len(text2)) for j in range(i, len(text2))}
    
    common_substrings = substrings_text1.intersection(substrings_text2)
    
    if not common_substrings:
        return ""
    
    return max(common_substrings, key=len)
