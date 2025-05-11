# Clase que representa un nodo de árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value       # Valor del nodo
        self.left = None         # Hijo izquierdo
        self.right = None        # Hijo derecho

# Clase que implementa un Árbol Binario de Búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None         # Nodo raíz del árbol

    def insert(self, value):
        # Si el árbol está vacío, el nuevo nodo será la raíz
        if not self.root:
            self.root = TreeNode(value)
        else:
            # Llamamos al método recursivo para insertar el valor
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Si el valor es menor, va al subárbol izquierdo
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)   # Crear nuevo nodo hoja
            else:
                self._insert_recursive(node.left, value)  # Repetir recursivamente
        else:
            # Si el valor es mayor o igual, va al subárbol derecho
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self):
        # Devuelve los valores del árbol en orden (de menor a mayor)
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        # Recorrido inorder: izquierda - nodo - derecha
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Función para balancear un árbol binario de búsqueda
def balance_bst(bst):
    # Paso 1: Obtener los valores del BST en orden (esto genera una lista ordenada)
    sorted_values = bst.inorder_traversal()

    # Paso 2: Usar los valores ordenados para construir un BST balanceado
    def build_balanced_bst(values):
        if not values:
            return None
        mid = len(values) // 2  # Tomamos el valor del medio como raíz
        node = TreeNode(values[mid])
        node.left = build_balanced_bst(values[:mid])         # Construir lado izquierdo
        node.right = build_balanced_bst(values[mid + 1:])    # Construir lado derecho
        return node

    # Creamos un nuevo árbol BST con la raíz balanceada
    balanced = BinarySearchTree()
    balanced.root = build_balanced_bst(sorted_values)
    return balanced

# Función de prueba para balancear BSTs con varios casos
def test_balance_bst():
    print("Testing Challenge 1: Tree Balancing ⚖️")

    # Caso 1: Árbol ya balanceado
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)

    # Caso 2: Árbol desbalanceado a la derecha
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)

    # Caso 3: Árbol desbalanceado a la izquierda
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)

    # Caso 4: Árbol vacío
    bst4 = BinarySearchTree()

    # Caso 5: Árbol con un solo nodo
    bst5 = BinarySearchTree()
    bst5.insert(42)

    # Función interna para verificar si el BST balanceado mantiene el orden original
    def assert_balanced(original, label):
        balanced = balance_bst(original)
        original_sorted = original.inorder_traversal()
        balanced_sorted = balanced.inorder_traversal()
        # Verificamos que el árbol balanceado tenga el mismo recorrido inorder
        assert original_sorted == balanced_sorted, f"{label} FAILED: Output differs!"
        print(f"{label} PASSED ✅")

    # Ejecutar los 5 casos de prueba
    assert_balanced(bst1, "Balanced Tree")
    assert_balanced(bst2, "Right-skewed Tree")
    assert_balanced(bst3, "Left-skewed Tree")
    assert_balanced(bst4, "Empty Tree")
    assert_balanced(bst5, "Single Node Tree")

if __name__ == "__main__":
    test_balance_bst()