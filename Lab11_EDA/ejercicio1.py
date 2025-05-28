class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value      # 🔢 Store the node's value
        self.left = None        # 🌿 Reference to the left child (initially None)
        self.right = None       # 🌿 Reference to the right child (initially None)

class BinarySearchTree:
    """🌳 Binary Search Tree with basic functionality"""
    def __init__(self):
        self.root = None        # 📭 The root of the tree starts as None (empty tree)

    def insert(self, value):
        """🧩 Insert a value into the BST"""
        if self.root is None:
            self.root = Node(value)  # 🌱 If the tree is empty, insert at the root
        else:
            self._insert(self.root, value)  # ➕ Otherwise, insert recursively

    def _insert(self, node, value):
        """🔄 Recursive insert logic"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # 👈 Insert to the left if no left child
            else:
                self._insert(node.left, value)  # ↪ Recurse left
        else:
            if node.right is None:
                node.right = Node(value)  # 👉 Insert to the right if no right child
            else:
                self._insert(node.right, value)  # ↪ Recurse right

    def build_from_list(self, values):
        """📦 Build BST from a list of values"""
        for val in values:
            self.insert(val)  # ➕ Insert each value one by one

# Extending the BinarySearchTree class
class BinarySearchTree(BinarySearchTree):
    def range_query(self, min_val, max_val):
        """🎯 Find all values in BST within given range"""
        result = []  # 🧺 List to store values in the range

        def inorder(node):
            if not node:
                return  # 🚪 Base case: if node is None, do nothing
            if node.value > min_val:
                inorder(node.left)  # 🔍 Explore left subtree if values might be in range
            if min_val <= node.value <= max_val:
                result.append(node.value)  # ✅ Add value if within range
            if node.value < max_val:
                inorder(node.right)  # 🔍 Explore right subtree if values might be in range

        inorder(self.root)  # 🌿 Start from the root
        return result  # 🎁 Return the collected results

# 🧪 Test cases
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("🧪 Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅ Should include 5, 7, 9

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("🧪 Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # 🌐 All values are within range

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("🧪 Test 3:", bst3.range_query(1, 5) == [])  # 📭 No values in range

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("🧪 Test 4:", bst4.range_query(10, 20) == [15])  # 🌱 Only value is within range

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("🧪 Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # 🔗 Range includes 10, 15, 20

# 🚀 Run all tests
test_range_query()
