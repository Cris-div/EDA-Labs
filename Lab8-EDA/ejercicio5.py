# Clase Nodo para representar un nodo en el árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value      # Valor del nodo
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho

# Clase Árbol Binario
class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol binario

    # Construye el árbol a partir de una lista nivel por nivel (None significa ausencia de nodo)
    def build_tree_from_list(self, values):
        if not values:
            return
        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1
        while queue and i < len(values):
            current = queue.pop(0)
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

# Función que poda el árbol eliminando subárboles que no contienen el valor objetivo
def prune_tree(node, target):
    if not node:
        return None  # Si el nodo es nulo, devolvemos None

    # Procesar primero los hijos (postorden)
    node.left = prune_tree(node.left, target)
    node.right = prune_tree(node.right, target)

    # Si el nodo actual no es el valor objetivo y no tiene hijos útiles, lo eliminamos
    if node.value != target and not node.left and not node.right:
        return None

    return node  # Si contiene el valor o tiene hijos útiles, se mantiene

# Función para imprimir el árbol en recorrido por niveles (level-order)
def print_tree_level_order(root):
    if not root:
        print("Empty tree 🈳")
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Eliminar los None finales para una impresión más limpia
    while result and result[-1] is None:
        result.pop()
    print(result)

# Función de prueba con varios casos
def test_prune_tree():
    print("Testing Challenge 5: Tree Pruning ✂️🌳")

    # Test Case 1: Solo queda el nodo raíz
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    pruned1 = prune_tree(tree1.root, 1)
    print("Test Case 1:")
    print_tree_level_order(pruned1)

    # Test Case 2: Mantener todas las ramas que tengan un 1
    tree2 = BinaryTree()
    tree2.root = TreeNode(1)
    tree2.root.left = TreeNode(2)
    tree2.root.right = TreeNode(3)
    tree2.root.left.left = TreeNode(1)
    tree2.root.left.right = TreeNode(5)
    tree2.root.right.right = TreeNode(1)
    pruned2 = prune_tree(tree2.root, 1)
    print("Test Case 2:")
    print_tree_level_order(pruned2)

    # Test Case 3: Árbol vacío
    tree3 = BinaryTree()
    pruned3 = prune_tree(tree3.root, 1)
    print("Test Case 3:")
    print_tree_level_order(pruned3)

    # Test Case 4: Ningún nodo tiene el valor objetivo
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    pruned4 = prune_tree(tree4.root, 4)
    print("Test Case 4:")
    print_tree_level_order(pruned4)

    # Test Case 5: Todos los nodos tienen el valor objetivo
    tree5 = BinaryTree()
    tree5.root = TreeNode(5)
    tree5.root.left = TreeNode(5)
    tree5.root.right = TreeNode(5)
    pruned5 = prune_tree(tree5.root, 5)
    print("Test Case 5:")
    print_tree_level_order(pruned5)

# Ejecutar todas las pruebas
test_prune_tree()
