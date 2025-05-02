class TreeNode:
    """Basic node in a binary tree."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.left = None    # 👈 Left child reference
        self.right = None   # 👉 Right child reference


def tree_height(root):
    """Calculate the height of a binary tree."""
    # Base case: empty tree has height -1
    if not root:
        return -1

    # Recursively find the height of left and right subtrees
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    # Height is the maximum of left and right subtree heights, plus 1
    return max(left_height, right_height) + 1
    
def test_tree_height():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert tree_height(root) == 2  

    # Test Case 2: Empty tree
    empty_tree = None
    assert tree_height(empty_tree) == -1  

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    assert tree_height(single_node) == 0  

    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    assert tree_height(left_skewed) == 3  

    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    assert tree_height(perfect) == 2  

    print("Todos los tests han pasado correctamente.")

test_tree_height()
