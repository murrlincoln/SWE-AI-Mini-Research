def max_product(nums: List[int]) -> int:
    """Finds the maximum product of any two distinct elements in the given list.

    Args:
        nums: A list of integers.

    Returns:
        The maximum product of any two distinct elements in the given list, or 0 if
        there are no two distinct elements.
    """

    if len(nums) < 2:
        return 0

    nums.sort()

    # Calculate the maximum product of the two smallest and two largest numbers.
    max_product_small = nums[0] * nums[1]
    max_product_large = nums[len(nums) - 2] * nums[len(nums) - 1]

    # Return the maximum product of the two smallest and two largest numbers.
    return max(max_product_small, max_product_large)
