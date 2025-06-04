class GenericTreeNode:
    """🌳 Node for a generic tree (multiple children)."""
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, value):
        """➕ Add a child node with the given value, return the new node."""
        # Your solution here 🛠️
        new_node=GenericTreeNode(value)
        self.children.append(new_node)
        return new_node

class GenericTree:
    """🌿 Generic tree with basic operations."""
    def __init__(self):
        self.root = None  # 🌱 Root of the generic tree

    def preorder_traversal(self, node=None, result=None):
        """
        📝 Visit node first, then all children (DLR) in left-to-right order.
        Returns a list of values in preorder.
        """
        # Your solution here 🛠️
        if result is None:
            result=[]
        if node is None:
            node=self.root
        if node is None:
            return result
        result.append(node.value)
        for child in node.children:
            self.preorder_traversal(child, result)
        return result

# 🧪 Test cases
def test_generic_preorder():
    # Test 1: Empty tree
    tree = GenericTree()
    print("🚶 Test 1:", tree.preorder_traversal() == [])

    # Build tree:
    #      A
    #    / | \
    #   B  C  D
    #      |
    #      E
    tree.root = GenericTreeNode("A")
    b = tree.root.add_child("B")
    c = tree.root.add_child("C")
    d = tree.root.add_child("D")
    c.add_child("E")

    # Test 2: Two-level
    print("🚶 Test 2:", tree.preorder_traversal() == ["A", "B", "C", "E", "D"])

    # Test 3: Single-node after resetting
    single = GenericTree()
    single.root = GenericTreeNode(42)
    print("🚶 Test 3:", single.preorder_traversal() == [42])

    # Test 4: More complex (add extra children)
    c.add_child("F")
    b.add_child("G")
    print("🚶 Test 4:", tree.preorder_traversal() == ["A", "B", "G", "C", "E", "F", "D"])

    # Test 5: Verify no duplication
    values = tree.preorder_traversal()
    print("🚶 Test 5:", len(values) == len(set(values)))

# 🚀 Run tests
test_generic_preorder()