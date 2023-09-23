from typing import Dict, List

def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    traversal_order = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return traversal_order
