from typing import List

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(ll: List[int]) -> List[int]:
    def array_to_linked_list(arr):
        dummy = ListNode()
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    def linked_list_to_array(node):
        arr = []
        while node:
            arr.append(node.value)
            node = node.next
        return arr
    
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    head = array_to_linked_list(ll)
    reversed_head = reverse_list(head)
    return linked_list_to_array(reversed_head)
