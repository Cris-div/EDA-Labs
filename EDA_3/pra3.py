class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree with height and balance utilities."""
    def __init__(self):
        self.root = None

    def get_height(self, node):
        """
        📏 Return height of AVL node or 0 if node is None.
        """
        # Your solution here 🛠
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        """
        ⚖ Return balance factor: height(left) - height(right), or 0 if node is None.
        """
        # Your solution here 🛠
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
# 🧪 Test cases
def test_height_and_balance():
    tree = AVLTree()
    print("📭 Test 1:", tree.get_height(None) == 0)
    n = AVLNode(5)
    print("🌱 Test 2:", tree.get_height(n) == 1)
    n.left = AVLNode(3)
    n.left.height = 2
    print("👈 Test 3:", tree.get_height(n.left) == 2)
    print("📭 Test 4:", tree.get_balance(None) == 0)
    n.right = AVLNode(8)
    n.right.height = 1
    print("📏 Test 5:", tree.get_balance(n) == 1)

# 🚀 Run tests
test_height_and_balance()