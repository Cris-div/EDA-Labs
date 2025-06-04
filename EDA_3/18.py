class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree with rotation methods."""
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """
        🔄 Perform left rotation on node z and return new root.
        """
        # Your solution here 🛠️
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        """
        🔃 Perform right rotation on node z and return new root.
        """
        # Your solution here 🛠️
        y = z.left
        T3 = y.right

        # Rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

# 🧪 Test cases
def test_rotations():
    tree = AVLTree()
    # Test 1: Left Rotate Simple
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.height = 1
    z.height = 2
    new_root = tree.left_rotate(z)
    cond1 = (new_root.key == 20 and new_root.left.key == 10 and new_root.left.right is None)
    print("🔄 Test 1:", cond1)

    # Test 2: Right Rotate Simple
    z = AVLNode(20)
    z.left = AVLNode(10)
    z.left.height = 1
    z.height = 2
    new_root = tree.right_rotate(z)
    cond2 = (new_root.key == 10 and new_root.right.key == 20 and new_root.right.left is None)
    print("🔃 Test 2:", cond2)

    # Test 3: Update Heights Left
    z = AVLNode(30)
    z.right = AVLNode(40); z.right.height = 1
    z.height = 2
    new_root = tree.left_rotate(z)
    cond3 = (new_root.height == 2 and new_root.left.height == 1)
    print("📏 Test 3:", cond3)

    # Test 4: Update Heights Right
    z = AVLNode(30)
    z.left = AVLNode(20); z.left.height = 1
    z.height = 2
    new_root = tree.right_rotate(z)
    cond4 = (new_root.height == 2 and new_root.right.height == 1)
    print("📐 Test 4:", cond4)

    # Test 5: Chain Left Rotate
    root = AVLNode(20)
    root.right = AVLNode(30); root.right.height = 2
    root.right.right = AVLNode(40); root.right.right.height = 1
    root.height = 3
    new_root = tree.left_rotate(root)
    cond5 = (new_root.key == 30 and new_root.left.key == 20 and new_root.right.key == 40)
    print("🔁 Test 5:", cond5)

# 🚀 Run tests
test_rotations()