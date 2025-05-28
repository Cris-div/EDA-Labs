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
    def is_valid_bst(self):
        """🧼 Check if the tree satisfies the BST property"""
        def validate(node, min_val, max_val):
            # Your solution here 🛠️
            if not node:
                return True
            if not (min_val < node.value< max_val):
                return False
            return(validate(node.left,min_val,node.value)and 
                   validate(node.right, node.value ,max_val))
        return validate(self.root, float('-inf'), float('inf'))

# 🧪 Test cases
def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 1:", bst1.is_valid_bst() == True)  # ✅ Valid tree

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # ❌ Incorrect: left > root
    bst2.root.right = Node(7)
    print("🧪 Test 2:", bst2.is_valid_bst() == False)  # ❌ Left violation

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # ❌ Incorrect: right < root
    print("🧪 Test 3:", bst3.is_valid_bst() == False)  # ❌ Right violation

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("🧪 Test 4:", bst4.is_valid_bst() == True)  # 🌱 Single node

    bst5 = BinarySearchTree()
    print("🧪 Test 5:", bst5.is_valid_bst() == True)  # 📭 Empty tree

# 🚀 Run tests
test_is_valid_bst()
