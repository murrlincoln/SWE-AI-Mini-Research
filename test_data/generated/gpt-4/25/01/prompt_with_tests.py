def longest_common_substring(text1: str, text2: str) -> str:
    if not text1 or not text2:
        return ""

    m, n = len(text1), len(text2)
    longest_length = 0
    end_index = 0

    # Create a 2D table to store the lengths of common substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    end_index = i

    return text1[end_index - longest_length:end_index]
