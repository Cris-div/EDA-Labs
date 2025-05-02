class TreeNode:
    """Basic node in a binary tree."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.left = None    # 👈 Left child reference
        self.right = None   # 👉 Right child reference

def is_balanced(root):
    """Check if a binary tree is balanced (height difference between subtrees ≤ 1)."""

    def check_height(node):
        """Helper function that returns (is_balanced, height)."""
        # Base case: empty subtree is balanced with height -1
        if not node:
            return True, -1

        # Check left subtree
        left_balanced, left_height = check_height(node.left)
        if not left_balanced:
            return False, 0

        # Check right subtree
        right_balanced, right_height = check_height(node.right)
        if not right_balanced:
            return False, 0

        # Check balance at current node
        is_balanced_here = abs(left_height - right_height) <= 1
        height_here = max(left_height, right_height) + 1

        return is_balanced_here, height_here

    # Call the helper function and return the balanced status
    balanced, _ = check_height(root)
    return balanced

def test_is_balanced():
    # Test Case 1: Balanced tree
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)

    result = is_balanced(balanced)
    assert result == True, f"Expected True, but got {result}"
    # Test Case 2: Empty tree (trivially balanced)
    empty_tree = None

    result = is_balanced(empty_tree)
    assert result == True, f"Expected True, but got {result}"
    
    # Test Case 3: Single node tree (trivially balanced)
    single_node = TreeNode(1)
    
    result = is_balanced(single_node)
    assert result == True, f"Expected True, but got {result}"
    # Test Case 4: Unbalanced tree - left-heavy
    unbalanced_left = TreeNode(1)
    unbalanced_left.left = TreeNode(2)
    unbalanced_left.left.left = TreeNode(3)
    unbalanced_left.left.left.left = TreeNode(4)

    result = is_balanced(unbalanced_left)
    assert result == False, f"Expected False, but got {result}"
    
    # Test Case 5: Just balanced on the edge case
    edge_balanced = TreeNode(1)
    edge_balanced.left = TreeNode(2)
    edge_balanced.right = TreeNode(3)
    edge_balanced.left.left = TreeNode(4)
    edge_balanced.left.right = TreeNode(5)
    edge_balanced.left.left.left = TreeNode(6)

    result = is_balanced(edge_balanced)
    assert result == False, f"Expected False, but got {result}"

    print("Todos los tests han pasado correctamente.")

test_is_balanced()
