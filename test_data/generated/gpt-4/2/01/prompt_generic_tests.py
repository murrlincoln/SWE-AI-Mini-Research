from typing import List

def function(a: List[int], b: List[int]) -> List[int]:
    merged_list = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
    while i < len(a):
        merged_list.append(a[i])
        i += 1
    while j < len(b):
        merged_list.append(b[j])
        j += 1
    return merged_list
