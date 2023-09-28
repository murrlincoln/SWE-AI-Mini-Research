from typing import List

def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from list1 and list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list
