from typing import List

class Node:
    def __init__(self, value: int, next: 'Node' = None):
        self.value = value
        self.next = next

def reverse_linked_list(ll: List[int]) -> List[int]:
    def array_to_linked_list(arr: List[int]) -> Node:
        head = None
        for item in reversed(arr):
            head = Node(item, head)
        return head
    
    def linked_list_to_array(node: Node) -> List[int]:
        arr = []
        while node:
            arr.append(node.value)
            node = node.next
        return arr
    
    head = array_to_linked_list(ll)
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev, current = current, next_node
    return linked_list_to_array(prev)
