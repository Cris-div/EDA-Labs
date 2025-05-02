class TreeNode:
    """Basic node in a binary tree."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.left = None    # 👈 Left child reference
        self.right = None   # 👉 Right child reference

def level_order_traversal(root):
    """Perform level order traversal of a binary tree."""
    if not root:
        return []

    result = []
    queue = [root]  # Use a list as a queue

    while queue:
        # Get the next node
        current = queue.pop(0)
        result.append(current.value)

        # Add children to the queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

def test_level_order_traversal():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    # Expected level order traversal: [1, 2, 3, 4, 5, 6]
    result = level_order_traversal(root)
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], but got {result}"
    
    # Test Case 2: Empty tree
    empty_tree = None
    # Expected level order traversal: []
    result = level_order_traversal(empty_tree)
    assert result == [], f"Expected [], but got {result}"
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    # Expected level order traversal: [1]
    result = level_order_traversal(single_node)
    assert result == [1], f"Expected [1], but got {result}"
    
    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    # Expected level order traversal: [1, 2, 3, 4]
    result = level_order_traversal(left_skewed)
    assert result == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], but got {result}"
    
    # Test Case 5: Right-skewed tree
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
     # Expected level order traversal: [1, 2, 3, 4]
    result = level_order_traversal(right_skewed)
    assert result == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], but got {result}"

    print("Todos los tests han pasado correctamente.")
test_level_order_traversal()
