def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    
    merged_list = []
    
    while list1 and list2:
        if list1[0] <= list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
            
    # One of the lists will now be empty.
    # Append the remaining values from the non-empty list.
    if list1:
        merged_list += list1
    if list2:
        merged_list += list2
        
    return merged_list