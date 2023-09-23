from typing import List
from itertools import combinations

def max_product(nums: List[int]) -> int:
    max_product = float('-inf')
    for combo in combinations(nums, 2):
        product = combo[0] * combo[1]
        max_product = max(max_product, product)
    return max_product
