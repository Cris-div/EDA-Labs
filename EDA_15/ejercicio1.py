# Lista global donde se almacenan los resultados de los tests
test_results = []

# Función auxiliar para registrar el resultado de un test con su nombre y condición (True/False)
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"  # Muestra un ícono según el resultado
    test_results.append(f"{emoji} {test_name}")  # Agrega el resultado a la lista

# Clase que representa un grafo no dirigido usando lista de adyacencia
class Graph:
    def __init__(self):
        # Inicializa una lista de adyacencia vacía (sin vértices)
        self.adjacency_list = {}
    
    def get_vertices(self):
        # Devuelve una lista con todos los vértices del grafo
        return list(self.adjacency_list.keys())
    
    def get_vertex_count(self):
        # Devuelve el número total de vértices en el grafo
        return len(self.adjacency_list)
        
    def has_vertex(self, vertex):
        # Verifica si un vértice existe en el grafo
        return vertex in self.adjacency_list

# Función que ejecuta una serie de pruebas unitarias sobre la clase Graph
def test_1_1():
    # 1.1.1 Verifica que un grafo recién creado tenga 0 vértices
    graph = Graph()
    record_test("1.1.1 Empty graph initialization", graph.get_vertex_count() == 0)
    
    # 1.1.2 Simula la existencia de vértices añadiéndolos manualmente al grafo
    graph.adjacency_list = {"Lima": [], "Cusco": []}
    record_test("1.1.2 Vertex counting", graph.get_vertex_count() == 2)
    
    # 1.1.3 Verifica si el vértice "Lima" existe
    record_test("1.1.3 Vertex existence check", graph.has_vertex("Lima") == True)
    
    # 1.1.4 Verifica si un vértice inexistente ("Lima") retorna False en un grafo vacío
    empty_graph = Graph()
    record_test("1.1.4 Empty graph edge case", empty_graph.has_vertex("Lima") == False)
    
    # 1.1.5 Verifica que la función get_vertices devuelva una lista
    record_test("1.1.5 Type validation", isinstance(graph.get_vertices(), list))

# 🚀 Ejecuta las pruebas
test_1_1()

# 📋 Imprime el resumen de resultados
for r in test_results:
    print(r)
