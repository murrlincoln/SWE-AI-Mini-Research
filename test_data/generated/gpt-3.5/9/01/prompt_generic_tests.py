from typing import Dict, List

def function(a: Dict[int, List[int]], b: int) -> List[int]:
    visited = set()
    result = []
    
    def dfs(node):
        visited.add(node)
        result.append(node)
        for neighbor in a.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(b)
    return result
