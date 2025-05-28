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
    def bst_to_dll(self):
        """🔁 Convert BST to sorted circular doubly linked list"""
        # Your solution here 🛠️
        if not self.root:
            return None   # 📭 If the tree is empty, return None
        prev=None  # ⬅️ Will track the previously visited node
        head=None  # 🔝 Will be the head of the resulting DLL
        def inorder(node):
            nonlocal prev,head
            if not node:
                return   # 🔚 Base case for recursion
            inorder(node.left)   # 👈 Traverse left subtree
            if prev:  # 🔗 Connect current node with the previous one
                prev.right=node
                node.left=prev
            else:   
                head=node  # 🏁 First node becomes the head
            prev=node   # 🔄 Update prev to current
            inorder(node.right)   # 👉 Traverse right subtree
        inorder(self.root)
        # 🔁 Make the DLL circular
        head.left=prev
        prev.right=head
        return head  # ✅ Return the head of the circular DLL

# ✅ DLL validator helper
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    return values == expected_values

# 🧪 Test cases
def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 🌳

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)  # 🌱

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)  # 📭 Empty tree

# 🚀 Run tests
test_bst_to_dll()
           