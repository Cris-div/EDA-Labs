class TreeNode:
    """Basic node in a binary tree."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.left = None    # 👈 Left child reference
        self.right = None   # 👉 Right child reference

def create_sample_tree():
    """Create a sample binary tree for testing."""
    # Create tree structure:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def count_leaves(root):
    """Count the number of leaf nodes in a binary tree."""
    # Base case: empty tree has 0 leaves
    if not root:
        return 0

    # If node is a leaf (no children), count as 1
    if not root.left and not root.right:
        return 1

    # Recursively count leaves in left and right subtrees
    return count_leaves(root.left) + count_leaves(root.right)

def test_count_leaves():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert count_leaves(root) == 3  # 4, 5 y 6 son hojas

    # Test Case 2: Árbol vacío
    empty_tree = None
    assert count_leaves(empty_tree) == 0  # No hay hojas en un árbol vacío

    # Test Case 3: Árbol con un solo nodo
    single_node = TreeNode(1)
    assert count_leaves(single_node) == 1  # El único nodo es una hoja

    # Test Case 4: Árbol donde no hay hojas en el primer nivel
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    assert count_leaves(no_leaves_at_first) == 0  # No hay hojas en el primer nivel

    # Test Case 5: Todos los nodos son hojas excepto la raíz
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    assert count_leaves(all_leaves) == 6  # 2, 3, 4, 5, 6, 7 son hojas

    print("Todos los tests han pasado correctamente.")

# Ejecutar el test
test_count_leaves()
