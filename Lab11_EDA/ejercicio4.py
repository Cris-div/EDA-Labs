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
    def kth_smallest(self, k):
        """📊 Find the kth smallest value in the BST"""
        # Your solution here 🛠️
        result=[]            # 📥 Store visited nodes in sorted order (inorder traversal)

        def inorder(node):
            if not node or len(result)>=k:   # ⛔ Stop if node is None or already got k elements
                return
            inorder(node.left)  # 👈 Traverse left subtree (smaller values)
            if len(result)<k:
                result.append(node.value)  # ➕ Visit current node if we still need more elements
            inorder(node.right) # 👉 Traverse right subtree (larger values)
        inorder(self.root)  # 🚀 Start traversal from root
        return result[k-1] if k<=len(result) else None  # ✅ Return kth smallest or None if out of bounds


# 🧪 Test cases
def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print("🧪 Test 1:", bst1.kth_smallest(2) == 2)  # 🎯

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 2:", bst2.kth_smallest(1) == 2)  # 📉 First (min)

    print("🧪 Test 3:", bst2.kth_smallest(7) == 8)  # 📈 Last (max)

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 Middle

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print("🧪 Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Single node

# 🚀 Run tests
test_kth_smallest()
