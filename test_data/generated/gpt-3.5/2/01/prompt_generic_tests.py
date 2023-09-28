from typing import List

def function(a: List[int], b: List[int]) -> List[int]:
    merged_list = sorted(a + b)
    return merged_list
