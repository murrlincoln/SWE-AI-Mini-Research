from typing import Dict, List

def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in reversed(graph[node]):  # Reversing to get the correct order due to stack's LIFO nature
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_order
