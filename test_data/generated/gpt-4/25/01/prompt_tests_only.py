def longest_common_substring(text1: str, text2: str) -> str:
    def find_longest_common_suffix(text1: str, text2: str) -> str:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        max_length = 0
        ending_index = 0

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        ending_index = i

        return text1[ending_index - max_length:ending_index]

    return find_longest_common_suffix(text1, text2)
