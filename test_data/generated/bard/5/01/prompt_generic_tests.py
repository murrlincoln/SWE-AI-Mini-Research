class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1

def function(a: TreeNode) -> bool:
    return is_balanced(a)
