class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with working insert and incomplete find_min."""
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

    def find_min(self):
        """🔎 Return the minimum value in the BST, or None if empty."""
        # Your solution here 🛠️
        node=self.root
        if node is None:
            return None
        while node.left is not None:
            node=node.left
        return node.value

# 🧪 Test cases
def test_find_min():
    # Test 1: Empty tree
    bst = BinarySearchTree()
    print("📭 Test 1:", bst.find_min() is None)
    # Test 2: Single node
    bst = BinarySearchTree()
    bst.insert(5)
    print("🌱 Test 2:", bst.find_min() == 5)
    # Test 3: Right-skewed [5,10,15]
    bst = BinarySearchTree()
    for v in [5, 10, 15]:
        bst.insert(v)
    print("👉 Test 3:", bst.find_min() == 5)
    # Test 4: Left-skewed [5,4,3]
    bst = BinarySearchTree()
    for v in [5, 4, 3]:
        bst.insert(v)
    print("👈 Test 4:", bst.find_min() == 3)
    # Test 5: Mixed [10,5,15,2,7]
    bst = BinarySearchTree()
    for v in [10, 5, 15, 2, 7]:
        bst.insert(v)
    print("🔍 Test 5:", bst.find_min() == 2)

# 🚀 Run tests
test_find_min()