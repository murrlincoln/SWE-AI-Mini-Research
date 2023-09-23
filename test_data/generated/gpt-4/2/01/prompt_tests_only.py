from typing import List

def reverse_linked_list(ll: List[int]) -> List[int]:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def create_linked_list(arr):
        if not arr:
            return None
        head = Node(arr[0])
        current = head
        for value in arr[1:]:
            current.next = Node(value)
            current = current.next
        return head

    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    head = create_linked_list(ll)
    reversed_head = reverse_list(head)
    
    result = []
    current = reversed_head
    while current:
        result.append(current.value)
        current = current.next
    
    return result
