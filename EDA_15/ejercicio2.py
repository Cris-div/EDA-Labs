# Lista donde se almacenan los resultados de los tests
test_results = []

# Función auxiliar para registrar y mostrar el resultado de cada prueba
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# Clase Graph: representa un grafo no dirigido mediante una lista de adyacencia
class Graph:
    def __init__(self):
        # Diccionario vacío donde cada clave será un vértice y su valor una lista de vecinos
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Agrega un vértice al grafo si aún no existe, con una lista vacía de vecinos
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            
    def get_vertices(self):
        # Devuelve una lista con todos los vértices del grafo
        return list(self.adjacency_list.keys())
    
    def get_vertex_count(self):
        # Devuelve la cantidad de vértices en el grafo
        return len(self.adjacency_list)
    
    def has_vertex(self, vertex):
        # Verifica si un vértice existe en el grafo
        return vertex in self.adjacency_list

# Función de prueba para validar el funcionamiento de add_vertex y métodos relacionados
def test_1_2():
    graph = Graph()
    
    # 1.2.1 Agrega un solo vértice y verifica si fue añadido
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))
    
    # 1.2.2 Agrega varios vértices y verifica la cantidad total
    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)
    
    # 1.2.3 Intenta agregar un vértice duplicado y verifica que no se duplique
    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima")  # Duplicado
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)
    
    # 1.2.4 Verifica que un vértice nuevo no tenga conexiones (aislado)
    lima_neighbors = graph.adjacency_list.get("Lima", [])
    record_test("1.2.4 Vertex isolation", len(lima_neighbors) == 0)
    
    # 1.2.5 Agrega otro vértice y verifica que se refleje en la lista de vértices
    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())

# 🚀 Ejecuta los tests
test_1_2()

# 📋 Muestra el resumen de resultados
for r in test_results:
    print(r)
