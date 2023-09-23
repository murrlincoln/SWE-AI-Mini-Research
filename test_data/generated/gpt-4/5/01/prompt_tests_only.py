class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node: TreeNode) -> int:
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

def is_balanced(tree: TreeNode) -> bool:
    return height(tree) != -1
