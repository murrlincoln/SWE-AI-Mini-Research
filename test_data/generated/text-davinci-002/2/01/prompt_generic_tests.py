def function(a: List[int], b: List[int]) -> List[int]:
    """
    >>> function([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> function([7, 9], [8, 10])
    [7, 8, 9, 10]
    """
    return sorted(a + b)