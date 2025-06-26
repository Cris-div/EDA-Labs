# Lista para almacenar los resultados de los tests
test_results = []

# Función para registrar el resultado de una prueba con un emoji visual
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# Clase que representa un grafo no dirigido utilizando una lista de adyacencia
class Graph:
    def __init__(self):
        # Diccionario para almacenar los vértices y sus vecinos
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Agrega un vértice al grafo si no existe aún
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Agrega una arista bidireccional entre vertex1 y vertex2
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def get_degree(self, vertex):
        # Retorna el grado (cantidad de conexiones) de un vértice
        if vertex in self.adjacency_list:
            return len(self.adjacency_list[vertex])
        return 0  # Si el vértice no existe, retorna 0

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        # Encuentra todos los caminos posibles entre dos vértices usando DFS

        def dfs(current, target, path, all_paths):
            # Si se supera el límite de longitud, se detiene
            if max_length is not None and len(path) > max_length:
                return
            # Si se llega al destino, se guarda el camino
            if current == target:
                all_paths.append(path.copy())
                return
            # Explora vecinos no visitados aún
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, target, path, all_paths)
                    path.pop()

        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []  # Si alguno no existe, no hay caminos

        all_paths = []
        dfs(start_vertex, end_vertex, [start_vertex], all_paths)
        return all_paths

    def get_connected_components(self):
        # Encuentra todos los componentes conectados del grafo usando DFS
        visited = set()
        components = []

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                stack = [vertex]
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.append(current)
                        # Agrega los vecinos no visitados al stack
                        stack.extend([n for n in self.adjacency_list[current] if n not in visited])
                components.append(component)  # Agrega componente completo a la lista
        return components

# Función que ejecuta pruebas sobre funciones de análisis del grafo
def test_1_5():
    graph = Graph()
    
    # Construye un grafo con dos componentes conectados
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Componente separado
    
    # 1.5.1 Verifica el grado del vértice Lima (debe tener 2 vecinos)
    lima_degree = graph.get_degree("Lima")
    record_test("1.5.1 Degree calculation", lima_degree == 2)
    
    # 1.5.2 Verifica si existen múltiples caminos de Lima a Arequipa con longitud máxima de 3
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    has_multiple_paths = len(paths) >= 2
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)
    
    # 1.5.3 Verifica que el grafo tiene exactamente 2 componentes conectados
    components = graph.get_connected_components()
    has_two_components = len(components) == 2
    record_test("1.5.3 Connected components", has_two_components)
    
    # 1.5.4 Verifica que un grafo vacío no tenga componentes conectados
    empty_graph = Graph()
    empty_components = empty_graph.get_connected_components()
    record_test("1.5.4 Empty graph analysis", empty_components == [])
    
    # 1.5.5 Verifica que se maneje correctamente un vértice inexistente al pedir su grado
    degree = graph.get_degree("NonExistent")
    record_test("1.5.5 Non-existent vertex handling", degree == 0 or degree is None)

# 🚀 Ejecuta los tests
test_1_5()

# 📋 Imprime los resultados
for r in test_results:
    print(r)
