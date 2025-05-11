# Clase Nodo para representar un nodo en el árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None     # Hijo izquierdo
        self.right = None    # Hijo derecho

# Clase Árbol Binario general (no necesariamente un BST)
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

    # Recorrido inorder: izquierda, nodo, derecha
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []  # Inicializamos la lista de resultados
        if node:
            self.inorder_traversal(node.left, result)  # Visitamos el subárbol izquierdo
            result.append(node.value)  # Visitamos el nodo
            self.inorder_traversal(node.right, result)  # Visitamos el subárbol derecho
        return result

# Función para serializar el árbol a una cadena (BFS)
def serialize(root):
    if not root:
        return "#"
    queue = [root]  # Usamos una cola para recorrer el árbol en nivel
    result = []  # Lista para almacenar los valores serializados
    while queue:
        node = queue.pop(0)  # Extraemos el primer nodo de la cola
        if node:
            result.append(str(node.value))  # Agregamos el valor del nodo a la lista
            queue.append(node.left)  # Añadimos el hijo izquierdo a la cola
            queue.append(node.right)  # Añadimos el hijo derecho a la cola
        else:
            result.append("#")  # Representamos los nodos vacíos con "#"
    return ",".join(result)  # Devolvemos la cadena serializada

# Función para deserializar una cadena a un árbol
def deserialize(data):
    if data == "#":
        return None  # Si la cadena es "#", significa que no hay árbol
    values = data.split(",")  # Separamos la cadena en valores
    root = TreeNode(int(values[0]))  # El primer valor es la raíz
    queue = [root]  # Usamos una cola para reconstruir el árbol
    i = 1
    while queue:
        node = queue.pop(0)  # Extraemos el primer nodo de la cola
        if values[i] != "#":
            node.left = TreeNode(int(values[i]))  # Creamos el hijo izquierdo si no es "#"
            queue.append(node.left)  # Lo añadimos a la cola
        i += 1
        if values[i] != "#":
            node.right = TreeNode(int(values[i]))  # Creamos el hijo derecho si no es "#"
            queue.append(node.right)  # Lo añadimos a la cola
        i += 1
    return root

# Función para probar la serialización y deserialización
def test_serialize_deserialize():
    print("Testing Challenge 2: Serialization/Deserialization 💾")
    cases = [
        ([1, 2, 3, 4, 5, None, 6], "Normal tree"),  # Árbol binario normal
        ([], "Empty tree"),  # Árbol vacío
        ([42], "Single node"),  # Árbol con un solo nodo
        ([1, 2, None, 3], "Left-skewed"),  # Árbol sesgado a la izquierda
        ([1, None, 2, None, None, None, 3], "Right-skewed")  # Árbol sesgado a la derecha
    ]
    for values, label in cases:
        print(f"Running test: {label}")
        tree = BinaryTree()  # Crear el árbol
        tree.build_tree_from_list(values)  # Construir el árbol a partir de la lista
        serialized = serialize(tree.root)  # Serializar el árbol
        deserialized_root = deserialize(serialized)  # Deserializar el árbol
        original_inorder = tree.inorder_traversal(tree.root)  # Recorrido inorder del árbol original
        new_inorder = tree.inorder_traversal(deserialized_root)  # Recorrido inorder del árbol deserializado
        assert original_inorder == new_inorder, f"{label} FAILED"  # Verificamos que ambos recorridos sean iguales
        print(f"{label} PASSED ✅")  # Si pasa, se imprime que la prueba fue exitosa

# Ejecutar las pruebas
test_serialize_deserialize()