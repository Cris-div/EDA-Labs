class QueueWhitStack:
    def __init__(self):
        self.stack_new=[]
        self.stack_old=[]
    
    def is_empty(self):
        return not self.stack_new and not self.stack_old
    
    
    def enqueue(self,item):
        self.stack_new.append(item)
        
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!!")
        if not self.stack_old:
            while self.stack_new:
                self.stack_old.append(self.stack_new.pop())
        return self.stack_old.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        if not self.stack_old:
            while self.stack_new:
                self.stack_old.append(self.stack_new.pop())
        return self.stack_old[-1] 
    
    def size(self):
        return len(self.stack_new) + len(self.stack_old)

def test_queue():
    # Crear una instancia de la cola
    q = QueueWhitStack()

    # Prueba de enqueue (agregar elementos)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Verificar el tamaño
    assert q.size() == 3, "Error: El tamaño debería ser 3"

    # Verificar el primer elemento con peek (sin eliminar)
    assert q.peek() == 10, "Error: El primer elemento debería ser 10"

    # Prueba de dequeue (eliminar el primer elemento)
    assert q.dequeue() == 10, "Error: El primer elemento (10) debería ser eliminado"

    # Verificar el tamaño después del dequeue
    assert q.size() == 2, "Error: El tamaño debería ser 2 después del dequeue"

    # Verificar el siguiente primer elemento
    assert q.peek() == 20, "Error: El siguiente primer elemento debería ser 20"

    # Prueba de otro dequeue
    assert q.dequeue() == 20, "Error: El siguiente primer elemento (20) debería ser eliminado"

    # Verificar el tamaño después del segundo dequeue
    assert q.size() == 1, "Error: El tamaño debería ser 1 después del segundo dequeue"

    # Verificar el siguiente primer elemento
    assert q.peek() == 30, "Error: El siguiente primer elemento debería ser 30"

    # Último dequeue
    assert q.dequeue() == 30, "Error: El último elemento (30) debería ser eliminado"

    # Verificar que la cola esté vacía
    assert q.is_empty() == True, "Error: La cola debería estar vacía después de eliminar todos los elementos"

    print("¡Todas las pruebas pasaron correctamente!")

# Ejecutar las pruebas
test_queue()

    
    