def find_longest_substring_without_repeating_characters(text: str) -> str:
    n = len(text)
    char_set = set()
    result = ""
    left, right = 0, 0

    while right < n:
        if text[right] not in char_set:
            char_set.add(text[right])
            right += 1
            if right - left > len(result):
                result = text[left:right]
        else:
            char_set.remove(text[left])
            left += 1

    return result
