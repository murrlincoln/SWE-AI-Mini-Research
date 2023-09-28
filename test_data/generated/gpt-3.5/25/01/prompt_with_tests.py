def longest_common_substring(text1: str, text2: str) -> str:
    if not text1 or not text2:
        return ""

    m, n = len(text1), len(text2)
    longest_len = 0
    end_idx = 0

    # Create a table to store the length of the common substring at each (i, j) position
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_len:
                    longest_len = dp[i][j]
                    end_idx = i

    return text1[end_idx - longest_len:end_idx]
