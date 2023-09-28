from typing import Dict, List

def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result
