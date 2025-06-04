class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with working insert and incomplete build_from_list."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST (already implemented)."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive helper for insert (already implemented)."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def build_from_list(self, values):
        """📦 Build BST from a list of integer values."""
        # Your solution here 🛠
        for value in values:
            self.insert(value)

# Reuse inorder_traversal from Challenge 4 for test 5:
def inorder_traversal(node, result_list):
    if node is None:
        return
    inorder_traversal(node.left, result_list)
    result_list.append(node.value)
    inorder_traversal(node.right, result_list)

# 🧪 Test cases
def test_build_from_list():
    # Test 1: Empty list
    bst = BinarySearchTree()
    bst.build_from_list([])
    print("📭 Test 1:", bst.root is None)
    # Test 2: Single element
    bst = BinarySearchTree()
    bst.build_from_list([5])
    print("🌱 Test 2:", bst.root is not None and bst.root.value == 5)
    # Test 3: Multiple insert
    bst = BinarySearchTree()
    bst.build_from_list([10, 5, 15])
    cond3 = (bst.root.left.value == 5 and bst.root.right.value == 15)
    print("🔄 Test 3:", cond3)
    # Test 4: Duplicates
    bst = BinarySearchTree()
    bst.build_from_list([10, 10, 10])
    cond4 = (bst.root.value == 10 and bst.root.right.value == 10 and bst.root.right.right.value == 10)
    print("🔁 Test 4:", cond4)
    # Test 5: Unsorted order & inorder check
    bst = BinarySearchTree()
    bst.build_from_list([7, 3, 11, 1, 5])
    ordered = []
    inorder_traversal(bst.root, ordered)
    print("📈 Test 5:", ordered == [1, 3, 5, 7, 11])

# 🚀 Run tests
test_build_from_list()