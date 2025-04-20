class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size_count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size_count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.front.data

    def size(self):
        return self.size_count

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        return f"Queue: [{', '.join(result)}]"
    
def hot_potato(names, max_passes):
    """Simulate the Hot Potato game."""
    import random
    queue=LinkedQueue()

    for name in names:
        queue.enqueue(name)

    print(f"Starting Hot Potato game with {len(names)} players: {', '.join(names)} 🎮")

    while queue.size() > 1:
        passes=random.randint(1,max_passes)
        print(f"\nPassing potato {passes} times...")

        for _ in range(passes):
            current_player=queue.dequeue()
            print(f"  Potato passed to {current_player} 🥔")
            queue.enqueue(current_player)

        eliminated = queue.dequeue()
        print(f"BOOM! {eliminated} is out of the game! 💥")

        players_list = []
        temp_player = queue.dequeue()
        players_list.append(temp_player)
        queue.enqueue(temp_player)

        for _ in range(queue.size() - 1):
            temp_player = queue.dequeue()
            players_list.append(temp_player)
            queue.enqueue(temp_player)
        
        print(f"Remaining players: {', '.join(players_list)} 👥")
    
    winner = queue.dequeue()
    print(f"\n🏆 {winner} wins the Hot Potato game! 🏆")
    return winner

def test_hot_potato():
    """Test Hot Potato game simulation."""
    players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    max_passes = 7
    winner = hot_potato(players, max_passes)
    print(f"Game winner: {winner} 🥔👑")

test_hot_potato()