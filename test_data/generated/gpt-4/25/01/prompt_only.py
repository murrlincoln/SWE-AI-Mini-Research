def longest_common_substring(text1: str, text2: str) -> str:
    def find_longest_common_suffix(text1: str, text2: str, start1: int, start2: int) -> int:
        length = 0
        while start1 + length < len(text1) and start2 + length < len(text2) and text1[start1 + length] == text2[start2 + length]:
            length += 1
        return length

    max_length = 0
    max_substring = ""
    
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                common_length = find_longest_common_suffix(text1, text2, i, j)
                if common_length > max_length:
                    max_length = common_length
                    max_substring = text1[i:i + common_length]

    return max_substring
