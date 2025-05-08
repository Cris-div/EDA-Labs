class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if not self.items:
            return None
        return self.items.pop(-1)
        

# ✅ Test cases
dq = Deque()
print(dq.remove_rear() == None) # 📭 Deque vacío
dq.add_rear(1)
print(dq.remove_rear() == 1) # 🥇 Un elemento
dq.add_rear(2)
dq.add_rear(3)
print(dq.remove_rear() == 3) # 🔄 Último elemento
dq.add_front(4)
print(dq.remove_rear() == 2) # 📊 Elemento al final