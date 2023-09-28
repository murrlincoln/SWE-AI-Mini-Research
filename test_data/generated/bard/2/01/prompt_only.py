def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
  """Merges two sorted lists into a single sorted list.

  Args:
    list1: A sorted list of integers.
    list2: A sorted list of integers.

  Returns:
    A sorted list of integers, which is the merger of list1 and list2.
  """

  merged_list = []
  i = 0
  j = 0
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged_list.append(list1[i])
      i += 1
    else:
      merged_list.append(list2[j])
      j += 1

  # Add the remaining elements of list1 (if any) to the merged list.
  while i < len(list1):
    merged_list.append(list1[i])
    i += 1

  # Add the remaining elements of list2 (if any) to the merged list.
  while j < len(list2):
    merged_list.append(list2[j])
    j += 1

  return merged_list
