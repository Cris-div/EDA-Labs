test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedQueue:
    def __init__(self):
        self.rear = None
        self._count = 0

    def enqueue(self, data) -> bool:
        """Add node at rear, return True."""
        # Your solution here 🔗
        node=Node(data)
        if self.rear is None:
            node.next=node
            self.rear=node
        else:
            node.next=self.rear.next
            self.rear.next=node
            self.rear=node
        self._count+=1
        return True

    def dequeue(self):
        """Remove and return front data or None if empty."""
        # Your solution here 🔄
        if self.rear is None:
            return None
        front_node=self.rear.next
        data=front_node.data
        if front_node is self.rear:
            self.rear=None
        else:
            self.rear.next=front_node.next
        self._count-=1
        return data
            

    def size(self) -> int:
        """Return number of elements."""
        # Your solution here 📏
        return self._count

def test_o6_2():
    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.1 empty",
        circular_linked_queue.dequeue() is None and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.2 single",
        circular_linked_queue.enqueue("A") is True and
        circular_linked_queue.dequeue() == "A" and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    circular_linked_queue.enqueue(1)
    circular_linked_queue.enqueue(2)
    circular_linked_queue.enqueue(3)
    record_test(
        "o6.2.3 multiple",
        circular_linked_queue.dequeue() == 1 and
        circular_linked_queue.dequeue() == 2 and
        circular_linked_queue.dequeue() == 3 and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    circular_linked_queue.enqueue("X")
    circular_linked_queue.dequeue()
    record_test(
        "o6.2.4 empty-again",
        circular_linked_queue.dequeue() is None and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.5 types",
        isinstance(circular_linked_queue.enqueue("Z"), bool) and
        isinstance(circular_linked_queue.dequeue(), (int, str, type(None))) and
        isinstance(circular_linked_queue.size(), int)
    )

# 🚀 Run tests
test_o6_2()

# 📋 Summary
for result in test_results:
    print(result)