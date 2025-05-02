class TreeNode:
    """Basic node in a binary tree."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.left = None    # 👈 Left child reference
        self.right = None   # 👉 Right child reference


def mirror_tree(root):
    """Mirror a binary tree by swapping left and right children."""
    # Base case: empty tree or leaf node
    if not root:
        return

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively mirror the subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root



def test_mirror_tree():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    mirrored = mirror_tree(root)
    # Expected mirrored tree:
    #      1
    #     / \
    #    3   2
    #       / \
    #       5  4
    assert mirrored.value == 1
    assert mirrored.left.value == 3
    assert mirrored.right.value == 2
    assert mirrored.right.left.value == 5
    assert mirrored.right.right.value == 4

    # Test Case 2: Empty tree
    empty_tree = None
    assert mirror_tree(empty_tree) == None

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    mirrored_single_node = mirror_tree(single_node)
    assert mirrored_single_node.value == 1
    
    # Test Case 4: Tree with only left children
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    mirrored_left_only = mirror_tree(left_only)
    # Expected mirrored tree:
    #      1
    #       \
    #        2
    #         \
    #          3
    assert mirrored_left_only.value == 1
    assert mirrored_left_only.right.value == 2
    assert mirrored_left_only.right.right.value == 3
    
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    mirrored_perfect = mirror_tree(perfect)
    # Expected mirrored tree:
    #      1
    #     / \
    #    3   2
    #   / \ / \
    #  7  6 5  4
    assert mirrored_perfect.value == 1
    assert mirrored_perfect.left.value == 3
    assert mirrored_perfect.right.value == 2
    assert mirrored_perfect.left.left.value == 7
    assert mirrored_perfect.left.right.value == 6
    assert mirrored_perfect.right.left.value == 5
    assert mirrored_perfect.right.right.value == 4

    print("Todos los tests han pasado correctamente.")

test_mirror_tree()
