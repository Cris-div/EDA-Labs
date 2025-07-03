test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class CircularArrayQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self._queue = [None] * capacity
        self._front = 0
        self._rear = -1
        self._count = 0

    def enqueue(self, item) -> bool:
        """Add item if not full, return True; else False."""
        # Your solution here 🎯
        if self._count< self.capacity:
            self._rear= (self._rear+1)%self.capacity
            self._queue[self._rear]=item
            self._count+=1
            return True
        return False

    def dequeue(self):
        """Remove and return front item or None if empty."""
        # Your solution here 🔄
        if self._count >0:
            item=self._queue[self._front]
            self._front=(self._front+1)%self.capacity
            self._count-=1
            return item
        return None

    def size(self) -> int:
        """Return number of elements."""
        # Your solution here 📏
        return self._count

def test_o6_1():
    circular_array_queue = CircularArrayQueue(3)
    circular_array_queue.enqueue("A")
    circular_array_queue.enqueue("B")
    circular_array_queue.enqueue("C")
    record_test(
        "o6.1.1 basic",
        circular_array_queue.dequeue() == "A" and
        circular_array_queue.dequeue() == "B" and
        circular_array_queue.dequeue() == "C" and
        circular_array_queue.size() == 0
    )

    circular_array_queue = CircularArrayQueue(3)
    circular_array_queue.enqueue(1)
    circular_array_queue.enqueue(2)
    circular_array_queue.enqueue(3)
    circular_array_queue.dequeue()
    circular_array_queue.enqueue(4)
    record_test(
        "o6.1.2 wrap",
        circular_array_queue.dequeue() == 2 and
        circular_array_queue.dequeue() == 3 and
        circular_array_queue.dequeue() == 4 and
        circular_array_queue.size() == 0
    )

    circular_array_queue = CircularArrayQueue(2)
    circular_array_queue.enqueue("X")
    circular_array_queue.enqueue("Y")
    circular_array_queue.dequeue()
    circular_array_queue.dequeue()
    record_test(
        "o6.1.3 empty",
        circular_array_queue.dequeue() is None and
        circular_array_queue.size() == 0
    )

    circular_array_queue = CircularArrayQueue(2)
    circular_array_queue.enqueue(9)
    circular_array_queue.enqueue(8)
    record_test(
        "o6.1.4 full",
        circular_array_queue.enqueue(7) is False and
        circular_array_queue.size() == 2
    )

    circular_array_queue = CircularArrayQueue(1)
    record_test(
        "o6.1.5 types",
        isinstance(circular_array_queue.enqueue("Z"), bool) and
        isinstance(circular_array_queue.dequeue(), (str, type(None))) and
        isinstance(circular_array_queue.size(), int)
    )

# 🚀 Run tests
test_o6_1()

# 📋 Summary
for result in test_results:
    print(result)