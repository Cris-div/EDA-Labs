class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        def _insert(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    _insert(node.left, value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    _insert(node.right, value)

        _insert(self.root, value)

    def search(self, value):
        node=self.root
        while node:
            if value==node.value:
                return True
            elif value<node.value:
                node=node.left
            else:
                node=node.right
        return False
             
# ✅ Test cases
bst = BinarySearchTree()
print(bst.search(10) == False) # 📭 Árbol vacío

bst.insert(10)
print(bst.search(10) == True) # ✅ Valor encontrado
print(bst.search(20) == False) # ❌ Valor no encontrado

bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
print(bst.search(7) == True) # 🎯 Valor en subárbol

print(isinstance(bst.search(5), bool)) # 🔍 Tipo booleano