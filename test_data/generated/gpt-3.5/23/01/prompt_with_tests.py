def longest_substring_with_k_distinct_characters(text: str, k: int) -> str:
    if k <= 0:
        return ''

    if len(text) < k:
        return ''

    # Initialize variables to keep track of the longest substring and its length
    longest_substring = ''
    max_length = 0

    # Initialize a dictionary to store character counts
    char_count = {}

    # Initialize pointers for the start and end of the current substring
    start = 0
    end = 0

    while end < len(text):
        # Add the current character to the char_count dictionary
        char = text[end]
        char_count[char] = char_count.get(char, 0) + 1

        # Check if the number of distinct characters exceeds k
        while len(char_count) > k:
            # Remove characters from the start of the substring
            start_char = text[start]
            char_count[start_char] -= 1
            if char_count[start_char] == 0:
                del char_count[start_char]
            start += 1

        # Update the longest substring if needed
        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substring = text[start:end + 1]

        end += 1

    return longest_substring
