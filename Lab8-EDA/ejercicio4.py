# Clase Nodo para representar un nodo en el árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Hijo izquierdo
        self.right = None   # Hijo derecho

# Clase Árbol Binario
class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol binario

    # Construye un árbol binario a partir de una lista de valores en nivel
    def build_tree_from_list(self, values):
        if not values:
            return   # Si la lista está vacía, no hay árbol que construir
        self.root = TreeNode(values[0])  # El primer valor será la raíz del árbol
        queue = [self.root]  # Usamos una cola para recorrer y construir el árbol nivel por nivel
        i = 1 # Índice para ir recorriendo la lista de valores
        while queue and i < len(values):  # Mientras haya nodos en la cola y valores por procesar
            current = queue.pop(0)  # Sacamos el primer nodo de la cola (FIFO)
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i]) # Creamos el hijo izquierdo si no es None
                queue.append(current.left)  # Lo agregamos a la cola para procesar sus hijos
            i += 1 # Avanzamos al siguiente valor
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])  # Creamos el hijo derecho si no es None
                queue.append(current.right) # Lo agregamos a la cola
            i += 1 # Avanzamos al siguiente valor

# Función para recorrido vertical sin usar collections
def vertical_order_traversal(root):
    if not root:
        return []   # Si no hay árbol, devolvemos una lista vacía

    col_map = {}  # Diccionario para agrupar nodos por su columna horizontal (x)
    queue = [(root, 0)]   # Cola para BFS (nodo, columna), raíz está en columna 0

    while queue:
        node, col = queue.pop(0)  # Tomamos el primer elemento de la cola
        if node:
            if col not in col_map:
                col_map[col] = []  # Si aún no hay lista para esa columna, la creamos
            col_map[col].append(node.value) # Añadimos el valor del nodo a su columna correspondiente

            queue.append((node.left, col - 1))# Hijo izquierdo está una columna a la izquierda (col - 1)
            queue.append((node.right, col + 1))  # Hijo derecho está una columna a la derecha (col + 1)

    sorted_cols = sorted(col_map.keys())  # Ordenamos las columnas de izquierda a derecha
    return [col_map[col] for col in sorted_cols] # Devolvemos los valores agrupados por columna

# Función de prueba para el recorrido en orden vertical
def test_vertical_order_traversal():
    print("Testing Challenge 4: Vertical Order Traversal 📏")
    cases = [
        ([1, 2, 3, 4, 5, None, 6], [[4], [2], [1, 5], [3], [6]], "Normal tree"),
        ([1, 2, None, 3], [[3], [2], [1]], "Vertical line left"),
        ([], [], "Empty tree"),
        ([1], [[1]], "Single node"),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]], "Complete binary tree")
    ]
    for values, expected, label in cases:
        tree = BinaryTree()
        tree.build_tree_from_list(values)
        result = vertical_order_traversal(tree.root)
        assert result == expected, f"{label} FAILED ❌\nExpected: {expected}\nGot: {result}"
        print(f"{label} PASSED ✅")

# Ejecutar las pruebas
test_vertical_order_traversal()