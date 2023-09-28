def longest_common_substring(text1: str, text2: str) -> str:
    def find_longest_common_suffix(text1: str, text2: str):
        n1, n2 = len(text1), len(text2)
        max_len, end_index = 0, 0
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i - 1

        return text1[end_index - max_len + 1:end_index + 1]

    return find_longest_common_suffix(text1, text2)
