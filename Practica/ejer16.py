class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def height(self, node=None):
        if node is None:
            if self.root is None:
                return -1
            return self.height(self.root)
        if node.left is None and node.right is None:
            return 0
        left_heigt=-1
        if node.left is not None:
            left_heigt=self.height(node.left)
        right_heigt=-1
        if node.right is not None:
            right_heigt=self.height(node.right)
        return max(left_heigt,right_heigt)+1

# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.height() == -1) # 📭 Árbol vacío
single_node_tree = BinaryTree(TreeNode(1))
print(single_node_tree.height() == 0) # 🌱 Árbol de un solo nodo

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
tree = BinaryTree(root)
print(tree.height() == 2) # 📏 Altura 2

deep_root = TreeNode(1)
deep_root.left = TreeNode(2)
deep_root.left.left = TreeNode(3)
deep_root.left.left.left = TreeNode(4)
deep_tree = BinaryTree(deep_root)
print(deep_tree.height() == 3) # 📐 Altura 3

print(isinstance(deep_tree.height(), int)) # 🔢 Tipo numérico