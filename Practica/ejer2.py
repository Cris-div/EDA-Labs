class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]
        
       

# ✅ Test cases
q = Queue()
print(q.peek() == None) # 📭 Cola vacía
q.enqueue("primero")
print(q.peek() == "primero") # 👁️ Ver sin eliminar
q.enqueue("segundo")
print(q.peek() == "primero") # 🥇 Sigue siendo el primero
q.items = []
print(q.peek() == None) # 📭 Cola vacía de nuevo
print(isinstance(q.peek(), str) or q.peek() == None) # 📝 Tipo correcto

