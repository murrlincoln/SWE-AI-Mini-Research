from typing import Dict, List

def function(a: Dict[int, List[int]], b: int) -> List[int]:
    visited = set()
    stack = [b]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            result.append(node)
            visited.add(node)
            stack.extend(reversed(a[node]))

    return result
