test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node=None, result=None):
        # Your solution here 🌲
        pass

    def inorder_traversal(self, node=None, result=None):
        # Your solution here 🔍
        pass

    def postorder_traversal(self, node=None, result=None):
        # Your solution here 🌴
        pass

def test_o7_2():
    # o7.2.1 Balanced Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    tree = BinaryTree(root)
    record_test(
        "o7.2.1 balanced traversals",
        tree.inorder_traversal() == [4, 2, 5, 1, 3, 6]
        and tree.preorder_traversal() == [1, 2, 4, 5, 3, 6]
        and tree.postorder_traversal() == [4, 5, 2, 6, 3, 1],
    )

    # o7.2.2 Single Node
    single = BinaryTree(TreeNode(42))
    record_test(
        "o7.2.2 single",
        single.preorder_traversal() == [42]
        and single.inorder_traversal() == [42]
        and single.postorder_traversal() == [42],
    )

    # o7.2.3 Empty Tree
    empty = BinaryTree()
    record_test(
        "o7.2.3 empty",
        empty.preorder_traversal() == []
        and empty.inorder_traversal() == []
        and empty.postorder_traversal() == [],
    )

    # o7.2.4 Right-Heavy Tree
    rh = BinaryTree(TreeNode(1))
    rh.root.right = TreeNode(2)
    rh.root.right.right = TreeNode(3)
    record_test(
        "o7.2.4 right-heavy",
        rh.preorder_traversal() == [1, 2, 3]
        and rh.inorder_traversal() == [1, 2, 3]
        and rh.postorder_traversal() == [3, 2, 1],
    )

    # o7.2.5 Return-Type Verification
    tree2 = BinaryTree()
    record_test(
        "o7.2.5 types",
        isinstance(tree2.preorder_traversal(), list)
        and isinstance(tree2.inorder_traversal(), list)
        and isinstance(tree2.postorder_traversal(), list),
    )

# 🚀 Run tests
test_o7_2()

# 📋 Summary
for r in test_results:
    print(r)