def longest_common_substring(text1: str, text2: str) -> str:
    # Initialize a matrix to store the lengths of common substrings
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    # Variables to keep track of the maximum substring length and its ending position
    max_length = 0
    end_position = 0

    # Fill in the matrix and track the maximum length
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i

    # Extract the longest common substring
    longest_substring = text1[end_position - max_length:end_position]

    return longest_substring
