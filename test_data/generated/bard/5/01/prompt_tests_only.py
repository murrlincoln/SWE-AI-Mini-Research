class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def is_balanced(tree: TreeNode) -> bool:
  """
  Checks if a binary tree is balanced.

  Args:
    tree: The root node of the binary tree.

  Returns:
    True if the tree is balanced, False otherwise.
  """

  if tree is None:
    return True

  left_height = height(tree.left)
  right_height = height(tree.right)

  return abs(left_height - right_height) <= 1 and is_balanced(tree.left) and is_balanced(tree.right)

def height(tree: TreeNode) -> int:
  """
  Calculates the height of a binary tree.

  Args:
    tree: The root node of the binary tree.

  Returns:
    The height of the binary tree.
  """

  if tree is None:
    return 0

  return max(height(tree.left), height(tree.right)) + 1
