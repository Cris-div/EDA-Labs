class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value  # 🔢 Node value
        self.left = None    # 🌿 Left child
        self.right = None   # 🌿 Right child

class BinarySearchTree:
    """🌳 Binary Search Tree with basic functionality"""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST"""
        if self.root is None:
            self.root = Node(value)  # 🌱 First node
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive insert logic"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # 👈 Go left
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)  # 👉 Go right
            else:
                self._insert(node.right, value)

    def build_from_list(self, values):
        """📦 Build BST from a list of values"""
        for val in values:
            self.insert(val)


class BinarySearchTree(BinarySearchTree):
    def range_query(self, min_val, max_val):
        """🎯 Find all values in BST within given range"""
        # Your solution here 🛠️
        result=[]

        def inorder(node):
            if not node:
                return 
            if node.value > min_val:
                inorder(node.left)
            if min_val <= node.value <= max_val:
                result.append(node.value)
            if node.value < max_val:
                inorder(node.right)
        inorder(self.root)
        return result

# 🧪 Test cases
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("🧪 Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("🧪 Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # 🌐

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("🧪 Test 3:", bst3.range_query(1, 5) == [])  # 📭

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("🧪 Test 4:", bst4.range_query(10, 20) == [15])  # 🌱

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("🧪 Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # 🔗

# 🚀 Run all tests
test_range_query()
