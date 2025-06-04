class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with working insert and incomplete search."""
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

    def search(self, value):
        """🔍 Return True if value exists in BST, else False."""
        # Your solution here 🛠️
        return self._search(self.root,value)

    def _search(self, node, value):
        """🔁 Recursive search helper."""
        # Your solution here 🛠️
        if node is None:
            return False
        if node.value==value:
            return True
        if value < node.value:
            return self._search(node.left,value)
        return self._search(node.right,value)

# 🧪 Test cases
def test_search():
    # Test 1: Empty tree
    bst = BinarySearchTree()
    print("📭 Test 1:", bst.search(5) == False)
    # Test 2: Root exists
    bst = BinarySearchTree()
    bst.insert(10)
    print("🎯 Test 2:", bst.search(10) == True)
    # Test 3: Left subtree
    bst = BinarySearchTree()
    for v in [10, 5, 3]:
        bst.insert(v)
    print("👈 Test 3:", bst.search(3) == True)
    # Test 4: Right subtree
    bst = BinarySearchTree()
    for v in [10, 5, 15, 20]:
        bst.insert(v)
    print("👉 Test 4:", bst.search(20) == True)
    # Test 5: Not found
    bst = BinarySearchTree()
    for v in [10, 5, 15]:
        bst.insert(v)
    print("❌ Test 5:", bst.search(7) == False)

# 🚀 Run tests
test_search()