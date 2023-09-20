def is_binary_tree_balanced(tree):
    if tree is None:
        return True
 
    left_height = tree.left.height() if tree.left else 0
    right_height = tree.right.height() if tree.right else 0
 
    if (abs(left_height - right_height) <= 1) and \
        is_binary_tree_balanced(tree.left) and \
        is_binary_tree_balanced(tree.right):
        return True
 
    return False