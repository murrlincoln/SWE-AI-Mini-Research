def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if not text or k == 0:
        return ""

    # Use a sliding window approach with two pointers: left and right
    left, right = 0, 0

    # Use a dictionary to keep track of the frequency of characters in the current window
    char_frequency = {}

    # Use a variable to keep track of the maximum length and the start index of the longest substring
    max_length, max_length_start = 0, 0

    while right < len(text):
        # Add the current character to the dictionary
        if text[right] not in char_frequency:
            char_frequency[text[right]] = 0
        char_frequency[text[right]] += 1

        # If the number of distinct characters in the current window exceeds k, shrink the window from the left
        while len(char_frequency) > k:
            char_frequency[text[left]] -= 1
            if char_frequency[text[left]] == 0:
                del char_frequency[text[left]]
            left += 1

        # Update the maximum length and start index if needed
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_length_start = left

        right += 1

    return text[max_length_start:max_length_start + max_length]
