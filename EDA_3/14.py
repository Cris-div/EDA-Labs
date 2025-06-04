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
        # Your solution here 🛠️
        for value in values:
            self.insert(value)

def inorder_traversal(node, result_list):
    """
    📝 Inorder traversal: left → root → right.
    Appends node values to result_list in sorted order.
    """
    # Your solution here 🛠️
    if result_list is None:
        result_list=[]
    if node is None:
        return 
    inorder_traversal(node.left,result_list)
    result_list.append(node.value)
    inorder_traversal(node.right,result_list)

# 🧪 Test cases
def test_inorder_traversal():
    # Test 1: Empty tree
    result = []
    inorder_traversal(None, result)
    print("📭 Test 1:", result == [])
    # Test 2: Single node
    single = Node(5)
    result = []
    inorder_traversal(single, result)
    print("🌱 Test 2:", result == [5])
    # Test 3: Simple tree [10,5,15]
    bst = BinarySearchTree()
    bst.build_from_list([10, 5, 15])
    result = []
    inorder_traversal(bst.root, result)
    print("✅ Test 3:", result == [5, 10, 15])
    # Test 4: Left-skewed [5,4,3]
    bst = BinarySearchTree()
    bst.build_from_list([5, 4, 3])
    result = []
    inorder_traversal(bst.root, result)
    print("👈 Test 4:", result == [3, 4, 5])
    # Test 5: Complex [7,3,11,1,5,9,13]
    bst = BinarySearchTree()
    bst.build_from_list([7, 3, 11, 1, 5, 9, 13])
    result = []
    inorder_traversal(bst.root, result)
    print("📈 Test 5:", result == [1, 3, 5, 7, 9, 11, 13])

# 🚀 Run tests
test_inorder_traversal()