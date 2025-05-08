class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def display(self):
        return str(self.items)

# ✅ Test cases
q = Queue()
print(q.display() == "[]") # 📭 Cola vacía
q.enqueue(1)
print(q.display() == "[1]") # 🥇 Un elemento
q.enqueue(2)
q.enqueue(3)
print(q.display() == "[1, 2, 3]") # 📊 Tres elementos
q.dequeue()
print(q.display() == "[2, 3]") # 🔄 Después de dequeue
print(isinstance(q.display(), str)) # 📝 Tipo cadena