def longest_common_substring(text1: str, text2: str) -> str:
    def lcp(strs, x, y, count):
        result = 0
        
        while (x + count < len(strs[0]) and
               y + count < len(strs[1]) and
               strs[0][x + count] == strs[1][y + count]):
            count += 1
            result = count
        
        return result

    strs = [text1, text2]
    result = 0
    end = 0

    for i in range(len(strs[0])):
        for j in range(len(strs[1])):
            if (i + result < len(strs[0]) and j + result < len(strs[1]) and
                    strs[0][i] == strs[1][j]):
                curr_result = lcp(strs, i, j, 0)
                if curr_result > result:
                    result = curr_result
                    end = i + curr_result
    
    return text1[end - result: end]
