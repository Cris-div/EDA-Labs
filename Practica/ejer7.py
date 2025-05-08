class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
       if (self.rear+1)%self.capacity==self.front:
           return False
       if self.front==-1:
           self.front=0
           self.rear=0
           self.queue[self.rear]=item
           return True
       self.rear=(self.rear+1)%self.capacity
       self.queue[self.rear]=item
       return True

# ✅ Test cases
cq = CircularQueue(2)
print(cq.enqueue("A") == True) # ✅ Primer elemento
print(cq.front == 0 and cq.rear == 0) # 🎯 Posiciones correctas
print(cq.enqueue("B") == True) # ✅ Segundo elemento
print(cq.enqueue("C") == False) # ❌ Tercer elemento
print(isinstance(cq.enqueue("X"), bool)) # 🔍 Tipo booleano