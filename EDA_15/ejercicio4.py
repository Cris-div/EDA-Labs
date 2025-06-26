# Lista para almacenar los resultados de las pruebas
test_results = []

# Función auxiliar para registrar el resultado de una prueba
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"  # Ícono de éxito o fallo
    test_results.append(f"{emoji} {test_name}")  # Agrega el resultado con el nombre del test

# Clase que representa un grafo no dirigido usando lista de adyacencia
class Graph:
    def __init__(self):
        # Diccionario donde cada vértice apunta a una lista de vértices vecinos
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Agrega un vértice si aún no existe
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Agrega una arista bidireccional (no dirigida) entre vertex1 y vertex2
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def find_path(self, start_vertex, end_vertex):
        # Encuentra un camino del vértice de inicio al de fin usando BFS
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []  # Si alguno no existe, no hay camino
        if start_vertex == end_vertex:
            return [start_vertex]  # Si son iguales, camino es el mismo vértice

        visited = set()  # Conjunto de vértices ya visitados
        queue = [(start_vertex, [start_vertex])]  # Cola con pares (actual, camino hasta aquí)

        while queue:
            current, path = queue.pop(0)  # Desencola el primer elemento
            if current == end_vertex:
                return path  # Camino encontrado
            visited.add(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
        return []  # Si termina el recorrido y no se encuentra el camino

    def is_connected(self, vertex1, vertex2):
        # Retorna True si hay algún camino entre vertex1 y vertex2
        return len(self.find_path(vertex1, vertex2)) > 0

# Función que ejecuta pruebas específicas sobre caminos y conectividad
def test_1_4():
    graph = Graph()
    
    # Construcción del grafo: Lima - Cusco - Arequipa (camino indirecto), Trujillo aislado
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_vertex("Trujillo")  # Sin conexiones
    
    # 1.4.1 Verifica que se pueda encontrar un camino directo entre Lima y Cusco
    path = graph.find_path("Lima", "Cusco")
    record_test("1.4.1 Direct connection path", path == ["Lima", "Cusco"])
    
    # 1.4.2 Verifica un camino indirecto entre Lima y Arequipa (a través de Cusco)
    path = graph.find_path("Lima", "Arequipa")
    is_valid_path = len(path) == 3 and path[0] == "Lima" and path[-1] == "Arequipa"
    record_test("1.4.2 Indirect connection path", is_valid_path)
    
    # 1.4.3 Caso sin camino: Lima y Trujillo no están conectados
    path = graph.find_path("Lima", "Trujillo")
    record_test("1.4.3 No path case", path == [])
    
    # 1.4.4 Camino hacia uno mismo: debe devolver una lista con el mismo vértice
    path = graph.find_path("Lima", "Lima")
    record_test("1.4.4 Self path", path == ["Lima"])
    
    # 1.4.5 Verificación de conectividad: debe ser True para Lima-Arequipa, False para Lima-Trujillo
    connected = graph.is_connected("Lima", "Arequipa")
    not_connected = graph.is_connected("Lima", "Trujillo")
    record_test("1.4.5 Connectivity check", connected and not not_connected)

# 🚀 Ejecuta los tests definidos
test_1_4()

# 📋 Muestra el resultado de cada prueba
for r in test_results:
    print(r)
