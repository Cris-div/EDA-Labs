test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value) -> 'TreeNode':
        """Insert a new node to the left; shift existing child if present."""
        node=TreeNode(value)
        if self.left is None:
            self.left=node
        else:
            old=self.left
            self.left=node
            node.left=old
        return node
        

    def insert_right(self, value) -> 'TreeNode':
        """Insert a new node to the right; shift existing child if present."""
        node=TreeNode(value)
        if self.right is None:
            self.right=node
        else:
            old=self.right
            self.right=node
            node.right=old
        return node
def test_o7_1():
    # o7.1.1 Left Creation
    root = TreeNode(1)
    left = root.insert_left(2)
    record_test("o7.1.1 left creation", root.left.value == 2)

    # o7.1.2 Right Creation
    root = TreeNode(1)
    right = root.insert_right(3)
    record_test("o7.1.2 right creation", root.right.value == 3)

    # o7.1.3 Independent Insertion
    root = TreeNode(1)
    root.insert_left(4)
    root.insert_right(5)
    record_test(
        "o7.1.3 independent insertion", root.left.value == 4 and root.right.value == 5
    )

    # o7.1.4 Validation: Left-Shift
    root = TreeNode(1)
    root.left = TreeNode(6)
    new_left = root.insert_left(7)
    record_test("o7.1.4 left shift", new_left.left.value == 6)

    # o7.1.5 Return-Type Verification
    record_test(
        "o7.1.5 return type", isinstance(left, TreeNode) and isinstance(right, TreeNode)
    )

# 🚀 Run tests
test_o7_1()

# 📋 Summary
for r in test_results:
    print(r)