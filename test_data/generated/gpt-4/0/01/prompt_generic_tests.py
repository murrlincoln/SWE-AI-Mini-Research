from typing import List

def function(a: List[int]) -> List[int]:
    evens, odds = [], []
    for num in a:
        (evens if num % 2 == 0 else odds).append(num)
    result = []
    e_i, o_i = 0, 0
    for num in a:
        if num % 2 == 0:
            result.append(evens[e_i])
            e_i += 1
        else:
            result.append(odds[o_i])
            o_i += 1
    return result
