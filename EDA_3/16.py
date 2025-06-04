class AVLNode:
    def __init__(self, key):
        """🌱 Initialize an AVL node with key and default height=1."""
        # Your solution here 🛠️
        self.key=key
        self.left=None
        self.right=None
        self.height=1

# 🧪 Test cases
def test_avl_node():
    n = AVLNode(10)
    print("🔑 Test 1:", n.key == 10)
    print("📐 Test 2:", n.left is None)
    print("📐 Test 3:", n.right is None)
    print("📏 Test 4:", n.height == 1)
    n2 = AVLNode(-5)
    print("🔑 Test 5:", n2.key == -5 and n2.height == 1)

# 🚀 Run tests
test_avl_node()