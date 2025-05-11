# Clase Nodo para representar un nodo en el árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None     # Hijo izquierdo
        self.right = None    # Hijo derecho

# Clase Árbol Binario
class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol binario

    # Construye un árbol binario a partir de una lista de valores en nivel
    def build_tree_from_list(self, values):
        if not values:
            return  # Si la lista está vacía, no hay árbol
        self.root = TreeNode(values[0])  # El primer valor es la raíz
        queue = [self.root]  # Usamos una cola para construir el árbol en niveles
        i = 1  # Índice para recorrer la lista de valores
        while queue and i < len(values):
            current = queue.pop(0)  # Extraemos el primer nodo de la cola
            if i < len(values) and values[i] is not None:  # Si hay un valor para el hijo izquierdo
                current.left = TreeNode(values[i])  # Creamos el hijo izquierdo
                queue.append(current.left)  # Lo añadimos a la cola
            i += 1
            if i < len(values) and values[i] is not None:  # Si hay un valor para el hijo derecho
                current.right = TreeNode(values[i])  # Creamos el hijo derecho
                queue.append(current.right)  # Lo añadimos a la cola
            i += 1

# Función para encontrar el ancestro común más bajo entre dos nodos
def lowest_common_ancestor(root, p, q):
    if not root:
        return None  # Si no hay nodo, no hay ancestro
    if root.value == p or root.value == q:
        return root  # Si el nodo es igual a uno de los valores, es el ancestro común
    # Buscamos el ancestro común en el subárbol izquierdo y derecho
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root  # Si encontramos p en el subárbol izquierdo y q en el derecho, la raíz es el ancestro común
    return left if left else right  # Si solo encontramos uno de los nodos en el subárbol, lo retornamos

# Función de prueba para el ancestro común más bajo
def test_lowest_common_ancestor():
    print("Testing Challenge 3: Lowest Common Ancestor 👨‍👩‍👧‍👦")
    cases = [
        ([1, 2, 3, 4, 5, None, 6], 4, 6, 1, "Different subtrees"),  # Caso con nodos en diferentes subárboles
        ([1, 2, 3, 4], 2, 4, 2, "Ancestor and descendant"),  # Caso donde uno es ancestro de otro
        ([1, 2, 3], 2, 3, 1, "Siblings"),  # Caso con nodos hermanos
        ([1, 2, 3], 1, 3, 1, "Root and child"),  # Caso con la raíz y un hijo
    ]
    for values, a, b, expected, label in cases:
        tree = BinaryTree()  # Crear el árbol
        tree.build_tree_from_list(values)  # Construir el árbol a partir de la lista de valores
        result = lowest_common_ancestor(tree.root, a, b)  # Encontrar el ancestro común más bajo
        # Verificar que el valor del resultado sea el esperado
        assert result and result.value == expected, f"{label} FAILED"
        print(f"{label} PASSED ✅")  # Si la prueba pasó, mostrar el mensaje

# Ejecutar las pruebas
test_lowest_common_ancestor()