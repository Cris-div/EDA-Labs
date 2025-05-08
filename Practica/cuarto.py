#level_order_traversal() en Árbol Binario 📊
#Implementa el método level_order_traversal() que realice un recorrido por niveles (BFS) de un árbol binario.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def level_order_traversal(self):
        if not self.root :
            return []
        result=[]
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
        
        
# ✅ Test cases
empty_tree = BinaryTree()
print(empty_tree.level_order_traversal() == []) # 📭 Árbol vacío

single_node_tree = BinaryTree(TreeNode(42))
print(single_node_tree.level_order_traversal() == [42]) # 🌱 Árbol de un solo nodo

# Árbol:      1
#           /   \
#          2     3
#         / \     \
#        4   5     6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

tree = BinaryTree(root)
print(tree.level_order_traversal() == [1, 2, 3, 4, 5, 6]) # 📊 Recorrido por niveles

tree.root = TreeNode(10)
tree.root.left = TreeNode(20)
tree.root.right = TreeNode(30)
print(tree.level_order_traversal() == [10, 20, 30]) # 🎯 Otro árbol

print(isinstance(tree.level_order_traversal(), list)) # 📋 Tipo lista