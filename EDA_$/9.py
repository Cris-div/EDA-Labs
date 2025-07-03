test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        return self._items.append(item)

    def dequeue(self):
        """Remove and return front item or None if empty."""
        # Your solution here 🛠️
        return self._items.pop(0) if self._items else None

    def peek(self):
        """Return front item without removing or None if empty."""
        # Your solution here 🛠️
        return self._items[0] if self._items else None

def test_o5_1():
    queue_array = Queue()
    record_test("o5.1.1 empty behavior",
        queue_array.dequeue() is None and queue_array.peek() is None)

    queue_array.enqueue(1)
    queue_array.enqueue(2)
    queue_array.enqueue(3)
    record_test("o5.1.2 FIFO order",
        queue_array.dequeue() == 1 and
        queue_array.dequeue() == 2 and
        queue_array.dequeue() == 3)

    queue_array.enqueue("x")
    record_test("o5.1.3 peek preserves",
        queue_array.peek() == "x" and queue_array.dequeue() == "x")

    queue_array.enqueue(None)
    queue_array.enqueue("y")
    record_test("o5.1.4 mixed types",
        queue_array.peek() is None and queue_array.dequeue() is None)

    val_removed = queue_array.dequeue()
    val_peeked  = queue_array.peek()
    record_test("o5.1.5 return types",
        isinstance(val_removed, (int, str, type(None))) and
        isinstance(val_peeked,   (int, str, type(None))))

# 🚀 Run tests
test_o5_1()

# 📋 Summary
for result in test_results:
    print(result)